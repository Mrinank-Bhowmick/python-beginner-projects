#!/usr/bin/env python3

"""PyQt5 application to play videos, with YouTube support."""

import math
import sys
from datetime import timedelta

from PyQt5.QtCore import QDir, Qt, QUrl
from PyQt5.QtMultimedia import QAudio, QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSlider,
    QStyle,
    QVBoxLayout,
    QWidget,
)
from youtube_dl import DownloadError, YoutubeDL


def seconds_to_timestamp(seconds: float, ms: bool = False) -> str:
    """
    Return timestamp from seconds.

    Include milliseconds if ms is True.
    """
    if not ms:
        seconds = math.ceil(seconds)
    return str(timedelta(seconds=seconds))


class VideoWindow(QMainWindow):
    """Window with video widget and media controls."""

    def __init__(self, parent=None) -> None:
        """Initialise parent and window."""
        super().__init__(parent)
        self.setWindowTitle("QTube")

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        self.searchBox = QLineEdit()
        self.searchBox.setPlaceholderText("Enter URL or search query")
        self.searchBox.returnPressed.connect(self.search)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.togglePlay)

        self.elapsedLabel = QLabel("00:00:00")
        self.durationLabel = QLabel("--:--:--")
        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.volumeLabel = QLabel(f"🔈 {self.mediaPlayer.volume()}%")
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(self.mediaPlayer.volume())
        self.volumeSlider.valueChanged.connect(self.setVolume)

        self.speedLabel = QLabel(f"Speed: {self.mediaPlayer.playbackRate()}x")
        self.speedSlider = QSlider(Qt.Horizontal)
        self.speedSlider.setRange(1, 16)
        self.speedSlider.setValue(1)
        self.speedSlider.valueChanged.connect(self.setSpeed)

        self.bufferLabel = QLabel("Buffer: N/A")

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        openAction = QAction(
            self.style().standardIcon(QStyle.SP_DirIcon), "&Open", self
        )
        openAction.setShortcut("Ctrl+O")
        openAction.setStatusTip("Open video")
        openAction.triggered.connect(self.openFile)

        exitAction = QAction(
            self.style().standardIcon(QStyle.SP_DialogCloseButton), "&Exit", self
        )
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(self.closeWindow)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

        widget = QWidget(self)
        self.setCentralWidget(widget)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.elapsedLabel)
        controlLayout.addWidget(self.positionSlider, 1)
        controlLayout.addWidget(self.durationLabel)
        controlLayout.addWidget(self.volumeLabel)
        controlLayout.addWidget(self.volumeSlider)

        advancedLayout = QHBoxLayout()
        advancedLayout.addWidget(self.speedLabel)
        advancedLayout.addWidget(self.speedSlider)
        advancedLayout.addWidget(self.bufferLabel)
        advancedLayout.addWidget(self.errorLabel, 1, Qt.AlignRight)

        layout = QVBoxLayout()
        layout.addWidget(self.searchBox)
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addLayout(advancedLayout)

        widget.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.bufferStatusChanged.connect(self.bufferStatusChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

    def search(self) -> None:
        """Search for query or URL and play it."""
        query = self.searchBox.text()
        if not query:
            return

        with YoutubeDL() as ydl:
            try:
                video = ydl.extract_info(query, download=False)
            except DownloadError:
                entries = ydl.extract_info(f"ytsearch:{query}", download=False)[
                    "entries"
                ]
                try:
                    video = entries[0]
                except IndexError:
                    video = {}
        if video:
            self.mediaPlayer.setMedia(QMediaContent(QUrl(video["formats"][-1]["url"])))
            self.playButton.setEnabled(True)

    def openFile(self) -> None:
        """Open and play a local file."""
        fileName, _ = QFileDialog.getOpenFileName(self, "Open video", QDir.homePath())
        if fileName:
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def closeWindow(self) -> None:
        """Handle closing the window."""
        self.close()

    def togglePlay(self) -> None:
        """Handle play/pause toggle."""
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state: QMediaPlayer.State) -> None:
        """Handle media state change event."""
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def bufferStatusChanged(self, percentFilled: int) -> None:
        """Update buffer label with current buffer percentage."""
        self.bufferLabel.setText(f"Buffer: {percentFilled}%")

    def positionChanged(self, position: int) -> None:
        """Update slider and label with current position."""
        self.positionSlider.setValue(position)
        self.elapsedLabel.setText(seconds_to_timestamp(position / 1000))

    def durationChanged(self, duration: int) -> None:
        """Update slider and label with total duration."""
        self.positionSlider.setRange(0, duration)
        self.durationLabel.setText(seconds_to_timestamp(duration / 1000))

    def setPosition(self, position: int) -> None:
        """Handle position slider movement events."""
        self.mediaPlayer.setPosition(position)

    def setVolume(self, position: int) -> None:
        """Handle volume slider movement events."""
        self.volumeLabel.setText(f"🔈 {position}%")
        volume = QAudio.convertVolume(
            position / 100, QAudio.LogarithmicVolumeScale, QAudio.LinearVolumeScale
        )
        self.mediaPlayer.setVolume(round(volume * 100))

    def setSpeed(self, position: int) -> None:
        """Handle speed slider movement events."""
        self.mediaPlayer.setPlaybackRate(position)
        self.speedLabel.setText(f"Speed: {self.mediaPlayer.playbackRate()}x")

    def handleError(self) -> None:
        """Handle errors raised by media player and disable playback."""
        self.playButton.setEnabled(False)
        self.errorLabel.setText(f"Error: {self.mediaPlayer.errorString()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = VideoWindow()
    player.resize(640, 480)
    player.show()
    sys.exit(app.exec_())

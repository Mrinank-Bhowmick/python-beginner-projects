# Import necessary libraries
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys


# Define the main window class
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Create a QWebEngineView widget
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)

        # Show the window maximized
        self.showMaximized()

        # Create a navigation toolbar
        navbar = QToolBar()
        navbar.adjustSize()
        self.addToolBar(navbar)

        # Add a back button to the toolbar
        back_btn = QAction("⮜", self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Add a forward button to the toolbar
        forward_btn = QAction("⮞", self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Add a reload button to the toolbar
        reload_btn = QAction("⟳", self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Add a URL bar to the toolbar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.open_url)
        navbar.addWidget(self.url_bar)

        # Update the URL bar when the browser URL changes
        self.browser.urlChanged.connect(self.update_url)

    # Load the URL entered in the URL bar
    def open_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    # Update the URL bar when the browser URL changes
    def update_url(self, q):
        self.url_bar.setText(q.toString())


# Create the application and main window
app = QApplication(sys.argv)
QApplication.setApplicationName("EFFLUX browser")
window = MainWindow()
app.exec_()

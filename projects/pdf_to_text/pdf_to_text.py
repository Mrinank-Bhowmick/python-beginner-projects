import sys
import os
from PyPDF2 import PdfReader
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class PDFTextExtractorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("PDF Text Extractor")

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        self.btn_open_pdf = QPushButton("Open PDF File", self)
        self.btn_open_pdf.clicked.connect(self.openPDF)

        self.btn_extract_text = QPushButton("Extract Text", self)
        self.btn_extract_text.clicked.connect(self.extractText)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.btn_open_pdf)
        layout.addWidget(self.btn_extract_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def openPDF(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        pdf_file, _ = QFileDialog.getOpenFileName(
            self,
            "Open PDF File",
            "",
            "PDF Files (*.pdf);;All Files (*)",
            options=options,
        )
        if pdf_file:
            self.pdf_path = pdf_file

    def extractText(self):
        if hasattr(self, "pdf_path"):
            pdf_path = self.pdf_path
            text = self.extractTextFromPDF(pdf_path)
            self.text_edit.setPlainText(text)
        else:
            self.text_edit.setPlainText("No PDF file selected.")

    def extractTextFromPDF(self, pdf_path):
        pdf_text = ""
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            pdf_text += page.extract_text()
        return pdf_text


def main():
    app = QApplication(sys.argv)
    window = PDFTextExtractorApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

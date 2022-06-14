import pyttsx3
import PyPDF2

book = open("Article.pdf", "rb")  # Enter your own PDF file path
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

for num in range(7, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

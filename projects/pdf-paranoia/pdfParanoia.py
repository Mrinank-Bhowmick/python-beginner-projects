import os
import PyPDF2


def encryptPDFs(root, password):
    """Encrypts all pdfs folder walk
    Args:
       root (str): folder path to walk
       password (str): password to encrypt pdfs with
    Returns:
       None
    """
    for folder, subfolder, fileList in os.walk(root):
        for file in fileList:
            if file.endswith(".pdf"):
                filepath = os.path.join(os.path.abspath(folder), file)
                pdfFileObj = open(filepath, "rb")
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                if not pdfReader.isEncrypted:
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    pdfWriter.encrypt(password)
                    newPath = (
                        os.path.dirname(filepath)
                        + "/untitled folder/"
                        + ("_encrypted.".join(os.path.basename(filepath).split(".")))
                    )
                    resultPdf = open(newPath, "wb")
                    pdfWriter.write(resultPdf)
                    resultPdf.close()


def decryptPDFs(root, password):
    """Decrypts all pdfs folder walk
    Args:
       root (str): folder path to walk
       password (str): password to decrypt pdfs with
    Returns:
       None
    """
    for folder, subfolder, fileList in os.walk(root):
        for file in fileList:
            if file.endswith("_encrypted.pdf"):
                filepath = os.path.join(os.path.abspath(folder), file)
                pdfFileObj = open(filepath, "rb")
                pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

                if pdfReader.isEncrypted:
                    success = pdfReader.decrypt(password)

                    if success:
                        pdfWriter = PyPDF2.PdfFileWriter()
                        for pageNum in range(pdfReader.numPages):
                            pdfWriter.addPage(pdfReader.getPage(pageNum))
                        newPath = (
                            os.path.dirname(filepath)
                            + "/"
                            + "".join(os.path.basename(filepath).split("_encrypted"))
                        )
                        resultPdf = open(newPath, "wb")
                        pdfWriter.write(resultPdf)
                        resultPdf.close()
                    else:
                        print("wrong password provided")


if __name__ == "__main__":

    password = input("Enter encryption password: ")
    encryptPDFs(".", password)
    decryptPDFs(".", password)

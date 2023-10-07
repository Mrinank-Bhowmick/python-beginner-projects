from email.message import EmailMessage
import ssl
import smtplib


def send_email():
    email_sender = input("\nEnter your email id :")
    email_password = "#put your password here"          #please read the README.md file to generate your own secure password

    email_reciever = input("\nEnter the email of the reciever :")

    subject = input("\nEnter the subject of the email : ")
    email_body = input("\nEnter the body/content of the email :")
    body = email_body

    em= EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciever, em.as_string())


send_email()
print(" Email sent successfully !!!")

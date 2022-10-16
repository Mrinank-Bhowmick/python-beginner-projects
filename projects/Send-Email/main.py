# importing the module

import smtplib
import os

# Get the username from environment variables.
# It can be assigned by running the following command
# export username=abc@abc.com     -> linux
# The same can be done for password
username = os.environ["username"]
receiver_add = "reciver789@gmail.com"
password = os.environ["password"]

# creating the SMTP server object by giving SMPT server address and port number

smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.ehlo()  # setting the ESMTP protocol

smtp_server.starttls()  # setting up to TLS connection
smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()

smtp_server.login(username, password)

msg_to_be_sent = """
Hello, receiver!
Hope you are doing well.
Welcome to PythonGeeks!
"""

# sending the mail by specifying the from and to address and the message

smtp_server.sendmail(username, receiver_add, msg_to_be_sent)
print("Successfully the mail is sent")  # priting a message on sending the mail

smtp_server.quit()

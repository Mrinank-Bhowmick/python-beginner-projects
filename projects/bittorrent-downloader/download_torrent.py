import subprocess
import imaplib
import imapclient
import pyzmail
from twilio.rest import Client


def check_for_torrents(imap_address, email_address, password, verified_creds):
    """Checks email for torrent links from verified accounts
    Args:
        imap_address (str): email providers imap address
        email_address (str): email address
        password (str): password for email
        verified_creds (dict): dict containing verfied email and password
    """
    imaplib._MAXLINE = 10000000
    imapObj = imapclient.IMAPClient(imap_address, ssl=True)
    # See https://support.google.com/accounts/answer/6010255 if (Login Error)
    imapObj.login(email_address, password)
    imapObj.select_folder("INBOX", readonly=True)
    UIDs = imapObj.search(["FROM " + verified_creds["email"]])

    links = []
    if UIDs:
        for u in UIDs:
            rawMessages = imapObj.fetch([u], ["BODY[]", "FLAGS"])
            message = pyzmail.PyzMessage.factory(rawMessages[u][b"BODY[]"])
            text = message.text_part.get_payload().decode(message.text_part.charset)

            if verified_creds["password"] in text:
                html = message.html_part.get_payload().decode(message.html_part.charset)
                links.append(html)

        imapObj.delete_messages(UIDs)
        imapObj.expunge()

    imapObj.logout()

    return links


def send_reminder(accountSID, authToken, myTwilioNumber, myCellPhone, message):
    """Sends a text using twilio
    Args:
        accountSID (str): twilio acct sid
        authToken (str): twilio authentication token
        myTwilioNumber (str): twilio number
        myCellPhone (str): my cell phone number
    Returns:
        None
    """
    twilioCli = Client(accountSID, authToken)
    message = twilioCli.messages.create(
        body="Rain Alert! Water is (not) wet. Grab an Umbrella bro.",
        from_=myTwilioNumber,
        to=myCellPhone,
    )


if __name__ == "__main__":

    torrent_client = ""  # enter path to qbittorent
    email = input("Enter your email: ")
    password = input("Enter your email password: ")

    links = check_for_torrents(
        "imap.gmail.com",
        email,
        password,
        {"email": "verified_email@ex.com", "password": "vpass"},
    )

    for l in links:
        tProc = subprocess.Popen(torrent_client + " " + l)
        tProc.wait()
        message = "Download Finished For: " + l
        send_reminder(
            "A***************",
            "A**************",
            "+1**********",
            "+1**********",
            message,
        )

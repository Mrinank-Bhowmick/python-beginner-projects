import random
import smtplib


def emailer(chores, emails):
    """emails random chores to emails
    Args:
        chores: list of chores
        emails: list of emails to send chores
    Returns:
        None
    """
    if not emails:
        print("emails list should not be empty")
        return

    if not chores:
        print("chores list should not be empty")
        return

    chores_dict = {}

    f = 0  # front of emails list

    while chores:

        randomChore = random.choice(chores)
        chores.remove(randomChore)
        email = emails[f]
        chores_dict.setdefault(email, [])
        chores_dict[email].append(randomChore)

        f = (f + 1) % len(emails)  # use list circularly

    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpObj.ehlo()

    email = input("Enter your email: ")
    password = input("Enter your email password: ")

    smtpObj.starttls()
    smtpObj.login(email, password)
    # See https://support.google.com/accounts/answer/6010255 if (Bad Credentials Error)

    for k, v in chores_dict.items():
        c = ", ".join(v)
        print("Sending email to %s..." % k)
        sendmailStatus = smtpObj.sendmail(
            email, k, "Subject: Your Chores.\nHi There!, {} are your chores".format(c)
        )
        if sendmailStatus != {}:
            print(
                "There was a problem sending email to %s: %s" % (email, sendmailStatus)
            )

    smtpObj.quit()


if __name__ == "__main__":
    emailer(
        ["dishes", "bathroom", "vacuum", "walk dog"],
        ["example@yahoo.com, example2@yahoo.com"],
    )

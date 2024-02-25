import time

import pyautogui


def send_message(contact, message):
    """Sends message to an active slack contact
    Args:
        contact (str): contacts name on slack
        message (str): message to send to friend
    Returns:
        None
    """
    try:
        print("5 seconds to navigate to slack app..")
        time.sleep(5)

        # Use JumpTo slack feature
        pyautogui.hotkey("command", "k")
        time.sleep(1)
        # Enter contact name in search box, click enter
        pyautogui.typewrite(contact)
        time.sleep(1)
        pyautogui.typewrite(["enter"])
        time.sleep(1)

        active = pyautogui.locateOnScreen("active_identifier.png")

        if not active:
            print(f"{contact} is not active, skipped contact")
            return

        print("Contact is active, sending message...")
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(message)
        pyautogui.typewrite(["enter"])

    except KeyboardInterrupt:
        print("Process was cancelled..")


if __name__ == "__main__":

    contacts = input(
        "Enter contact list, separated by space >> Messi Onazi John: "
    ).split(" ")
    message = input("Enter the message you wish to send out to them: ")

    for c in contacts:
        contact = c.strip()
        send_message(contact, message)

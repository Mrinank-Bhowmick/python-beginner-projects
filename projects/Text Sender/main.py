import schedule
import time
import requests
import click


def main():
    while True:
        option = int(input("""\
            1: Send a one-time text message\n\
            2: Schedule a text message every day at a chosen time?\n\
            
            Option 1 or 2: """))

        if option in [1, 2]:
            break

    global number, message
    number, message = set_text_details()

    if option == 1:
        send_text()

    if option == 2:
        schedule_text()


def set_text_details():
    number = input("What phone number would you like to text? ")
    number = ''.join(c for c in number if c.isdigit())
    prompt = f"# Please enter your text message for phone number {number} above."
    message = click.edit('\n\n' + prompt)

    if message:
        message = message.split(prompt)[0].strip()

    return number, message


def send_text():
    resp = requests.post('https://textbelt.com/text', {
        'phone': number,
        'message': message,
        'key': 'textbelt',  # textbelt allows one free text per day using this key
    })

    print(resp.json())


def schedule_text():
    while True:
        scheduled_time = input(
            "Please enter the time you would like to send the text each day, in 24-hour time: ")

        scheduled_time = scheduled_time.replace(':', '')

        if scheduled_time.isdigit() and len(scheduled_time) == 4:
            if int(scheduled_time[:2]) <= 23 and int(scheduled_time[2:]) <= 59:
                scheduled_time = f'{scheduled_time[:2]}:{scheduled_time[2:]}'
                break

    schedule.every().day.at(scheduled_time).do(send_text)

    while True:
        schedule.run_pending()
        time.sleep(1)


main()

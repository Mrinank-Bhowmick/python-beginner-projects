# Instant Messenger Bot

Automates sending messages to active Slack contacts by simulating keyboard and mouse input.

## Example

```text
Enter contact list, separated by space >> Messi Onazi John: Alice Bob
Enter the message you wish to send out to them: Happy Monday everyone!
5 seconds to navigate to slack app..
Contact is active, sending message...
5 seconds to navigate to slack app..
Contact is active, sending message...
```

The bot uses Slack's Jump To shortcut to open each contact's chat and types the message automatically.

## How to run on localhost

```
pip install -r requirements.txt
python slack_messenger.py
```

## Dependencies

pyautogui.

# WhatsApp Random Message Sender

## Example

1. Run `python mesaage_spam.py`. A browser window opens to `https://web.whatsapp.com`.
2. Scan the QR code with your phone to log in to WhatsApp Web (you have 10 seconds).
3. Navigate to any open chat in WhatsApp Web.
4. The script automatically types and sends 10 random messages from `("Hello", "Hey", "Good Morning")`, pausing 1–3 seconds between each.

## Usage

1. Install required libraries:
   
- `pip install -r requirements.txt`
  
2. Run the script:
    ```
    python mesaage_spam.py
    ```

3. Follow on-screen instructions to log in to WhatsApp Web.

4. The script will send random messages to the current chat.

## Customization

- Edit the `messages` variable to change the list of messages to send.
- Adjust the sleep interval for message timing..

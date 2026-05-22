# Your-Desktop-Artificial-Assistant-(JARVIS)
Jarvis is a Python coding companion or your personal assistant . Point it to a python function, and it will execute it. As soon as you change and save your code, Jarvis will detect it, and will rerun the function. If an exception is raised, it will be displayed in the error panel. Enjoy your assistant at free of cost.

## Example

1. Run `python JARVIS2.0.py`. JARVIS greets you based on the time of day (e.g., "Good Morning!") and says "jarvis here at your service sir. How may I help you?".
2. Speak a command into your microphone. The console shows:
   ```
   Listening...
   Recognizing...
   User said: open youtube
   ```
3. JARVIS opens YouTube in your default browser. Other supported voice commands include "wikipedia [topic]", "what is the time", "tell me a joke", "open google", "open stackoverflow", "play music", and "email to Raj".
4. Say "quit" or "exit" to stop.

## Installation
### For windows users
(run those in command prompt/cmt/terminal)
For jarvis to listen to our voice/speech
`pip install speechRecognition`

To speak out, or text to speech
`pip install pyttsx3`

For advance control on browser
`pip install pywhatkit`

To get wikipedia data
`pip install wikipedia`

To get funny jokes
`pip install pyjokes`
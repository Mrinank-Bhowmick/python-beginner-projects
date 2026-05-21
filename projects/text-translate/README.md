## Install these necessary libraries

```pip install pygame``` 
```pip install gTTS``` 
```pip install tkinter``` 
```pip install googletrans==4.0.0-rc1``` 
## Pyodide-runnable

No — `main.py` uses the `translate` package which makes network requests, and `translate _GUIaudio.py` additionally uses `tkinter`, `gtts`, and `pygame`.

# WiFi Password Generator

Retrieves the saved Wi-Fi passwords on a Windows machine. It runs `netsh wlan` commands to list the stored wireless profiles and prints each network name alongside its password.

## How to run

```
python wifi.py
```

(Windows only.)

## Dependencies

Standard library only (`subprocess`).

## Pyodide-runnable

No — it shells out to Windows-only `netsh` system commands via `subprocess`, which the browser sandbox cannot run.

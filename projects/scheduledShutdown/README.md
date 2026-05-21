# Scheduled Shutdown

A console utility that asks for a number of minutes and then shuts down the computer after that delay using a system shutdown command.

## How to run

```sh
python shutdown.py
```

## Dependencies

Standard library only (uses `os` and `time`).

## Pyodide-runnable

No - it calls `os.system("shutdown ...")` to power off the host machine, which is not available in the browser sandbox.

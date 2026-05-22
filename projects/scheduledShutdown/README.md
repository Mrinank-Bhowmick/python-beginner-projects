# Scheduled Shutdown

A console utility that asks for a number of minutes and then shuts down the computer after that delay using a system shutdown command.

## Example

```text
Shutdown After ----> 30
Computer Will Now Shutdown in 30 Minutes

Computer Will Now Shutdown!
```

After the specified number of minutes the script executes the system shutdown command.

## How to run on localhost

```sh
python shutdown.py
```

## Dependencies

Standard library only (uses `os` and `time`).

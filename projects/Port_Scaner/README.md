# Port Scanner

Port Scanner is developed for:
checking if the port is open

## Example

```text
 ____           _     ____
|  _ \ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __
| |_) / _ \| '__| __| \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
|  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |
|_|   \___/|_|   \__| |____/ \___\__,_|_| |_|_| |_|\___|_|

Port Scanner
Enter the port to check: 80
Port is open
```

```text
Enter the port to check: 9999
Port is not open
```

## How to run on localhost

```sh
pip install pyfiglet
python port_scanner.py
```

## Dependencies

- pyfiglet
- socket (standard library)

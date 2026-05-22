# WiFi Password Generator

Retrieves the saved Wi-Fi passwords on a Windows machine. It runs `netsh wlan` commands to list the stored wireless profiles and prints each network name alongside its password.

## Example

```text
HomeNetwork                   |  MySecretPass123
OfficeWifi                    |  workpassword99
GuestNetwork                  |
```

Each saved wireless profile is printed with its name left-aligned in a 30-character column, followed by `|` and its stored password. Profiles that have no saved password (open networks) show an empty value.

## How to run on localhost

```
python wifi.py
```

(Windows only.)

## Dependencies

Standard library only (`subprocess`).

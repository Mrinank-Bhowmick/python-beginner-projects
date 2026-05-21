# Port Scanner

Port Scanner is developed for:
checking if the port is open

## How to run

```sh
pip install pyfiglet
python port_scanner.py
```

## Dependencies

- pyfiglet
- socket (standard library)

## Pyodide-runnable

No - it uses real TCP sockets (`socket.connect_ex`), which are not available in the browser sandbox.
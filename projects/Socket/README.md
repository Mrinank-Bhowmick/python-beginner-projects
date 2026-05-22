# Socket example

### Implementation of a socket in python

## Example

**Terminal 1 (server):**
```text
$ python ./server.py
Server runing in port  3000
New conection ('127.0.0.1', 54321)
b'Hello from client'
```

**Terminal 2 (client):**
```text
$ python ./client.py
b' Hello from server!'
```

## How to run on localhost

```bash
# fist run the server
python ./server.py
```

```bash
# then run the client
python ./client.py
```

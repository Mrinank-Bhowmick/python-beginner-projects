# Mongo CRUD

A small example of create/read/update/delete operations against a MongoDB database using `pymongo`. `conexao.py` opens the database connection and `usuario.py` defines a `Usuario` class with methods to insert, search, update, list and delete user records.

## How to run

Requires a running MongoDB server on `localhost:27017`.

```
pip install pymongo pandas
python usuario.py
```

## Dependencies

- pymongo
- pandas

## Pyodide-runnable

No — it needs a network connection to a MongoDB database server, which is unavailable in the browser.

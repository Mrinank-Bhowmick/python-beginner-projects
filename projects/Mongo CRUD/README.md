# Mongo CRUD

A small example of create/read/update/delete operations against a MongoDB database using `pymongo`. `conexao.py` opens the database connection and `usuario.py` defines a `Usuario` class with methods to insert, search, update, list and delete user records.

## Example

```python
# Insert a new user
user = Usuario("Alice", "12345", 30, 1.65)
user.inserir_um_registro()

# List all users
user.listar_registros()
# ======= Listagem de usuários =======
#     nome    cpf  idade  altura
# 0  Alice  12345     30    1.65

# Update a field
user = Usuario(nome="Alice Updated", idade=31)
user.alterar_registro("12345")

# Delete a user
user.deletar_registro("12345")
```

## How to run on localhost

Requires a running MongoDB server on `localhost:27017`.

```
pip install pymongo pandas
python usuario.py
```

## Dependencies

- pymongo
- pandas

import MySQLdb

DB = ""
HOST = "localhost"
USER = "root"
PASSWORD = ""
PORT = 3306

class DataBase:

    def convert_dict_to_sql(self, table_to_update, data: dict) -> str:
        sql = f"UPDATE {table_to_update} SET"
        values = []

        for key, value in data.items():
            if not str(value)[0].isdigit():
                values.append(f" {key} = '{value}' ")
            else:
                values.append(f" {key} = {value} ")
        values_columns = ",".join(values)

        sql += str(values_columns)
        sql += f" WHERE id = {data['id']} "

        return sql

    def create_connection_and_cursor(self, db_name: str = "") -> None:
        self.conn = MySQLdb.connect(host=HOST, user=USER, password=PASSWORD, port=PORT, db=db_name)
        self.conn.autocommit(True)
        self.cursor = self.conn.cursor()

    def conn_and_cursor_exist(self) -> bool:
        try:
            self.conn
            self.cursor
            return True
        except AttributeError:
            return False

    def is_database_selected(self) -> bool:
        try:
            self.cursor.execute("CREATE TABLE temp_table (teste varchar(1))")
            self.cursor.execute("DROP TABLE temp_table")
            return True
        except Exception:
            return False

    def change_current_database(self, new_database_name: str) -> None:
        self.conn.select_db(new_database_name)

    def convert_list_to_sql_string(self, data: list) -> str:
        converted_to_sql_data = [f"'{value}'"
                                 if isinstance(value, str) and value.upper() != "DEFAULT" and value.upper() != "NULL"
                                 else str(value)
                                 for value in data]
        string_values = ",".join(converted_to_sql_data)
        return string_values

    def insert_data(self, table_to_insert: str, data: list) -> bool:
        if not self.conn_and_cursor_exist():
            raise Exception("Connetion or cursor is not defined!")
        if not self.is_database_selected():
            raise Exception("Database is not selected!")
        if not isinstance(data, list):
            raise TypeError("Data is not a list!")

        string_values = self.convert_list_to_sql_string(data)
        sql = f"""INSERT INTO {table_to_insert} VALUES ({string_values})"""

        try:
            affected_rows = self.cursor.execute(sql)
            if affected_rows > 0:
                return True
        except:
            return False

        return False

    def delete_data(self, table_to_delete: str, data: int) -> bool:
        if not self.conn_and_cursor_exist():
            raise Exception("Connetion or cursor is not defined!")
        if not self.is_database_selected():
            raise Exception("Database is not selected!")

        sql = f"""DELETE FROM {table_to_delete} WHERE id = {data}"""

        try:
            affected_rows = self.cursor.execute(sql)
            if affected_rows > 0:
                return True
        except:
            return False

        return False

    def select_data(self, table_to_select: str, data: int) -> list:
        if not self.conn_and_cursor_exist():
            raise Exception("Connetion or cursor is not defined!")
        if not self.is_database_selected():
            raise Exception("Database is not selected!")

        sql = f"""SELECT * FROM {table_to_select} WHERE id = {data}"""

        try:
            affected_rows = self.cursor.execute(sql)
            if affected_rows > 0:
                print(list(self.cursor.fetchall()))
                return True
        except:
            return False

        return False

    def update_data(self, table_to_update: str, data: dict):
        if not self.conn_and_cursor_exist():
            raise Exception("Connetion or cursor is not defined!")
        if not self.is_database_selected():
            raise Exception("Database is not selected!")
        if not isinstance(data, dict):
            raise TypeError("Data is not a dict!")

        sql = self.convert_dict_to_sql(table_to_update, data)

        try:
            affected_rows = self.cursor.execute(sql)
            if affected_rows > 0:
                return True
        except:
            return False

        return False



teste = DataBase()
teste.create_connection_and_cursor("aula_bd")
teste.conn_and_cursor_exist()
teste.is_database_selected()
# teste.insert_data("exemplotabela", ["jefferson", "323", 23, 2])
teste.select_data("exemplotabela", 41)
# teste.update_data("exemplotabela", dict(id=1, Nome="bla"))

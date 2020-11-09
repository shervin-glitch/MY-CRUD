from Python.CRUD.connector import connect


class Select():
    def __init__(self, code, name, family, phone):
        self.code = code
        self.name = name
        self.family = family
        self.phone = phone

    def select_data(self):
        try:
            con, cursor = connect().database()
            query = "SELECT * FROM user WHERE phone = %s"%self.phone
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)

        except:
            print("Data Selection Failed")
from Python.CRUD.connector import connect


class Delete():
    def __init__(self, code, name, family, phone):
        self.code = code
        self.name = name
        self.family = family
        self.phone = phone

    def delete_data(self):
        try:
            con, cursor = connect().database()
            query = "DELETE FROM user WHERE code = %s"
            data = (self.code, self.name, self.family, self.phone)
            cursor.execute(query , data)
            con.commit()

        except:
            print("Failed To Delete Data")
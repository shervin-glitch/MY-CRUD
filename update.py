from Python.CRUD.connector import connect


class Update():
    def __init__(self, code, name, family, phone):
        self.code = code
        self.name = name
        self.family = family
        self.phone = phone

    def update_data(self):
        try:
            con, cursor = connect().database()
            query = "UPDATE user SET" + "#Entry Object name" + "=%s WHERE code = %s"
            data = (self.code, self.name, self.family, self.phone)
            cursor.execute(query , data)
            con.commit()

        except:
            print("Failed To Update Data")
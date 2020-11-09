from Python.CRUD.connector import connect

class Create():
    def __init__(self , code , name , family , phone):
        self.code = code
        self.name = name
        self.family = family
        self.phone = phone

    def create_data(self):
        try:
            con , cursor = connect().database()
            query = "INSERT INTO user(code , name , family , phone) VALUES(%s , %s , %s , %s)"
            data = (self.code , self.name , self.family , self.phone)
            cursor.execute(query , data)
            con.commit()
            print("Data Created Succcessfully")

        except:
            print("Data Creation Failed")

code = int(input("Please Enter Your Code :"))
name = input("Please Enter Your Name :")
family = input("Please Enter Your Family :")
phone = int(input("Please Enter Your Phone"))

insert = Create(code , name , family , phone)
insert.create_data()
from pymysql import connect


class Connect():
    def database(self):

        try:
            con=connect(
                host = "127.0.0.1" ,
                user = "Shervin" ,
                password = "password" ,
                db = "db"
            )
            print("Connected Successfully")

        except:
            print("Access Denid")

        finally:
            print("Connected")
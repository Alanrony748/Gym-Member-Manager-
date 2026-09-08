
import mysql.connector
from datetime import datetime

class DbConnect:
    def get_connection(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="alanr.ec2226",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def get(self):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="select * from member"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.connect=super().get_connection()
            self.cursor=self.connect.cursor()
            query="insert into member (name,place,mobile,plan,fee,joined_on_date) values (%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("new member added successfully")
        except Exception as e:
            print(e)

    def retreive(self,id=None):
        try:
            record=self.get_object(id=id)
            if record==None:
                print("member not found")
            else:
                print(record)
        except Exception as e:
            print(e)

    def delete(self,id=None):
        try:
            record = self.get_object(id=id)
            values = (id,)
            if record != None:
                query = "delete from member where id =%s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("member deleted successfully")
            else:
                print("member not found")
        except Exception as e:
            print(e)


    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s,"
                placeholder=placeholder.rstrip(",")
                query=f"update member set {placeholder} where id=%s"
                values=[v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("updation successful")
            else:
                print("member not found")
        except Exception as e:
            print(e)


# connection_instance=DbConnect()
# print(connection_instance.get_connection())

member_instance=GymMemberManager()

# member_instance.post(name="nikheth",place="kakanadu",mobile="523732837838",plan="8 months",fee=8000,joined_on_date=datetime.today())
# member_instance.get()
# member_instance.retreive(id=3)
# member_instance.delete(3)
member_instance.put(id=2,name="diva")
member_instance.get()


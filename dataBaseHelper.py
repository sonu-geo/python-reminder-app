import mysql.connector
import random


class DataBaseHelper:
    def __init__(self):
        self.myDb = mysql.connector.connect(
            host="remotemysql.com",
            user=" 7C1b9IUQMB",
            passwd="4nO2zBohE0",
            database=' 7C1b9IUQMB'
        )

    def createReminder(self, description, time):
        myCursor = self.myDb.cursor()
        id = random.randint(0, 10000)
        sql = "INSERT INTO reminder values("+str(id)+",'"+description+"','"+str(time)+"')"
        try:
            myCursor.execute(sql)
            self.myDb.commit()
            return {'status':'success'}
        except Exception as e:
            return {'status': 'failed','message':e}
    def selectReminder(self):
        myCursor = self.myDb.cursor()
        sql ='SELECT * from reminder'
        myCursor.execute(sql)
        result = myCursor.fetchall()
        return result
    def updateReminder(self,id,time):
        myCursor = self.myDb.cursor()
        sql = "UPDATE reminder SET dateTime='"+str(time)+"' WHERE id="+str(id)
        try:
            myCursor.execute(sql)
            self.myDb.commit()
            return {'status':'success'}
        except Exception as e:
            return {'status': 'failed','message':e}
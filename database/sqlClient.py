import mysql.connector
import time
import datetime
class Database:
    def __init__(self):
        super().__init__()
        self.host="localhost"
        self.user="root"
        self.password="czd888"
        self.database="livetalking"

    def connect(self):
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS livetalking")
        self.mycursor.execute("USE livetalking")
    def insert_data(self, data):
        nowtime = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        return 'ok'
    def select_data(self, data):
        return 'ok'
    def update_data(self, data):
        return 'ok'
    def delete_data(self, data):
        return 'ok'
    def close(self):
        self.mycursor.close()
        self.mydb.close()


if __name__ == '__main__':
    database=Database()
    database.connect()
    database.close()
    print(datetime.datetime)
    # db = Database()
    # db.connect()

import mysql.connector

conn = mysql.connector.connect(username='root', password='root',host='localhost',database='Mysql',port=3306)
cursor = conn.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

print(data)

conn.close()
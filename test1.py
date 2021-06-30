#!C:\ProgramData\Miniconda3\python.exe
# Importing the 'cgi' module
import time
import datetime
import mysql.connector
import cgi

print("Content-type: text/html\r\n\r\n")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mini_proj"
)

mycursor = mydb.cursor()

pro = 'tea'
para= (pro,)
que="SELECT pro_id FROM menu WHERE pro_name=%s"
mycursor.execute(que,para)
result_list = [row[0] for row in mycursor.fetchall()]
if result_list:
    print(result_list)
else:
    print("unsuccess")

ts = time.time()
print(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
#!C:\ProgramData\Miniconda3\python.exe

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

mycursor.execute("SELECT * FROM menu")
myresult = mycursor.fetchall()

print ("<meta name=viewport' content='width=device-width, initial-scale=1'><link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>")
print ("<br><br>")
print ("<form action='process_bill.py' method='get' align='center'>")
print ("<table class='w3-table' border='1'>")
print ("<tr><th>Product id</th><th>product name</th><th>ptoduct price</th></tr>")
for x in myresult:
    print("<tr><td>",x[0],"</td><td><input type='checkbox' name='product[]' id='product' value='",x[1],"'>",x[1],"</td><td>",x[2],"</td></tr>")
print ("</table><input type='submit' value-'next' align='center' value='Next'/></form>")

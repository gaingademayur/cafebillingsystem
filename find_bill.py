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


que = "SELECT bill_no FROM bills ORDER BY bill_no DESC"
mycursor.execute(que)
id_result = [row[0] for row in mycursor.fetchall()]
if id_result==[]:
    print("<h3 align = 'center'>You have not created any bills yet.<br><a href='/mini_propy/index.py'>Click here</a> to create a new one.</h3>")
else:
  print("""<h3><form action='display_found_bill.py' method='get'><br><br>
    Enter the bill no. you want to search:<br>
    <input type = 'text' name = 'bill_no' id='bill_no' maxlength='4' placeholder='bill no.'/>
    <input type = 'submit' value='Search'/>
    </form></h3>""")

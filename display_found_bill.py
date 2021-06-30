#!C:\ProgramData\Miniconda3\python.exe

import mysql.connector
import cgi
import time
import datetime
import ast
print("Content-type: text/html\r\n\r\n")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mini_proj"
)

mycursor = mydb.cursor()
form = cgi.FieldStorage()
bill_no = form.getvalue('bill_no')
que = "SELECT bill_no FROM bills ORDER BY bill_no DESC"
mycursor.execute(que)
id_result = [row[0] for row in mycursor.fetchall()]
print("<br>")
if id_result[0]<int(bill_no):
    print("<h4 align='center'>Sorry! Bill not found</h4>")
    print("<h3 align = 'center'><br><a href='/mini_propy/index.py'>Create a new bill here</a></h3>")

else:
    que = "SELECT * FROM bills WHERE bill_no='%s'"%bill_no
    mycursor.execute(que)
    result = mycursor.fetchall()
    datadic = ast.literal_eval(result[0][1])
    bill_date = result[0][2]
    quantity = datadic['quantity']
    product = datadic['product']
    ids = datadic['ids']
    prices = datadic['prices']
    total = 0
    i=0
    print("<table class='w3-table' border='1' align='center'>")
    print("<tr><th colspan='5'><h2 align='center'>Your Bill</h2></th></tr>")
    print("<tr><th colspan='4'></th><td><h5>Bill no.: ",bill_no,"<br>Bill date and time</h5>",bill_date,"</td></tr>")
    print("<tr><th colspan='5'><h2 align='center'></h2></th></tr>")
    print("<tr><th>Product id</th><th>product name</th><th>product price</th><th>Quantity</th><th>Product total</th></tr>")
    for pro in product:
        pro_total = float(prices[i])*int(quantity[i])
        total = total + pro_total
        print("<tr><td>",ids[i],"</td><td>",pro,"</td><td>",prices[i],"</td><td>",quantity[i],"</td><td>",pro_total,"</td></tr>")
        i = i+1
    print("<tr><td colspan='4'>Total</td><td>",total,"</td></tr>")
    print("</table>")

    print("<br>")
    print("<br>")
    print("<br>")
    print("<br>")
    print("<h3 align = 'center'><br><a href='/mini_propy/index.py'>Create a new bill here</a></h3>")

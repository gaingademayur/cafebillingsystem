#!C:\ProgramData\Miniconda3\python.exe

import mysql.connector
import cgi
import string
print("Content-type: text/html\r\n\r\n")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mini_proj"
)

mycursor = mydb.cursor()

form = cgi.FieldStorage()
product = form.getvalue('product[]')
i = 0
prices = []
ids = []
pro2=[]
print("<form action='display_bill.py' method='get' align = 'center'>")
print("<table class='w3-table' border='1' align='center'>")
print("<tr><th>product id</th><th>product name</th><th> product price</th><th>Quantity</th></tr>")


for pro in product:
    para = (str(pro))
    que = "SELECT pro_id FROM menu WHERE pro_name='%s'"%para.strip()
    mycursor.execute(que)
    id_result = [row[0] f   or row in mycursor.fetchall()]
    ids.append(id_result[0])

    que = "SELECT pro_price FROM menu WHERE pro_name='%s'"%para.strip()
    mycursor.execute(que)
    pri_result = [row[0] for row in mycursor.fetchall()]
    prices.append(pri_result[0])
    print("<tr><td>",id_result[0],"</td><td>",pro,"</td><td>",pri_result[0],"</td><td><input type='text' name='quantity[]' id='quantity' placeholder='Enter the Quantity'/></td></tr>")
    print("<input type ='hidden' name='prices[]' id='prices' value='%s'/>" % pri_result[0])
    print("<input type ='hidden' name='ids[]' id='ids' value='%s'/>" % id_result[0])


print("</table>")
#print("<input type ='hidden' name='product' id='product' value='%s'/>"%product)
#print("<input type ='hidden' name='prices' id='prices' value='%s'/>"%prices)
#print("<input type ='hidden' name='ids' id='ids' value='%s'/>"%ids)
print("<input type = 'submit'/>")
print("</form>")
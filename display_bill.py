#!C:\ProgramData\Miniconda3\python.exe
import time
import datetime
import mysql.connector
import cgi
print("Content-type: text/html\r\n\r\n")
print("""
<script>
  function printDiv(divName){
    var printContents = document.getElementById(divName).innerHTML;
    var originalContents = document.body.innerHTML;
    document.body.innerHTML = printContents;
    window.print();
    document.body.innerHTML = originalContents;
  }
</script>
""")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mini_proj"
)
mycursor = mydb.cursor()

form = cgi.FieldStorage()
prices = form.getvalue('prices[]')
ids = form.getvalue('ids[]')
quantity = form.getvalue('quantity[]')



product=[]
for prid in ids:
    que = "SELECT pro_name FROM menu WHERE pro_id='%s'" % prid
    mycursor.execute(que)
    id_result = [row[0] for row in mycursor.fetchall()]
    product.append(id_result[0])



que = "SELECT bill_no FROM bills ORDER BY bill_no DESC"
mycursor.execute(que)
id_result = [row[0] for row in mycursor.fetchall()]
if id_result==[]:
    bill_no = 1
else:
    bill_no = 1+int(id_result[0])

total = 0
ts = time.time()
my_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
i = 0
print("\n\n\n\n\n\n\n\n")

print("<br><br><br><br>")
print("<div align='center'>")
print("<div id='bill_tab' align='center'>")
print("<table class='w3-table' border='1' align='center' >")
print("<tr><th colspan='5'><h2 align='center'>Your Bill</h2></th></tr>")
print("<tr><th colspan='4'></th><td><h5>Bill no.: ",bill_no,"<br>Bill date and time</h5>",my_date,"</td></tr>")
print("<tr><th colspan='5'><h2 align='center'></h2></th></tr>")
print("<tr><th>Product id</th><th>product name</th><th>ptoduct price</th><th>Quantity</th><th>Product total</th></tr>")

for pro in product:
  pro_total = float(prices[i])*int(quantity[i])
  total = total + pro_total
  print("<tr><td>",ids[i],"</td><td>",pro,"</td><td>",prices[i],"</td><td>",quantity[i],"</td><td>",pro_total,"</td></tr>")
  i = i+1

print("<tr><td colspan='4'>Total</td><td>",total,"</td></tr>")
print("</table>")
print("</div>")
print("<br><br>")
print("<button onclick=\"printDiv('bill_tab')\" align='center'>Print bill</button>")
print("</div>")
print("<br><br>")

print("<h3 align = 'center'><br><a href='/mini_propy/index.py'>Create a new bill here</a></h3>")

datadic = {}
datadic["quantity"] = quantity
datadic["product"] = product
datadic["ids"] = ids
datadic["prices"] = prices

que = "INSERT INTO bills (bill_no, bill_data, bill_date, bill_total) VALUES(\"%s\",\"%s\",\"%s\",\"%s\")" % (bill_no, datadic, my_date, total)
mycursor.execute(que)
mydb.commit()

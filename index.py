#!C:\ProgramData\Miniconda3\python.exe

import mysql.connector
import cgi
print("Content-type: text/html\r\n\r\n")
print('''<html>
<head>
<script>
</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body>
  <br><br>
<form action="create_bill.py" method="get" align='center'>
<input type="submit" value="create bill" class=""/>
</form><br>
<form action="find_bill.py" method="get" align='center'>
<input type="submit" value="find bill"/>
</form>
</body>
</html>''')
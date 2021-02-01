import mysql.connector

mydb = mysql.connector.connect(
  host="mysql-19580-0.cloudclusters.net",
  user="vijay",
  password="Vijay@83",
    port="19588",
database="CancerPatientDatabase"
)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
  host="seitux2.adfa.unsw.edu.au",
  user="z5317512",
  password="mysqlpass",
  database="z5317512",
  ssl_disabled=True,
)

mycursor = mydb.cursor()

# sql = "INSERT into users (ID, fName, lName, email, password, type) VALUES (%s, %s, %s, %s, %s, %s)"
# val = ("1115", "Tyson", "Lovett", "tysonlovett@hotmail.com", "password", "A")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
for x in myresult:
  print("ID is:", x[0])
  print("Name is:", x[1], x[2])
  print("User ID is:", x[3])
  print("Password is:", x[4])
  print("Account type is:", x[5])


if __name__ == '__main__':
    print("Hi")

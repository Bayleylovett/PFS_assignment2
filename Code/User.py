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

def searchID():
    searchItemID = int(input("Insert the ID of the item you would like to find: "))
    mycursor.execute("""SELECT DISTINCT a.iName, a.category, a.company, a.price, b.quantity, c.wName FROM items a, warehouseStock b, warehouses c WHERE a.ID='%s' AND b.iID=a.ID AND c.ID=b.wID""" % searchItemID)
    myresult = mycursor.fetchall()
    for x in myresult:
      print("Item Name:", x[0], "Category:", x[1], "Company:", x[2], "Price:", x[3], "Quantity:", x[4], "Warehouse Name:", x[5])




def searchCompany():
    searchItemCompany = input("Insert the company of the item you would like to find: ")
    mycursor.execute("""SELECT DISTINCT a.iName, a.category, a.company, a.price, b.quantity, c.wName FROM items a, warehouseStock b, warehouses c WHERE a.company='%s' AND b.iID=a.ID AND c.ID=b.wID""" % searchItemCompany)
    myresult = mycursor.fetchall()
    for x in myresult:
      print("Item Name:", x[0], "Category:", x[1], "Company:", x[2], "Price:", x[3], "Quantity:", x[4], "Warehouse Name:", x[5])

# def searchCategory():

# def moveItems():

# def destroyItems():



if __name__ == '__main__':
    # searchID()
    searchCompany()

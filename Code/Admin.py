import mysql.connector
from mysql.connector import Error
import random
import hashlib
import secrets
mydb = mysql.connector.connect(
  host="seitux2.adfa.unsw.edu.au",
  user="z5317512",
  password="mysqlpass",
  database="z5317512",
  ssl_disabled=True,
)
mycursor = mydb.cursor()
#creates the salt needed to hash the password
#NOTE: this is also stored in the users row of data
SALT = secrets.token_bytes(32)

def adminSwitch():
    i = None
    while i != '0':
        i = input('\nWhat would you like to do\n'
                  '0: Logout\n'
                  '1: Create a user\n'
                  '2: Assign a user to a warehouse\n'
                  '3: Create an item\n'
                  '4: Create a warehouse\n'
                  '5: Add stock to a warehouse\n'
                  '6: List warehouses and managers\n'
                  '7: List users\n'
                  '8: List items\n'
                  '9: Check Stock\n'
                  'Please enter your choice: ')

        if i == '0':
            print('\nGood bye')
        elif i == '1':
            createUser()
        elif i == '2':
            assignUser()
        elif i == '3':
            createItem()
        elif i == '4':
            createWarehouse()
        elif i == '5':
            addStock()
        elif i == '6':
            listWarehouses()
        elif i == '7':
            listUsers()
        elif i == '8':
            listItems()
        elif i == '9':
            checkStock()
        else:
            print('\nIncorrect Input, Try Again')

def createUser():
    createUserfName = input("Enter User First Name:")
    createUserlName = input("Enter User Last Name:")
    createUserUserID = input("Enter User Unique ID:")
    createUserPassword = input("Enter User Password:")
    #creates the hashed password to store in the database
    password = hashlib.pbkdf2_hmac('sha256', createUserPassword.encode(), SALT, 4096)
    #print("Inserting password: " + password + "\n and program SALT: %s" % (password, SALT))
    id=random.randint(1000, 9999)
    mycursor.execute("""SELECT ID FROM users WHERE ID='%s'""" % id)
    myresult = mycursor.fetchall()
    while not mycursor.rowcount==0:
        id=random.randint(1000, 9999)
        mycursor.execute("""SELECT ID FROM users WHERE ID='%s'""" % id)
        myresult = mycursor.fetchall()
    mycursor.execute("""INSERT INTO users (ID, fName, lName, userID, type, password, salt) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (id, createUserfName, createUserlName, createUserUserID, "U", password.hex(), SALT.hex()))
    mydb.commit()

def assignUser():
    assignUserID = input("Enter User ID:")
    assignWarehouseID = input("Enter Warehouse ID:")
    id=random.randint(10000, 99999)
    mycursor.execute("""SELECT ID FROM warehouseManagers WHERE ID='%s'""" % id)
    myresult = mycursor.fetchall()
    while not mycursor.rowcount==0:
        id=random.randint(10000, 99999)
        mycursor.execute("""SELECT ID FROM warehouseManagers WHERE ID='%s'""" % id)
        myresult = mycursor.fetchall()
    mycursor.execute("""SELECT * FROM warehouseManagers WHERE mID='%s' AND wID='%s'""" % (assignUserID, assignWarehouseID))
    myresult = mycursor.fetchall()
    for x in myresult:
        print("User is already a Manager of this warehouse.")
    else:
        mycursor.execute("""INSERT INTO warehouseManagers (ID, mID, wID) VALUES ('%s', '%s', '%s')""" % (id, assignUserID, assignWarehouseID))
        mydb.commit()

def createItem():
    createItemiName = input("Enter Item Name:")
    createItemCategory = input("Enter Item Category:")
    createItemoLocation = input("Enter Item Location:")
    createItemCompany = input("Enter Item Company:")
    createItemPrice = float(input("Enter Item Price:"))
    id=random.randint(1000000000, 9999999999)
    mycursor.execute("""SELECT ID FROM items WHERE ID='%s'""" % id)
    myresult = mycursor.fetchall()
    while not mycursor.rowcount==0:
        id=random.randint(1000000000, 9999999999)
        mycursor.execute("""SELECT ID FROM items WHERE ID='%s'""" % id)
        myresult = mycursor.fetchall()
    mycursor.execute("""SELECT * FROM items WHERE iName='%s' AND category='%s'""" % (createItemiName, createItemCategory))
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Item name and category already exists.")
    else:
        mycursor.execute("""INSERT INTO items (ID, iName, category, oLocation, company, price) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')""" % (id, createItemiName, createItemCategory, createItemoLocation, createItemCompany, createItemPrice))
        mydb.commit()

def createWarehouse():
    createWarehousewName = input("Enter Warehouse Name:")
    createWarehouseState = input("Enter Warehouse State:")
    createWarehouseCountry = input("Enter Warehouse Country:")
    id=random.randint(100, 999)
    mycursor.execute("""SELECT ID FROM warehouses WHERE ID='%s'""" % id)
    myresult = mycursor.fetchall()
    while not mycursor.rowcount==0:
        id=random.randint(100, 999)
        mycursor.execute("""SELECT ID FROM warehouses WHERE ID='%s'""" % id)
        myresult = mycursor.fetchall()
    mycursor.execute("""SELECT * FROM warehouses WHERE wName='%s'""" % createWarehousewName)
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Warehouse name already exists.")
    else:
        mycursor.execute("""INSERT INTO warehouses (ID, wName, state, country) VALUES ('%s', '%s', '%s', '%s')""" % (id, createWarehousewName, createWarehouseState, createWarehouseCountry))
        mydb.commit()

def addStock():
    addStockWarehouseID = input("Enter Warehouse ID to add stock:")
    addStockItemID = input("Enter Item ID:")
    addStockQuantity = int(input("Enter Quantity:"))
    id=random.randint(100000, 999999)
    mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
    myresult = mycursor.fetchall()
    while not mycursor.rowcount==0:
        id=random.randint(100000, 999999)
        mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
        myresult = mycursor.fetchall()
    mycursor.execute("""SELECT * FROM warehouseStock WHERE wID='%s' AND iID='%s'""" % (addStockWarehouseID, addStockItemID))
    myresult = mycursor.fetchall()
    for x in myresult:
        id=id

    if mycursor.rowcount>0:
        mycursor.execute("""UPDATE warehouseStock SET quantity='%s' WHERE wID='%s' AND iID='%s'""" % (x[3]+addStockQuantity, addStockWarehouseID, addStockItemID))
        mydb.commit()
    else:
        mycursor.execute("""INSERT INTO warehouseStock (ID, wID, iID, quantity) VALUES ('%s', '%s', '%s', '%s')""" % (id, addStockWarehouseID, addStockItemID, addStockQuantity))
        mydb.commit()

def listWarehouses():
    mycursor.execute("""SELECT a.ID, a.wName, a.state, a.country, b.fName, b.lName FROM warehouses a, users b, warehouseManagers c WHERE c.wID=a.ID AND b.ID=c.mID""")
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Warehouse ID:",x[0],"Warehouse Name:",x[1],"Warehouse Location:",x[2], x[3],"Warehouse Manager:",x[4], x[5])

def listUsers():
    mycursor.execute("""SELECT ID, fName, lName, userID, type FROM users""")
    myresult = mycursor.fetchall()
    for x in myresult:
        print("User ID:",x[0],"User Name:",x[1], x[2],"User Unique ID:",x[3],"User Type:",x[4])

def listItems():
    mycursor.execute("""SELECT * FROM items""")
    myresult = mycursor.fetchall()
    for x in myresult:
        print("ID:",x[0],"Name:",x[1],"Category:",x[2],"Location:",x[3],"Company:",x[4],"Price:",x[5])

def checkStock():
    mycursor.execute("""SELECT DISTINCT b.iName, b.category, a.quantity, c.wName FROM warehouseStock a, items b, warehouses c WHERE a.wID=c.ID AND a.iID=b.ID""")
    myresult = mycursor.fetchall()
    for x in myresult:
      print("Item Name:",x[0],"Category:",x[1],"Quantity:",x[2],"Warehouse Name:",x[3])

if __name__ == '__main__':
    # print("Admin")
    adminSwitch()

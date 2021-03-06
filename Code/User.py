# Prebuilt functions to import for program
import mysql.connector
from mysql.connector import Error
import random
# Database connection
mydb = mysql.connector.connect(
  host="seitux2.adfa.unsw.edu.au",
  user="z5317512",
  password="mysqlpass",
  database="z5317512",
  ssl_disabled=True,
)
mycursor = mydb.cursor()

# Searches for specific items based off ID
def searchID():
    searchItemID = int(input("Insert the ID of the item you would like to find: "))
    mycursor.execute("""SELECT DISTINCT a.iName, a.category, a.company, a.price, b.quantity, c.wName FROM items a, warehouseStock b, warehouses c WHERE a.ID='%s' AND b.iID=a.ID AND c.ID=b.wID""" % searchItemID)
    myresult = mycursor.fetchall()
    for x in myresult:
      print("Item Name:", x[0], "Category:", x[1], "Company:", x[2], "Price:", x[3], "Quantity:", x[4], "Warehouse Name:", x[5])

# Searches for specfic items based off company
def searchCompany():
    searchItemCompany = input("Insert the company of the item you would like to find: ")
    mycursor.execute("""SELECT DISTINCT a.iName, a.category, a.company, a.price, b.quantity, c.wName FROM items a, warehouseStock b, warehouses c WHERE a.company='%s' AND b.iID=a.ID AND c.ID=b.wID""" % searchItemCompany)
    myresult = mycursor.fetchall()
    for x in myresult:
      print("Item Name:", x[0], "Category:", x[1], "Company:", x[2], "Price:", x[3], "Quantity:", x[4], "Warehouse Name:", x[5])

# Searches for specific items based off category
def searchCategory():
    searchItemCategory = input("Insert the category of the item you would like to find: ")
    mycursor.execute("""SELECT DISTINCT a.iName, a.category, a.company, a.price, b.quantity, c.wName FROM items a, warehouseStock b, warehouses c WHERE a.category='%s' AND b.iID=a.ID AND c.ID=b.wID""" % searchItemCategory)
    myresult = mycursor.fetchall()
    for x in myresult:
      print("Item Name:", x[0], "Category:", x[1], "Company:", x[2], "Price:", x[3], "Quantity:", x[4], "Warehouse Name:", x[5])

# Moves an item from one warehouse to another if the user is the manager of that warehouse
def moveItems(moveItemsUserID):
    # User input
    moveItemsItem = int(input("Insert the ID of the item you would like to move: "))
    moveItemsWarehousePRE = int(input("Insert the ID of the warehouse you would like the items to move from: "))
    moveItemsWarehousePOST = int(input("Insert the ID of the warehouse you would like the items to move to: "))
    moveItemsQuantity = int(input("Insert the quantity of items you would like to move: "))
    # Checks to see if user is a manager and the quanitity to see if it exists
    mycursor.execute("""SELECT DISTINCT b.quantity FROM warehouseManagers a, warehouseStock b WHERE a.mID='%s' AND a.wID='%s' AND b.iID='%s' AND b.wID=a.wID""" % (moveItemsUserID, moveItemsWarehousePRE, moveItemsItem))
    myresult = mycursor.fetchall()
    if mycursor.rowcount==0:
        print("Invalid inputs or you cannot access this warehouse.")
    else:
        # Different methods based on if it exists or not and how much the quantity is to configure specific mysql statements
        for x in myresult:
            if int(x[0])>moveItemsQuantity:
                mycursor.execute("""SELECT quantity FROM warehouseStock WHERE iID='%s' AND wID='%s'""" % (moveItemsItem, moveItemsWarehousePOST))
                myresult = mycursor.fetchall()
                # Error checking if quantity exists
                for y in myresult:
                    id=000000
                if mycursor.rowcount==0:
                    # Randomly generating ID and checking if it already exists
                    id=random.randint(100000, 999999)
                    mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
                    myresult = mycursor.fetchall()
                    while not mycursor.rowcount==0:
                        id=random.randint(100000, 999999)
                        mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
                        myresult = mycursor.fetchall()
                    # Adding new stock to warehouse and removing stock from current warehouse
                    mycursor.execute("""INSERT INTO warehouseStock (ID, wID, iID, quantity) VALUES ('%s', '%s', '%s', '%s')""" % (id, moveItemsWarehousePOST, moveItemsItem, moveItemsQuantity))
                    mydb.commit()
                    mycursor.execute("""UPDATE warehouseStock SET quantity='%s' WHERE wID='%s' AND iID='%s'""" % (x[0]-moveItemsQuantity, moveItemsWarehousePRE, moveItemsItem))
                    mydb.commit()
                else:
                    id=random.randint(100000, 999999)
                    mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
                    myresult = mycursor.fetchall()
                    while not mycursor.rowcount==0:
                        id=random.randint(100000, 999999)
                        mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
                        myresult = mycursor.fetchall()
                    mycursor.execute("""UPDATE warehouseStock SET quantity='%s' WHERE wID='%s' AND iID='%s'""" % (y[0]+moveItemsQuantity, moveItemsWarehousePOST, moveItemsItem))
                    mydb.commit()
                    mycursor.execute("""UPDATE warehouseStock SET quantity='%s' WHERE wID='%s' AND iID='%s'""" % (x[0]-moveItemsQuantity, moveItemsWarehousePRE, moveItemsItem))
                    mydb.commit()
            elif int(x[0])==moveItemsQuantity:
                mycursor.execute("""SELECT quantity FROM warehouseStock WHERE iID='%s' AND wID='%s'""" % (moveItemsItem, moveItemsWarehousePOST))
                myresult = mycursor.fetchall()
                for y in myresult:
                    id=000000
                if mycursor.rowcount==0:
                    id=random.randint(100000, 999999)
                    mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
                    myresult = mycursor.fetchall()
                    while not mycursor.rowcount==0:
                        id=random.randint(100000, 999999)
                        mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
                        myresult = mycursor.fetchall()
                    mycursor.execute("""INSERT INTO warehouseStock (ID, wID, iID, quantity) VALUES ('%s', '%s', '%s', '%s')""" % (id, moveItemsWarehousePOST, moveItemsItem, moveItemsQuantity))
                    mydb.commit()
                    mycursor.execute("""DELETE FROM warehouseStock WHERE wID='%s' AND iID='%s'""" % (moveItemsWarehousePRE, moveItemsItem))
                    mydb.commit()
                else:
                    id=random.randint(100000, 999999)
                    mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
                    myresult = mycursor.fetchall()
                    while not mycursor.rowcount==0:
                        id=random.randint(100000, 999999)
                        mycursor.execute("""SELECT ID FROM warehouseStock WHERE ID='%s'""" % id)
                        myresult = mycursor.fetchall()
                    mycursor.execute("""UPDATE warehouseStock SET quantity='%s' WHERE wID='%s' AND iID='%s'""" % (y[0]+moveItemsQuantity, moveItemsWarehousePOST, moveItemsItem))
                    mydb.commit()
                    mycursor.execute("""DELETE FROM warehouseStock WHERE wID='%s' AND iID='%s'""" % (moveItemsWarehousePRE, moveItemsItem))
                    mydb.commit()
            else:
                print("Quantity to large.")

# Destroys items in warehouse the user manages
def destroyItems(destroyItemsUserID):
    # User inputs
    destroyItemsItem = int(input("Insert the ID of the item you would like to delete: "))
    destroyItemsWarehouse = int(input("Insert the ID of the warehouse you would like to delete items from: "))
    destroyItemsQuantity = int(input("Insert the quantity of items you would like to delete: "))
    # Checks if quantity exists
    mycursor.execute("""SELECT DISTINCT b.quantity FROM warehouseManagers a, warehouseStock b WHERE a.mID='%s' AND a.wID='%s' AND b.iID='%s' AND b.wID=a.wID""" % (destroyItemsUserID, destroyItemsWarehouse, destroyItemsItem))
    myresult = mycursor.fetchall()
    if mycursor.rowcount==0:
        print("Invalid inputs or you cannot access this warehouse.")
    else:
        # Depending on how much stock there is and the user input it configures the mysql statements
        for x in myresult:
            if int(x[0])>destroyItemsQuantity:
                mycursor.execute("""UPDATE warehouseStock SET quantity='%s' WHERE wID='%s' AND iID='%s'""" % (x[0]-destroyItemsQuantity, destroyItemsWarehouse, destroyItemsItem))
                mydb.commit()
            elif int(x[0])==destroyItemsQuantity:
                mycursor.execute("""DELETE FROM warehouseStock WHERE wID='%s' AND iID='%s'""" % (destroyItemsWarehouse, destroyItemsItem))
                mydb.commit()
            else:
                print("Quantity to large.")

# Lists all warehouses
def listWarehouses():
    mycursor.execute("""SELECT * FROM warehouses""")
    myresult = mycursor.fetchall()
    rows=mycursor.rowcount
    rowsTemp = 0
    mycursor.execute("""SELECT a.ID, a.wName, a.state, a.country, b.fName, b.lName FROM warehouses a, users b, warehouseManagers c WHERE c.wID=a.ID AND b.ID=c.mID""")
    myresult = mycursor.fetchall()
    for x in myresult:
        print("Warehouse ID:",x[0],"Warehouse Name:",x[1],"Warehouse Location:",x[2], x[3],"Warehouse Manager:",x[4], x[5])
        rowsTemp += 1
    if (rowsTemp!=rows):
        print("Warehouses have not all been assigned a Manager, listing all warehouses.")
        mycursor.execute("""SELECT * FROM warehouses""")
        myresult = mycursor.fetchall()
        for x in myresult:
            print("Warehouse ID:",x[0],"Warehouse Name:",x[1],"Warehouse Location:",x[2], x[3])

# Switch statement to run specific functions based off user input
def userSwitch(userIdentification):
    i = None
    while i != '0':
        i = input('\nWhat would you like to do\n'
                  '0: Logout\n'
                  '1: Search for items using an ID\n'
                  '2: Search for items using Company\n'
                  '3: Search for item using a Category\n'
                  '4: Move an item between a warehouse\n'
                  '5: Delete an item from the database\n'
                  '6: List all the warehouses\n'
                  'Please enter your choice: ')

        if i == '0':
            print('\nGood bye')
        elif i == '1':
            searchID()
        elif i == '2':
            searchCompany()
        elif i == '3':
            searchCategory()
        elif i == '4':
            moveItems(int(userIdentification))
        elif i == '5':
            destroyItems(int(userIdentification))
        elif i == '6':
            listWarehouses()
        else:
            print('\nIncorrect Input, Try Again')

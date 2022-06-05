import mysql.connector
from mysql.connector import Error
from User import userSwitch
from Admin import adminSwitch


userType = None

mydb = mysql.connector.connect(
  host="seitux2.adfa.unsw.edu.au",
  user="z5317512",
  password="mysqlpass",
  database="z5317512",
  ssl_disabled=True,
)

mycursor = mydb.cursor()

def login():
    loggedIn = 0
    while(loggedIn == 0):
        try:
            userID = int(input('\nEnter your user identification number:'))
        except:
            print('\nIncorrect Input!')
            userID = None

        password = input('\nEnter your password:')

        #connect to db
        sql = "SELECT * FROM users WHERE userID = %s AND password = %s;"
        val = (userID, password)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        for x in myresult:
            global userType
            userType = x[5]
        if(userType == 'A' or userType == 'U'):
            loggedIn = 1
        else:
            print('\nIncorrect Login')

#Switch statement based on user permissions
def switch():

    while userType != '0':
        if userType == '0':
               print('\nGood Bye')
        elif userType == 'U':
                userSwitch()
        elif userType == 'A':
            adminSwitch()
        else:
            print('\nGood Bye')
            break
    if userType == '0':
        print('\nGood Bye')


if __name__ == '__main__':
    print("Hi")
    login()
    switch()

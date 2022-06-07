import secrets
import mysql.connector
from mysql.connector import Error
import ast
import hashlib
from User import userSwitch
from Admin import adminSwitch


userType = None
userID = None
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
        global userID
        try:
            userID = int(input('\nEnter your user identification number:'))
        except:
            print('\nIncorrect Input!')
            userID = None

        password = input('\nEnter your password:')
        #gets the stored password and SALT from the users data in the users table
        sqlstmt = "SELECT password, salt FROM users WHERE userID = %s;"
        mycursor.execute(sqlstmt, userID)
        saltAndKey = mycursor.fetchall()
        hash_User_password_Verify = saltAndKey[0]
        SALT = saltAndKey[1]

        #uses the stored SALT to generate a hash from the inputted password
        hash_User_password = hashlib.pbkdf2_hmac('sha256', password.encode(), SALT, 4096)

        #compares the stored hashed value to the inputted hash value
        if secrets.compare_digest(hash_User_password, hash_User_password_Verify):
            print("Password is good continuing log in")
        else:
            print("Password is incorrect, terminating log in attempt")

        #connect to db
        #passing the values to the sql statement as variables protects against sql injection
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
    inputVar = None
    while inputVar != '0':
        inputVar = input('\nIf you would like to quit press 0.\n'
                  'If not hit enter: ')
        if inputVar == '0':
            print('\nGood Bye')
            break
        elif userType == 'U':
            userSwitch(userID)
        elif userType == 'A':
            adminSwitch()
        else:
            print('\nGood Bye')
            break



if __name__ == '__main__':
    print("Hi")
    login()
    switch()

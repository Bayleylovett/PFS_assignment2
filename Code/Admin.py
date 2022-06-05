

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
        else:
            print('\nIncorrect Input, Try Again')

def createUser():
    print('\nCreate User')

def assignUser():
    print('\nCreate User')


def createItem():
    print('\nCreate User')


def createWarehouse():
    print('\nCreate User')


def addStock():
    print('\nCreate User')



if __name__ == '__main__':
    print("Admin")



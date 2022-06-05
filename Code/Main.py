from User import userSwitch
from Admin import adminSwitch

global type



def login():
    userID = input('\nEnter your user identification number:')
    password = input('\nEnter your password:')

    #insert select satement and then get type



#Switch statement based on user permissions
def switch():
    while type != '0':
        if type == '0':
               print('\nGood Bye')
        elif type == 'user':
                userSwitch()
        elif type == 'admin':
            adminSwitch()

    if type == '0':
        print('\nGood Bye')

if __name__ == '__main__':
    login()
    switch()



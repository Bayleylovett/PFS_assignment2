def userSwitch():
    i = 10
    while i != '0':
        i = input('\nWhat would you like to do\n'
                      '0: Break\n'
                      '1: Create a list\n'
                      '2: Print the list\n'
                      '3: Find a movie\n'
                      '4: Rate a movie\n'
                      '5: Order the movies based on rating\n'
                      'Please enter your choice: ')

        if i == '0':
            print('\nGood bye')
        elif i == '1':

        elif i == '2':

        elif i == '3':

        elif i == '4':
            try:
                rateMovie(input('\nEnter the movie you would like to rate:'), int(input('\nEnter the rating out of 1-10: ')))
            except:
                print('Incorrect input entered')
        elif i == '5':
            orderMovies()
        else:
            print('\nEnter a value between 0-5')


if __name__ == '__main__':
    print("Hi")



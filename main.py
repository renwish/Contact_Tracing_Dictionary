#display menu
print("Menu:\n 1.) Add an item\n 2.) Search\n 3.) Exit (Y/n)\n")

#select item in menu
option = input("What do you want to do? (1-3): ")

agedict = {}
regdict = {}
citydict = {}
numdict = {}
emaildict = {}
testdict = {}

#perform option
#1. ask data for contact tracing
while option not in ['1','2','3']:
    print('ERROR! select a number from 1-3')
    option = input("What do you want to do? (1-3): ")

while option in ['1','2','3']:
    if option == '1':
        name = input('Name: ')
        age = input('Age: ')
        reg = input('Region: ')
        city = input('City: ')
        num = input('Mobile no.: ')
        email = input('Email: ')
        test = input('Were you recently tested for COVID-19? (Y/n): ')

        test = test.lower()
        while test not in ['y','n']:
            print('ERROR! Y/n only')
            test = input('Were you recently tested for COVID-19? (Y/n): ')

        if test == 'y':
            pos = input('Did you test positive for COVID? (Y/n): ')
            pos = pos.lower()

            if pos == 'y':
                print('\nWe sincerely hope you get well soon.')

            else:
                print('\nGood to know :)')



        print("\nYour data has been recorded and will be saved.")


        #logging of items to dictionaries
        agedict[name] = age
        regdict[name] = reg
        citydict[name] = city
        numdict[name] = num
        emaildict[name] = email
        testdict[name] = test

        print(agedict)
        print (regdict)




#2. search full name, then display
#3. exit or retry

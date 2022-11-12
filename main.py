#display menu
print("Menu:\n 1.) Add an item\n 2.) Search\n 3.) Exit (Y/n)\n")

#select item in menu
option = input("What do you want to do? (1-3): ")

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
        vaxx = input('Have you been vaccinated for COVID-19? (Y/n): ')
        symp = input('Are you currently experiencing any symptoms of COVID-19? (Y/n): ')
        test = input('Were you recently tested for COVID-19? (Y/n): ')

        vaxx = vaxx.lower()
        symp = symp.lower()
        test = test.lower()

        if test == 'y':
            pos = input('Did you test positive for COVID? (Y/n): ')
            pos = pos.lower()

            if pos == 'y':
                print('\nWe sincerely hope you get well soon.')

        print("\nYour data has been recorded and will be saved.")


        #logging of items to dictionary








#2. search full name, then display
#3. exit or retry

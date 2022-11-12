#display menu
print("Menu:\n 1.) Add an item\n 2.) Search\n 3.) Exit (Y/n)\n")



agedict = {}
regdict = {}
citydict = {}
numdict = {}
emaildict = {}
testdict = {}




while True:

    # select item in menu
    option = input("What do you want to do? (1-3):")

    while option not in ['1', '2', '3']:
        print('\nERROR! select a number from 1-3\n')
        option = input("What do you want to do? (1-3):")

    # perform option

    # 1. ask data for contact tracing

    if option == '1':
        name = input('Name:')
        name = name.lower()
        age = input('Age:')
        reg = input('Region:')
        city = input('City:')
        num = input('Mobile no.:')
        email = input('Email:')
        test = input('Were you recently tested for COVID-19? (Y/n):')

        test = test.lower()
        while test not in ['y','n']:
            print('ERROR! Y/n only')
            test = input('Were you recently tested for COVID-19? (Y/n):')

        if test == 'y':
            pos = input('Did you test positive for COVID? (Y/n):')
            pos = pos.lower()

            if pos == 'y':
                print('\nWe sincerely hope you get well soon.')

            else:
                print('Good to know :)')



        print("\nYour data has been recorded and will be saved.\n")


        #logging of items to dictionaries
        agedict[name] = age
        regdict[name] = reg
        citydict[name] = city
        numdict[name] = num
        emaildict[name] = email
        testdict[name] = test

    # 2. search full name, then display data
    if option == '2':
        name = input('Name:')
        name = name.lower()
        print('\nHere are the details found under that name:')
        print('Age:',agedict.get(name))
        print('Region:',regdict.get(name))
        print('City:',citydict.get(name))
        print('Mobile no.:',numdict.get(name))
        print('Email:',emaildict.get(name))
        print('Recently tested for COVID? (y/n) :',testdict.get(name)'\n')

    # 3. exit or retry
    if option == '3':
        cont = input("Exit? (Y/n):")
        cont = cont.lower()

        if cont == 'y':
            break;

        else:
            continue;




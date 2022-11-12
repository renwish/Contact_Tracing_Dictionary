#display menu
print("Menu:\n 1.) Add an item\n 2.) Search\n 3.) Exit (y/n)\n")

#select item in menu
option = input("What do you want to do? (1-3): ")

#perform option
#1. ask data for contact tracing
while option not in ['1','2','3']:
    print('ERROR! select a number from 1-3')
    option = input("What do you want to do? (1-3): ")

if option == '1':
    print('yay')


#2. search full name, then display
#3. exit or retry

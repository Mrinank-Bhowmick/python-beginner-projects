def table():
    while True:                             #will stay True forever
        n=int(input('Enter the Number : '))   #user input
        for i in range(1,11):               #loop running from 1 to 10, 11 is exclusive
            print(n,'x',i,'=',n*i)  
        print('\n')    
        print('Want to Know Table of any Other Number?')    #restarting the loop from the start, as per the user choice
        print('Press (y/n)')
        ch=input()
        if ch=='N' or ch=='n':
            print("Thank You For Using")
            break
        else:
            continue

table()

def table():
    while True:
        n=int(input('Enter the Number : '))
        for i in range(1,11):
            print(n,'x',i,'=',n*i)
        print('\n')    
        print('Want to Know Table of any Other Number?')
        print('Press (y/n)')
        ch=input()
        if ch=='N' or ch=='n':
            print("Thank You For Using")
            break
        else:
            continue

table()

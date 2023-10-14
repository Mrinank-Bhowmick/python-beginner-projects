import random

comp= random.randint(0,2)
# print(comp)

#Using input to take the input from the user
# 0 for snake 1 for water and 2 for gun 
#as rule defined snake drinks water ,water damaged gun,and gun kills snake 

# points counting 
comp_score=0    
user_score=0
n_times=0   
while(True):
    if(n_times==5):
     break   
    user_inp=int(input("Enter your prefered number (0 for snake 1 for water and 2 for Gun and 5 for quit)"))
    n_times=user_inp
    print(f"computer's turn {comp}")
    if(comp==user_inp):
        print('Game draw!')
    elif(comp==0 and user_inp==1):
        print('Computer won!')   
        comp_score=comp_score+1 
    elif(comp==0 and user_inp==2):
        print('User won! hehey')
        user_score=user_score+1         
    elif(comp==1 and user_inp==2):
        print('Computer won!')    
        comp_score=comp_score+1 
    elif(comp==1 and user_inp==0):
        print('User won! hehey')    
        user_score=user_score+1    
    elif(comp==2 and user_inp==0):
        print('computer won!')
        comp_score=comp_score+1 
    elif(comp==2 and user_inp==1):
        print('User won! hehey')
        user_score=user_score+1   

         
        


print('User Won with the score',user_score) if (user_score>comp_score) else print('computer won with the score',comp_score)
    

            
    

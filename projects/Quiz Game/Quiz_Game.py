print("welcome! Enjoy the quiz game!")

playing = input("Do you want to play?\n") 

if playing.lower() != 'yes':     
##'lower' is a method in python that converts text in lower case. And 'Upper' converts text in upper case.
#it will evaluate as boolean.
    quit()

print("Okey! Let's play :)")
score = 0

answer = input("What does 'CPU' stand for?\n")
if answer.lower() == "central processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
    

answer = input("What does 'GPU' stand for?\n")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
    
    
answer = input("What does 'RAM' stand for?\n")
if answer.lower() == "random access memory":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")
    
    
answer = input("What does 'PSU' stand for?\n")
if answer.lower() == "power supply unit":
    print('Correct!')
    score+=1
else:
    print("Incorrect!")

print("You got " +str(score) + " questions correct!")
print("You got " +str((score/4) * 100) + " %.")
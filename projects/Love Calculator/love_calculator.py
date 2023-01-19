def love_calculator():
    per1 = input("enter your name: ")
    per2 = input("enter your lovers name: ")
    word1, word2 = list('true'), list('love')
    ct, ct2 = 0 , 0
    
    for i in per1 + per2:
        if i in word1:
            ct += 1
        elif i in word2:
            ct2 += 1
    score = int(str(ct) + str(ct2))
    
    if score < 10 or score > 90:
        print(f"Your match with {per2} it high af! perfect match. score {score}")
    elif score > 40 and score < 50:
        print(f"You and {per2} will be alright together... nothing more... score {score}")
    else:
        print(f"it's a disaster... score is {score}")

if __name__ == "__main__":
    love_calculator()
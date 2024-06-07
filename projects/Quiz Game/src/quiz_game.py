def welcome_message():
    print("Welcome to AskPython Quiz!!")

def start_game():
    return input("Are you ready to play the Quiz? (yes/no) :").lower() == "yes"

def get_questions():
    return [
        {"question":"Question 1: What is your Favourite programming language?","answer":"python"},
        {"question":"Question 2: Do you follow any author on AskPython?","answer":"yes"},
        {"question":"Question 3: What is the name of your favourite website for learning Python?","answer":"askpython"},
    ]

def result(score,total):
    print(f"Thank you for Playing this small quiz game, you attempted{score}, questions correctly!",)
    mark = int((score / total) * 100)
    print(f"Marks obtained: {mark}%")
print("Welcome to AskPython Quiz")

# Get user's readiness to play the Quiz
answer = input("Are you ready to play the Quiz? (yes/no) :")

# Initialize the score and total number of questions
score = 0
total_questions = 3

# Check if the user is ready to play
if answer.lower() == "yes":
    # Question 1
    answer = input("Question 1: What is your Favourite programming language?")
    if answer.lower() == "python":
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect

    # Question 2
    answer = input("Question 2: Do you follow any author on AskPython? ")
    if answer.lower() == "yes":
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect

    # Question 3
    answer = input(
        "Question 3: What is the name of your favourite website for learning Python?"
    )
    if answer.lower() == "askpython":
        score += 1
        print("correct")  # User's answer is correct, increment the score
    else:
        print("Wrong Answer :(")  # User's answer is incorrect

# Display the result and user's score
print(
    "Thank you for Playing this small quiz game, you attempted",
    score,
    "questions correctly!",
)
mark = int((score / total_questions) * 100)
print(f"Marks obtained: {mark}%")

# Farewell message
print("BYE!")

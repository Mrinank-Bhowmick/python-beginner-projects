# === Quiz Game · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ZackeryRSmith.

import sqlite3


# Open (or create) the SQLite database file
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


# Insert a player's name and score into the database
def save_score(conn, name, score):
    sql = """ INSERT INTO scores(name, score)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, (name, score))
    conn.commit()
    return cur.lastrowid


# Fetch all scores ordered best first
def get_all_scores(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM scores ORDER BY score DESC")

    rows = cur.fetchall()
    return rows


# Welcome the player to the quiz
print("Welcome to AskPython Quiz")

# Ask if the player is ready to start
answer = input("Are you ready to play the Quiz? (yes/no) :")

# Track score and total question count
score = 0
total_questions = 3

# Only proceed if the player says yes
if answer.lower() == "yes":
    # Ask question 1 and check the answer
    answer = input("Question 1: What is your Favourite programming language?")
    if answer.lower() == "python":
        score += 1
        print("correct")
    else:
        print("Wrong Answer :(")

    # Ask question 2 and check the answer
    answer = input("Question 2: Do you follow any author on AskPython? ")
    if answer.lower() == "yes":
        score += 1
        print("correct")
    else:
        print("Wrong Answer :(")

    # Ask question 3 and check the answer
    answer = input(
        "Question 3: What is the name of your favourite website for learning Python?"
    )
    if answer.lower() == "askpython":
        score += 1
        print("correct")
    else:
        print("Wrong Answer :(")

    # Show final score and percentage
    print(
        "Thank you for Playing this small quiz game, you attempted",
        score,
        "questions correctly!",
    )
    mark = int((score / total_questions) * 100)
    print(f"Marks obtained: {mark}%")

    # Get player name and prepare to save score
    player_name = input("Enter your name: ")
    player_score = score

    database = "quiz_game.db"

    # Connect to the database
    conn = create_connection(database)

    if conn is not None:
        # Save score and display all previous scores
        save_score(conn, player_name, player_score)

        print("Previous scores:")
        scores = get_all_scores(conn)
        for row in scores:
            print(f"Name: {row[1]}, Score: {row[2]}, Date: {row[3]}")

        conn.close()
    else:
        print("Error! Cannot create the database connection.")
else:
    print(" Please, when you're ready, enter the game again.")

# Print farewell message
print("BYE!")

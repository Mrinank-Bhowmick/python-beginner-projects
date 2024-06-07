# import the sqlite3 to reterive previous scores
import sqlite3


# create Conn to have the database file
def create_connection(db_file):
    """create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


# store the player's score with their name
def save_score(conn, name, score):
    """
    Save the player's score to the database
    """
    sql = """ INSERT INTO scores(name, score)
              VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql, (name, score))
    conn.commit()
    return cur.lastrowid


#  recall the previous scores to display them
def get_all_scores(conn):
    """
    Query all rows in the scores table
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM scores ORDER BY score DESC")

    rows = cur.fetchall()
    return rows


# The beginning of the game
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

    # Getting the player's name and score to insert into the database
    player_name = input("Enter your name: ")
    player_score = score

    database = "quiz_game.db"

    # Create a database connection
    conn = create_connection(database)

    if conn is not None:
        # Save the player's score
        save_score(conn, player_name, player_score)

        # Display all scores
        print("Previous scores:")
        scores = get_all_scores(conn)
        for row in scores:
            print(f"Name: {row[1]}, Score: {row[2]}, Date: {row[3]}")

        conn.close()
    else:
        print("Error! Cannot create the database connection.")
else:
    print(" Please, when you're ready, enter the game again.")

# Farewell message
print("BYE!")

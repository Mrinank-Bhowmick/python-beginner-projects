class QuizGameSystem:
    def __init__(self):
        self.questions = self.get_questions()

    def welcome_message(self):
        print("Welcome to AskPython Quiz!!")

    def start_game(self):
        return input("Are you ready to play the Quiz? (yes/no) :").lower() == "yes"

    def get_questions(self):
        return [
            {"question": "Question 1: What is your Favourite programming language?",
             "answer": "python"},
            {"question": "Question 2: Do you follow any author on AskPython?",
             "answer": "yes"},
            {"question": "Question 3: What is the name of your favourite website for learning Python?",
             "answer": "askpython"},
        ]

    def ask_question(self,question, correct_answer):
        answer = input(question)
        if answer == correct_answer:
            print("correct\n")
            return 1
        else:
            print("Wrong Answer :(\n")
            return 0

    def show_result(self, score, total):
        print(f"Thank you for Playing this small quiz game, you attempted {score}, questions correctly!\n")
        mark = int((score / total) * 100)
        print("<<<<<Correct answers>>>>>")
        show_answer(self)
        print(f"Marks obtained: {mark}%\n")

def show_answer(self):
    count = 1
    for question in self.questions:
        answer = question["answer"]
        print(f"Question {count}:{answer}")
        count += 1

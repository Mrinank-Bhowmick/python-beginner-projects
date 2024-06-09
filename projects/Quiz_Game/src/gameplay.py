from gamesystem import QuizGameSystem

def main():
    game = QuizGameSystem()
    game.welcome_message()
    start = game.start_game()

    if (start):
        score = 0
        total_questions = len(game.get_questions())

        for question in game.get_questions():
            if(game.ask_question(question["question"], question["answer"])):
                score += 1

        game.show_result(score, total_questions)

    else:
        print("See you next time")


if __name__ == "__main__":
    main()

import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word_list = ["python", "hangman", "programming", "computer", "developer", "code", "challenge"]
        self.word = ""
        self.guessed_letters = []
        self.max_attempts = 6
        self.attempts = 0
        self.guessed = set()

        # Initialize hangman stages
        self.hangman_stages = [
            "  ____\n |    |\n      |\n      |\n      |\n      |\n",
            "  ____\n |    |\n O    |\n      |\n      |\n      |\n",
            "  ____\n |    |\n O    |\n |    |\n      |\n      |\n",
            "  ____\n |    |\n O    |\n/|    |\n      |\n      |\n",
            "  ____\n |    |\n O    |\n/|\\   |\n      |\n      |\n",
            "  ____\n |    |\n O    |\n/|\\   |\n/     |\n      |\n",
            "  ____\n |    |\n O    |\n/|\\   |\n/ \\   |\n      |\n"
        ]
        
        self.current_hangman = tk.Label(root, text=self.hangman_stages[0], font=("Courier", 16))
        self.current_hangman.pack()

        self.word_label = tk.Label(root, text="", font=("Arial", 24))
        self.word_label.pack()

        self.attempts_label = tk.Label(root, text="", font=("Arial", 16))
        self.attempts_label.pack()

        self.letter_buttons = [None] * 26
        for i in range(26):
            letter = chr(ord("a") + i)
            self.letter_buttons[i] = tk.Button(
                root, text=letter, font=("Arial", 16),
                command=lambda letter=letter: self.make_guess(letter)
            )
            self.letter_buttons[i].pack(side="left")

        self.new_game_button = tk.Button(
            root, text="New Game", command=self.play_new_game, font=("Arial", 16)
        )
        self.new_game_button.pack()

        self.play_new_game()

    def play_new_game(self):
        self.word = random.choice(self.word_list)
        self.guessed_letters = ["_"] * len(self.word)
        self.attempts = 0
        self.guessed = set()
        self.update_display()

    def update_display(self):
        word_display = " ".join(self.guessed_letters)
        self.word_label.config(text=word_display)
        attempts_text = f"Attempts left: {self.max_attempts - self.attempts}"
        self.attempts_label.config(text=attempts_text)
        self.current_hangman.config(text=self.hangman_stages[self.attempts])

    def make_guess(self, guess):
        if self.attempts >= self.max_attempts or "_" not in self.guessed_letters:
            return

        if guess in self.guessed:
            return

        self.guessed.add(guess)

        if guess in self.word:
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.guessed_letters[i] = guess
        else:
            self.attempts += 1

        self.update_display()

        if "_" not in self.guessed_letters:
            self.word_label.config(text=f"Congratulations! You guessed the word: {self.word}")
        elif self.attempts >= self.max_attempts:
            self.word_label.config(text=f"Sorry, you're out of attempts. The word was: {self.word}")

if __name__ == "__main__":
    root = tk.Tk()
    hangman = HangmanGame(root)
    root.mainloop()

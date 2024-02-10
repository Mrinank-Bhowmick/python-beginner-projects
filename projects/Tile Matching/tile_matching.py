import tkinter as tk
import random
from tkinter import messagebox


class TileMatchingGame:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.tiles = []
        self.selected_tiles = []
        self.is_game_over = False
        self.create_board()
        self.score = 0
        self.attempts = 0
        self.create_scoreboard()
        self.create_timer(60)

    def create_board(self):
        all_colors = [
            "lightcoral",
            "lightseagreen",
            "lightsteelblue",
            "lightgoldenrodyellow",
            "lightsalmon",
            "lightgreen",
            "lightpink",
            "lightcyan",
        ]
        colors = random.sample(all_colors, self.rows * self.columns // 2)
        colors *= 2  # Duplicate colors to have pairs
        random.shuffle(colors)

        for row in range(self.rows):
            tile_row = []
            for col in range(self.columns):
                tile = tk.Label(
                    self.root,
                    text="",
                    width=10,
                    height=4,
                    relief="raised",
                    borderwidth=3,
                    bg="gray",  # Initially, tiles are gray (hidden)
                )
                tile.grid(row=row, column=col)
                tile.bind("<Button-1>", self.tile_clicked)
                tile_row.append(tile)
            self.tiles.append(tile_row)
        self.tile_colors = colors

    def create_scoreboard(self):
        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.grid(row=self.rows, columnspan=self.columns)
        self.attempts_label = tk.Label(self.root, text="Attempts: 0")
        self.attempts_label.grid(row=self.rows + 1, columnspan=self.columns)

    def create_timer(self, seconds):
        self.timer_label = tk.Label(self.root, text=f"Time: {seconds}")
        self.timer_label.grid(row=self.rows + 2, columnspan=self.columns)
        self.remaining_time = seconds
        self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0 and not self.is_game_over:
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time: {self.remaining_time}")
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")
            self.is_game_over = True

    def tile_clicked(self, event):
        if self.is_game_over:
            return

        tile = event.widget
        row, col = self.get_tile_position(tile)
        if (row, col) not in self.selected_tiles and len(self.selected_tiles) < 2:
            tile.config(
                text="X", bg=self.tile_colors[row * self.columns + col]
            )  # Reveal the color when clicked
            self.selected_tiles.append((row, col))

            if len(self.selected_tiles) == 2:
                self.root.update_idletasks()
                self.root.after(500, self.check_matching_tiles)
                self.attempts += 1
                self.attempts_label.config(text=f"Attempts: {self.attempts}")

    def check_matching_tiles(self):
        if len(self.selected_tiles) == 2:
            tile1 = self.selected_tiles[0]
            tile2 = self.selected_tiles[1]
            if (
                self.tile_colors[tile1[0] * self.columns + tile1[1]]
                == self.tile_colors[tile2[0] * self.columns + tile2[1]]
            ):
                self.score += 1
                self.score_label.config(text=f"Score: {self.score}")
                if self.score == self.rows * self.columns // 2:
                    self.end_game()

            else:
                self.root.update_idletasks()
                self.root.after(500, self.hide_unmatched_tiles, tile1, tile2)

    def hide_unmatched_tiles(self, tile1, tile2):
        self.tiles[tile1[0]][tile1[1]].config(text="", bg="gray")
        self.tiles[tile2[0]][tile2[1]].config(text="", bg="gray")
        self.selected_tiles = []

    def end_game(self):
        self.timer_label.config(text="Game Over!")
        self.is_game_over = True
        messagebox.showinfo("Congratulations!", "You've won the game!")

    def get_tile_position(self, tile):
        for row, row_tiles in enumerate(self.tiles):
            if tile in row_tiles:
                col = row_tiles.index(tile)
                return row, col

    def reset_game(self):
        self.root.destroy()
        main()


def main():
    root = tk.Tk()
    root.title("Tile Matching Game")

    rows, columns = 4, 4

    game = TileMatchingGame(root, rows, columns)

    # Reset Button
    reset_button = tk.Button(root, text="Reset Game", command=game.reset_game)
    reset_button.grid(row=rows + 3, columnspan=columns)

    # Exit Button
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.grid(row=rows + 4, columnspan=columns)

    root.mainloop()


if __name__ == "__main__":
    main()

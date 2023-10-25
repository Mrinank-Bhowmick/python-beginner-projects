#2048 game using python

from tkinter import *
import random

class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.main_grid = Frame(self, bg='lightgrey', bd=3, width=400,height=400)
        self.main_grid.grid()
      
#creating a 4 x 4 Gameboard
    def gameboard(self):
        self.tiles = []
        for i in range(4):
            row = []
            for j in range(4):
                tile_frame = Frame(
                    self.main_grid,
                    bg='white',
                    width='50',
                    height='50'
                )
                tile_frame.grid(
                    row=i, column=j, 
                    padx=3, pady=3
                )
                tile_number = Label(
                    self.main_grid, 
                    bg='white'
                )
                tile_number.grid(row=i, column=j)
                tile_data = 
                {
                   "frame": tile_frame, 
                   "number": tile_number
                }
                row.append(tile_data)
            self.tiles.append(row)

#MovetoLeft operation
    def moveToLeft(self):
        new_board = [[0 for col in range(4)] for row in range(4)]
        for i in range(4):
            fill_position = 0
            for j in range(4):
                if self.board[i][j] != 0:
                    new_board[i][fill_position] = self.board[i][j]
                    fill_position += 1
        self.board = new_board

#merge operation
    def merge(self):
        for i in range(4):
            for j in range(3):
                if self.board[i][j] != 0 and self.board[i][j] == self.board[i][j+1]:
                    self.board[i][j] *= 2
                    self.board[i][j+1] = 0

#reverse operation
    def reverse(self):
        new_board = []
        for i in range(4):
            new_board.append([])
            for j in range(4):
                new_board[i].append(self.board[i][3-j])
        self.board = new_board

#Transpose operation
    def transpose(self):
        new_board = [[0 for col in range(4)] for row in range(4)]
        for i in range(4):
            for j in range(4):
                new_board[i][j] = self.board[j][i]
        self.board = new_board

#pick random values
    def pickNewValue(self):
        row = col = 0
        while self.board[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)

        if random.randint(1, 5) == 1:
            self.board[row][col] = 4
        else:
            self.board[row][col] = 2

#update the board
    def updateGame(self):
        for i in range(4):
            for j in range(4):
                tile_value = self.board[i][j]
                if tile_value == 0:
                    self.tiles[i][j]["frame"].configure(bg="white")
                    self.tiles[i][j]["number"].configure(bg="white", text="")
                else:
                    self.tiles[i][j]["frame"].configure(bg="orange")
                    self.tiles[i][j]["number"].configure(
                        bg="orange",
                        fg="white",
                        font="20",
                   text=str(tile_value)
                    )
            self.update_idletasks()

#Moves for the game
#Left move
    def left(self, event):
        self.moveToLeft()
        self.merge()
        self.moveToLeft()
        self.pickNewValue()
        self.updateGame()
        self.final_result()
#Right move
    def right(self, event):
        self.reverse()
        self.moveToLeft()
        self.merge()
        self.moveToLeft()
        self.reverse()
        self.pickNewValue()
        self.updateGame()
        self.final_result()
#up move
    def up(self, event):
        self.transpose()
        self.moveToLeft()
        self.merge()
        self.moveToLeft()
        self.transpose()
        self.pickNewValue()
        self.updateGame()
        self.final_result()
#Down move
   def down(self, event):
        self.transpose()
        self.reverse()
        self.moveToLeft()
        self.merge()
        self.moveToLeft()
        self.reverse()
        self.transpose()
        self.pickNewValue()
        self.updateGame()
        self.final_result()

#check for moves
    def horizontal_move_exists(self):
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j+1]:
                    return True
        return False

    def vertical_move_exists(self):
        for i in range(3):
            for j in range(4):
                if self.board[i][j] == self.board[i+1][j]:
                    return True
        return False

#End of moves
    def final_result(self):
        if any(2048 in row for row in self.board):
            game_over_frame = Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor='center')
            Label(
                game_over_frame,
                text="You Win",
                bg="green",
                fg="white",
                font="20"
            ).pack()

        elif not any(0 in row for row in self.board) and not self.horizontal_move_exists() and not self.vertical_move_exists():
            game_over_frame = Frame(self.main_grid, borderwidth=2)
            game_over_frame.place(relx=0.5, rely=0.5, anchor='center')
            Label(
                game_over_frame,
                text="Game Over",
                bg="Red",
                fg="white",
                font="20"
            ).pack()


#Show output
#To show the gameboard and all the graphics we need to add some more steps. First, we need to call the functions to create the board and start the game in the init method at the beginning of the code. There we also need to bind the moves to keyboard press. The mainloop() is added to keep the GUI running.
class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.main_grid = Frame(self, bg='lightgrey', bd=3, width=400,height=400)
        self.main_grid.grid()
        
        #call the functions to run the program
        self.gameboard()
        self.start_game()

        self.master.bind("<Left>", self.left)
        self.master.bind("<Right>", self.right)
        self.master.bind("<Up>", self.up)
        self.master.bind("<Down>", self.down)

        self.mainloop()

#At the end of the code, we need to create an instance of the class Game to run the code.
def main():
    Game()

if __name__ == "__main__":
    main()

# ==== creating main class
class Play_2048(Tk):

   # ==== adding necessary class variables
   game_board = []
   new_random_tiles = [2, 2, 2, 2, 2, 2, 4]
   score = 0
   high_score = 0
   game_score = 0
   highest_score = 0

   # ==== creating user window
   def __init__(self, *args, **kwargs):
       Tk.__init__(self, *args, **kwargs)
       # ==== create user interface
       self.game_score = StringVar(self)
       self.game_score.set("0")
       self.highest_score = StringVar(self)
       self.highest_score.set("0")

       # ==== adding new game , score and highest score option
       self.button_frame = Frame(self)
       self.button_frame.grid(row=2, column=0, columnspan=4)
       Button(self.button_frame, text="New Game", font=("times new roman", 15), command=self.new_game).grid(row=0, column=0)
       self.button_frame.pack(side="top")

       Label(self.button_frame, text="Score:", font=("times new roman", 15)).grid(row=0, column=1)
       Label(self.button_frame, textvariable=self.game_score, font=("times new roman", 15)).grid(row=0, column=2)
       Label(self.button_frame, text="Record:", font=("times new roman", 15)).grid(row=0, column=3)
       Label(self.button_frame, textvariable=self.highest_score, font=("times new roman", 15)).grid(row=0, column=4)

       self.canvas = Canvas(self, width=410, height=410, borderwidth=5, highlightthickness=0)
       self.canvas.pack(side="top", fill="both", expand="false")

       # ==== create new game
       self.new_game()

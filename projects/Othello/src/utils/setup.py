from utils.board import Board
from utils.minimax import find_best_move
import pygame

pygame.init()

class Application:
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 800

    def __init__(self) -> None:
        '''Initiliase the Application Object with the necessary initialisations.'''

        self.game_board = Board()

        # pygame initialisations
        self.screen = pygame.display.set_mode(  (Application.SCREEN_WIDTH, 
                                                 Application.SCREEN_HEIGHT  ))
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

        pygame.display.set_caption("Othello/Reversi")

        # image initialisations
        self.boardIMG = pygame.image.load("images/Othello_Black_Side_Board.png")
        self.blackDiscIMG = pygame.image.load("images/Black_Disc.png")
        self.whiteDiscIMG = pygame.image.load("images/White_Disc.png")

        self.blackDiscCounterIMG = pygame.image.load("images/Large_Black_Disc.png")
        self.whiteDiscCounterIMG = pygame.image.load("images/Large_White_Disc.png")

        self.possibleBlackMoveIMG = pygame.image.load("images/Black_Disc.png")
        self.possibleWhiteMoveIMG = pygame.image.load("images/White_Disc.png")
        pygame.Surface.set_alpha(self.possibleBlackMoveIMG, 50)
        pygame.Surface.set_alpha(self.possibleWhiteMoveIMG, 50)

        self.endScreenBlackIMG = pygame.image.load("images/End_Screen_Black.png")
        self.endScreenWhiteIMG = pygame.image.load("images/End_Screen_White.png")
        self.endScreenDrawIMG = pygame.image.load("images/End_Screen_Draw.png")
        self.endPromptIMG  = pygame.image.load("images/End_Prompt.png")

        self.choiceIMG = pygame.image.load("images/Othello_Game-mode_Choice.png")

        # font initialisation
        self.discCountFont = pygame.font.Font("Gotham-Font/GothamLight.ttf", 40)

        self.single_player = False
        self.displayed_choice = False

        self.running = True
        self.game_end = False
        self.shown_moves = False

        self.hasBlackForfeited = False
        self.hasWhiteForfeited = False

        self.turn = Board.BLACK
        self.possible_moves = []
        self.last_move = (20, 20)

    @staticmethod
    def fade(screen: pygame.Surface, *surfaceNcoords: tuple[pygame.Surface, tuple[int, int]]):
        '''Fade-in surface(s) on a given screen, at the specified coordinates.'''

        for alpha in range(0, 257, 6):
            for snc in surfaceNcoords:
                surface, coordinates = snc
                surface.set_alpha(alpha)
                screen.blit(surface, coordinates)
                pygame.time.delay(30)
            pygame.display.flip()

    def handleMouseClick(self) -> None:
        '''Handle events following mouse click on the board'''

        mx, my = pygame.mouse.get_pos()
        mx -= 100
        my -= 100
        r = my // 75
        c = mx // 75

        if (r, c) not in self.possible_moves:   return

        self.last_move = (r, c)
        self.game_board.set_discs(r, c, self.turn)
        self.possible_moves.remove((r,c))
        self.shown_moves = False

        for pos in self.possible_moves:
            row, col = pos
            x = 100 + 75 * col
            y = 100 + 75 * row
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x+4, y+4, 67, 67))

        self.turn *= -1
    
    def handleGameEnd(self, event: pygame.event.Event):
        '''Handle the events following the end of game:
                1. Either restarts the game,
                2. Or Quits the Application.
        '''

        if event.key not in (pygame.K_r, pygame.K_q): return

        # fade out the screen
        dummy_surface = pygame.Surface( (Application.SCREEN_WIDTH, 
                                            Application.SCREEN_HEIGHT  ))
        dummy_surface.fill((255, 255, 255))
        Application.fade(self.screen, (dummy_surface, (0, 0)))

        if event.key == pygame.K_q:
            self.running = False
            return
        
        self.turn = 1
        self.single_player = False
        self.displayed_choice = False
        self.game_end = False
        self.game_board.reset_board()

        self.screen.blit(self.boardIMG, (0,0))
        self.screen.blit(self.blackDiscCounterIMG, (775, 475))
        self.screen.blit(self.whiteDiscCounterIMG, (950, 475))
        self.last_move = (20, 20)

    def displayDiscs(self) -> None:
        '''Display all the dics present on the game board'''

        for row in range(8):
            for col in range(8):
                if self.game_board.board[row, col] == Board.BLACK:
                    x = 100 + 75 * col
                    y = 100 + 75 * row
                    self.screen.blit(self.blackDiscIMG, (x,y))

                elif self.game_board.board[row, col] == Board.WHITE:
                    x = 100 + 75 * col
                    y = 100 + 75 * row
                    self.screen.blit(self.whiteDiscIMG, (x,y))
    
    def markLastMove(self) -> None:
        '''Mark the last move made on the game board'''

        r, c = self.last_move

        RED = (255, 0, 0)
        x = c * 75 + 100 + 75/2
        y = r * 75 + 100 + 75/2
        pygame.draw.circle(surface=self.screen, color=RED, center=(x, y), radius=5)

    def displayScore(self) -> None:
        '''Blit the score of each player during the game'''

        dummy_surface = pygame.Surface((60, 40))
        dummy_surface.fill((255, 255, 255))
        self.screen.blit(dummy_surface, (885, 510))
        self.screen.blit(dummy_surface, (1060, 510))

        black_disc_count = self.discCountFont.render(f"{self.game_board.black_disc_count}", False, (0, 0, 0))
        white_disc_count = self.discCountFont.render(f"{self.game_board.white_disc_count}", False, (0, 0, 0))
        self.screen.blit(black_disc_count, (885, 510))
        self.screen.blit(white_disc_count, (1060, 510))

    def displayLegalMoves(self) -> None:
        '''Display all the possible legal moves for the player with the current turn.'''

        if self.shown_moves:    # possible moves are already displayed
            return
        
        self.possible_moves = list(self.game_board.all_legal_moves(self.turn))
        if self.possible_moves == []:
            if self.turn == Board.BLACK:
                self.hasBlackForfeited = True
            else:
                self.hasWhiteForfeited = True
            self.shown_moves = not (self.hasBlackForfeited if self.turn == Board.BLACK else self.hasWhiteForfeited)
            self.turn *= -1
            return
        
        # else there are new possible moves to be displayed

        if self.turn == Board.BLACK:
            self.hasBlackForfeited = False
        else:
            self.hasWhiteForfeited = False
        
        possibleMoveIMG = self.possibleBlackMoveIMG if self.turn == Board.BLACK else self.possibleWhiteMoveIMG
        for pos in self.possible_moves:
            r, c = pos
            x = 100 + 75 * c
            y = 100 + 75 * r
            self.screen.blit(possibleMoveIMG, (x, y))
            
        self.shown_moves = not (self.hasBlackForfeited if self.turn == Board.BLACK else self.hasWhiteForfeited)

    def gameOverScreen(self) -> None:
        '''Display the game over screen in accordance with the game result.'''

        if self.game_board.black_disc_count > self.game_board.white_disc_count: # black won
            Application.fade(self.screen, (self.endScreenBlackIMG, (725, 250)))

        elif self.game_board.black_disc_count < self.game_board.white_disc_count:   # white won
            Application.fade(self.screen, (self.endScreenWhiteIMG, (725, 250)))

        else:   # draw
            Application.fade(self.screen, (self.endScreenDrawIMG, (725, 250)))

        Application.fade(self.screen, (self.endPromptIMG, (877, 420)))
        self.game_end = True
    
    def computerPlayerTurn(self) -> None:
        '''Code to run when it is computer player's turn.'''
        
        r, c = find_best_move(self.game_board)
        if (r,c) == (20, 20):
            self.hasWhiteForfeited = True
            self.shown_moves = not self.hasWhiteForfeited
        else:
            self.last_move = (r, c)
            self.game_board.set_discs(r, c, self.turn)
            self.shown_moves = False
        self.turn *= -1

    def handleGameModeChoice(self, event) -> None:
        '''Handle the events at the initial screen.'''

        if event.key not in (pygame.K_a, pygame.K_h):
            return
        
        self.single_player = (event.key == pygame.K_a)

        self.displayed_choice = True

        dummy_surface = pygame.Surface( (Application.SCREEN_WIDTH, 
                                            Application.SCREEN_HEIGHT  ))
        dummy_surface.fill((255, 255, 255))
        Application.fade(self.screen, (dummy_surface, (0, 0)))

        self.displayInitialBoardPos()
            
    def displayInitialBoardPos(self) -> None:
        '''Blitting initial board position on screen'''

        self.screen.blit(self.boardIMG, (0,0))
        self.screen.blit(self.blackDiscCounterIMG, (775, 475))
        self.screen.blit(self.whiteDiscCounterIMG, (950, 475))
        pygame.display.flip()

    def game_loop(self) -> None:
        '''Game loop to run the application.'''

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handleMouseClick()
                elif self.game_end and event.type == pygame.KEYDOWN:
                    self.handleGameEnd(event)
                elif not self.displayed_choice and event.type == pygame.KEYDOWN:
                    self.handleGameModeChoice(event)
            
            if not self.displayed_choice:
                self.screen.blit(self.choiceIMG, (0,0))
                pygame.display.flip()
                continue

            if self.game_end:
                continue  
            
            if self.single_player and self.turn == Board.WHITE:
                self.computerPlayerTurn()
                
            self.displayDiscs()
            
            self.markLastMove()

            self.displayLegalMoves()

            self.displayScore()

            if self.hasBlackForfeited and self.hasWhiteForfeited:
                self.gameOverScreen()

            pygame.display.flip()

        pygame.quit()
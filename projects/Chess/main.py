# import necessary dependencies
from sys import exit
import pygame

# initialize the game
pygame.init()

# display game
surface = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Chess")

grid = [
    ["r", "n", "b", "q", "k", "b", "n", "r"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
]

selected = False
selectX, selectY, moveX, moveY = None, None, None, None
validMoves = None
turn = 1


# define ValidMoveGenerator class
class ValidMoveGenerator(object):
    def __init__(self):
        self.vMoves = []
        self.vMoves2 = []
        self.white = None

    def generateValidMoves(self, x, y, grid):
        global validMoves
        self.vMoves = []
        self.vMoves2 = []
        self.white = grid[x][y].isupper()

        piece = grid[x][y].upper()
        if piece == "K":
            validMoves = self.King(x, y, grid)
        elif piece == "Q":
            validMoves = self.Queen(x, y, grid)
        elif piece == "R":
            validMoves = self.Rook(x, y, grid)
        elif piece == "B":
            validMoves = self.Bishop(x, y, grid)
        elif piece == "N":
            validMoves = self.Knight(x, y, grid)
        elif piece == "P":
            validMoves = self.Pawn(x, y, grid)
        return validMoves

    def King(self, x, y, grid):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                self.vMoves.append([x + i, y + j])

        for i in range(len(self.vMoves)):
            if (
                self.vMoves[i][1] >= 0
                and self.vMoves[i][0] >= 0
                and self.vMoves[i][1] < 8
                and self.vMoves[i][0] < 8
            ):
                base = grid[self.vMoves[i][0]][self.vMoves[i][1]]
                sameColor = None
                if base == 0:
                    sameColor = False
                elif self.white:
                    sameColor = base.isupper()
                else:
                    sameColor = base.islower()

                if not sameColor:
                    self.vMoves2.append([self.vMoves[i][0], self.vMoves[i][1]])

        return self.vMoves2

    def Queen(self, x, y, grid):
        r, b = self.Rook(x, y, grid), self.Bishop(x, y, grid)
        for i in range(len(r)):
            self.vMoves.append(r[i])
        for i in range(len(b)):
            self.vMoves.append(b[i])
        return self.vMoves

    def Rook(self, x, y, grid):
        for i in range(x + 1, 8):
            if grid[i][y] == 0:
                self.vMoves.append([i, y])
                continue
            if not self.sameColor(i, y, grid):
                self.vMoves.append([i, y])
                break
            break
        for i in range(x - 1, -1, -1):
            if grid[i][y] == 0:
                self.vMoves.append([i, y])
                continue
            if not self.sameColor(i, y, grid):
                self.vMoves.append([i, y])
                break
            break
        for i in range(y + 1, 8):
            if grid[x][i] == 0:
                self.vMoves.append([x, i])
                continue
            if not self.sameColor(x, i, grid):
                self.vMoves.append([x, i])
                break
            break
        for i in range(y - 1, -1, -1):
            if grid[x][i] == 0:
                self.vMoves.append([x, i])
                continue
            if not self.sameColor(x, i, grid):
                self.vMoves.append([x, i])
                break
            break

        return self.vMoves

    def Bishop(self, x, y, grid):
        for i in range(1, 8):
            if (x + i < 8) and (y + i < 8):
                if grid[x + i][y + i] == 0:
                    self.vMoves.append([x + i, y + i])
                    continue
                if not self.sameColor(x + i, y + i, grid):
                    self.vMoves.append([x + i, y + i])
                    break
                break
            else:
                break
        for i in range(1, 8):
            if (x - i >= 0) and (y - i >= 0):
                if grid[x - i][y - i] == 0:
                    self.vMoves.append([x - i, y - i])
                    continue
                if not self.sameColor(x - i, y - i, grid):
                    self.vMoves.append([x - i, y - i])
                    break
                break
            else:
                break
        for i in range(1, 8):
            if (x + i < 8) and (y - i >= 0):
                if grid[x + i][y - i] == 0:
                    self.vMoves.append([x + i, y - i])
                    continue
                if not self.sameColor(x + i, y - i, grid):
                    self.vMoves.append([x + i, y - i])
                    break
                break
            else:
                break
        for i in range(1, 8):
            if (x - i >= 0) and (y + i < 8):
                if grid[x - i][y + i] == 0:
                    self.vMoves.append([x - i, y + i])
                    continue
                if not self.sameColor(x - i, y + i, grid):
                    self.vMoves.append([x - i, y + i])
                    break
                break
            else:
                break

        return self.vMoves

    def Knight(self, x, y, grid):
        if (
            x < 6
            and y < 7
            and (grid[x + 2][y + 1] == 0 or not self.sameColor(x + 2, y + 1, grid))
        ):
            self.vMoves.append([x + 2, y + 1])
        if (
            x < 6
            and y > 0
            and (grid[x + 2][y - 1] == 0 or not self.sameColor(x + 2, y - 1, grid))
        ):
            self.vMoves.append([x + 2, y - 1])
        if (
            x > 1
            and y < 7
            and (grid[x - 2][y + 1] == 0 or not self.sameColor(x - 2, y + 1, grid))
        ):
            self.vMoves.append([x - 2, y + 1])
        if (
            x > 1
            and y > 0
            and (grid[x - 2][y - 1] == 0 or not self.sameColor(x - 2, y - 1, grid))
        ):
            self.vMoves.append([x - 2, y - 1])
        if (
            x < 7
            and y < 6
            and (grid[x + 1][y + 2] == 0 or not self.sameColor(x + 1, y + 2, grid))
        ):
            self.vMoves.append([x + 1, y + 2])
        if (
            x > 0
            and y < 6
            and (grid[x - 1][y + 2] == 0 or not self.sameColor(x - 1, y + 2, grid))
        ):
            self.vMoves.append([x - 1, y + 2])
        if (
            x < 7
            and y > 1
            and (grid[x + 1][y - 2] == 0 or not self.sameColor(x + 1, y - 2, grid))
        ):
            self.vMoves.append([x + 1, y - 2])
        if (
            x > 0
            and y > 1
            and (grid[x - 1][y - 2] == 0 or not self.sameColor(x - 1, y - 2, grid))
        ):
            self.vMoves.append([x - 1, y - 2])
        return self.vMoves

    def Pawn(self, x, y, grid):
        if grid[x][y] == "p":
            if x == 1 and grid[x + 2][y] == 0:
                self.vMoves.append([x + 2, y])
            if grid[x + 1][y] == 0:
                self.vMoves.append([x + 1, y])
            if (
                y > 0
                and x < 7
                and grid[x + 1][y - 1] != 0
                and grid[x + 1][y - 1].isupper()
            ):
                self.vMoves.append([x + 1, y - 1])
            if (
                y < 7
                and x < 7
                and grid[x + 1][y + 1] != 0
                and grid[x + 1][y + 1].isupper()
            ):
                self.vMoves.append([x + 1, y + 1])
        elif grid[x][y] == "P":
            if x == 6 and grid[x - 2][y] == 0:
                self.vMoves.append([x - 2, y])
            if grid[x - 1][y] == 0:
                self.vMoves.append([x - 1, y])
            if (
                x > 0
                and y > 0
                and grid[x - 1][y - 1] != 0
                and grid[x - 1][y - 1].islower()
            ):
                self.vMoves.append([x - 1, y - 1])
            if (
                x > 0
                and y < 7
                and grid[x - 1][y + 1] != 0
                and grid[x - 1][y + 1].islower()
            ):
                self.vMoves.append([x - 1, y + 1])

        for i in range(len(self.vMoves)):
            if (
                self.vMoves[i][1] >= 0
                and self.vMoves[i][0] >= 0
                and self.vMoves[i][1] < 8
                and self.vMoves[i][0] < 8
            ):
                self.vMoves2.append(self.vMoves[i])

        return self.vMoves2

    def sameColor(self, x, y, grid):
        if self.white:
            return grid[x][y].isupper()
        else:
            return grid[x][y].islower()


validMoveGen = ValidMoveGenerator()


# define Board class
class Board(object):
    def __init__(self):
        self.sqs = [[], [], [], [], [], [], [], []]
        self.IMAGES = [
            pygame.transform.scale(
                pygame.image.load("Assets\\WhiteKing.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\WhiteQueen.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\WhiteRook.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\WhiteBishop.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\WhiteKnight.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\WhitePawn.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\BlackKing.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\BlackQueen.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\BlackRook.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\BlackBishop.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\BlackKnight.png"), (64, 85)
            ),
            pygame.transform.scale(
                pygame.image.load("Assets\\BlackPawn.png"), (64, 85)
            ),
        ]
        self.colors = [[], [], [], [], [], [], [], []]
        self.createBoard()

    def createBoard(self):
        for i in range(8):
            for j in range(8):
                self.sqs[i].append(pygame.Rect(j * 80, i * 80, 80, 80))
                if i % 2 == j % 2:
                    self.colors[i].append((200, 200, 200))
                else:
                    self.colors[i].append((30, 30, 30))

    def colorBoard(self):
        global surface
        surface.fill((12, 12, 12))
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(surface, self.colors[i][j], self.sqs[i][j])

    def placePieces(self):
        global surface, grid
        for i in range(8):
            for j in range(8):
                if grid[i][j] == "K":
                    surface.blit(
                        self.IMAGES[0],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[0].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[0].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "Q":
                    surface.blit(
                        self.IMAGES[1],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[1].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[1].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "R":
                    surface.blit(
                        self.IMAGES[2],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[2].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[2].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "B":
                    surface.blit(
                        self.IMAGES[3],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[3].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[3].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "N":
                    surface.blit(
                        self.IMAGES[4],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[4].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[4].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "P":
                    surface.blit(
                        self.IMAGES[5],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[5].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[5].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "k":
                    surface.blit(
                        self.IMAGES[6],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[6].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[6].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "q":
                    surface.blit(
                        self.IMAGES[7],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[7].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[7].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "r":
                    surface.blit(
                        self.IMAGES[8],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[8].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[8].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "b":
                    surface.blit(
                        self.IMAGES[9],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[9].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[9].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "n":
                    surface.blit(
                        self.IMAGES[10],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[10].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[10].get_rect().height / 2,
                        ),
                    )
                elif grid[i][j] == "p":
                    surface.blit(
                        self.IMAGES[11],
                        (
                            self.sqs[i][j].x
                            + self.sqs[i][j].width / 2
                            - self.IMAGES[11].get_rect().width / 2,
                            self.sqs[i][j].y
                            + self.sqs[i][j].height / 2
                            - self.IMAGES[11].get_rect().height / 2,
                        ),
                    )
                elif i % 2 == j % 2:
                    pygame.draw.rect(surface, (200, 200, 200), self.sqs[i][j])
                else:
                    pygame.draw.rect(surface, (30, 30, 30), self.sqs[i][j])

    def colorValidMoves(self, x, y):
        global validMoveGen
        self.colors[x][y] = (200, 200, 0)
        validMoves = validMoveGen.generateValidMoves(x, y, grid)
        for i in validMoves:
            self.colors[i[0]][i[1]] = (255, 121, 164)

    def resetColor(self):
        for i in range(8):
            for j in range(8):
                if i % 2 == j % 2:
                    self.colors[i][j] = (200, 200, 200)
                else:
                    self.colors[i][j] = (30, 30, 30)


board = Board()


def notResultsInCheck(x1, y1, x2, y2):
    global grid, validMovegen
    grid2 = []
    for i in range(8):
        grid2.append([])
        for j in range(8):
            grid2[i].append(grid[i][j])
    grid2[x2][y2] = grid[x1][y1]
    grid2[x1][y1] = 0

    white = grid2[x2][y2].isupper()
    kingX, kingY = None, None
    pos = []

    for i in range(8):
        for j in range(8):
            if white:
                if grid2[i][j] == "K":
                    kingX = i
                    kingY = j
            else:
                if grid2[i][j] == "k":
                    kingX = i
                    kingY = j
            if grid2[i][j] != 0:
                if white:
                    if grid2[i][j].islower():
                        pos.append([i, j])
                else:
                    if grid2[i][j].isupper():
                        pos.append([i, j])

    vMoves = []
    for i in range(len(pos)):
        vMoves.append(validMoveGen.generateValidMoves(pos[i][0], pos[i][1], grid2))

    for i in range(len(vMoves)):
        i1 = vMoves[i]
        for j in range(len(i1)):
            j1 = i1[j]
            if kingX == j1[0] and kingY == j1[1]:
                return False
    return True


# define Event object
class Event(object):
    def __init__(self):
        self.selected = False
        self.selectX = None
        self.selectY = None
        self.moveX = None
        self.moveY = None
        self.turn = 1

    def event(self, i, j):
        global grid, board
        if self.selected:
            self.moveX = i
            self.moveY = j
            if (
                (
                    self.selectX != None
                    and self.selectY != None
                    and self.moveX != None
                    and self.moveY != None
                )
                and self.selectX != self.moveX
                or self.selectY != self.moveY
            ):
                if notResultsInCheck(
                    self.selectX, self.selectY, self.moveX, self.moveY
                ):
                    self.move(self.selectX, self.selectY, self.moveX, self.moveY)
                else:
                    self.selectX = None
                    self.selectY = None
                    self.moveX = None
                    self.moveY = None
                board.colorBoard()
            else:
                self.selectX = None
                self.selectY = None
                self.moveX = None
                self.moveY = None
                board.resetColor()
            board.colorBoard()
            self.selected = False
        else:
            if grid[i][j] != 0 and self.turnCheck(i, j):
                self.selected = True
                self.selectX = i
                self.selectY = j
                board.colorValidMoves(self.selectX, self.selectY)
                board.colorBoard()
            else:
                self.selected = False
                self.selectX = None
                self.selectY = None

    def turnCheck(self, i, j):
        global grid
        if self.turn == 1:
            return grid[i][j] == 0 or grid[i][j].isupper()
        else:
            return grid[i][j] == 0 or grid[i][j].islower()

    def move(self, x1, y1, x2, y2):
        global grid, validMoves
        validMoveGen.generateValidMoves(x1, y1, grid)
        for i in range(len(validMoves)):
            if validMoves[i][0] == x2 and validMoves[i][1] == y2:
                grid[x2][y2] = grid[x1][y1]
                grid[x1][y1] = 0
                self.turn *= -1
                break
        board.placePieces()
        board.resetColor()


eventHandler = Event()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
        mouse = pygame.mouse.get_pos()
        for i in range(8):
            for j in range(8):
                if (
                    e.type == pygame.MOUSEBUTTONDOWN
                    and mouse[0] > board.sqs[i][j].left
                    and mouse[1] > board.sqs[i][j].top
                    and mouse[0] < board.sqs[i][j].right
                    and mouse[1] < board.sqs[i][j].bottom
                ):
                    eventHandler.event(i, j)
    board.colorBoard()
    board.placePieces()
    pygame.display.flip()

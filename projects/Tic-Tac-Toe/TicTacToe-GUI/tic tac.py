# importing the modules
import pygame, sys, time
from pygame.locals import *

# initializing the pygame window
pygame.init()
win = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("")
# pygame.mixer.music.load('AlanWalker3.mp3')        #This line
# pygame.mixer.music.play(-1,0.0)
# define all pygame related objects here
xImg = pygame.transform.scale(pygame.image.load("X.png"), (100, 100))
oImg = pygame.transform.scale(pygame.image.load("O.jpg"), (100, 100))
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 30, 1, 1)
text1 = font.render("Make your entry", 1, "BLUE")
text2 = font.render("Invalid  entry", 1, "BLUE")
text3 = font.render("Entry already exists", 1, "BLUE")
text4 = font.render("You won", 1, "BLUE")
text5 = font.render("Comp has won", 1, "BLUE")
text6 = font.render("The game has been a tie", 1, "BLUE")
# define all variables here
fps = 10
gameStage = 1
run = True
r1 = ["", "", ""]
r2 = ["", "", ""]
r3 = ["", "", ""]
r = []
# define all boolaean flags here
run = True
run1 = False
boardDraw = False
# define all functions here
def reDrawWindow():
    win.fill("WHITE")
    if gameStage == 1:
        firstFontDisplayer()
    if gameStage == 2:
        secondFontDisplayer()
    if boardDraw:
        boardReDraw()
    if gameStage == 3:
        entryDisplayer()

    pygame.display.update()


def firstFontDisplayer():
    font1 = pygame.font.SysFont("comicsans", 50, True)
    text1 = font1.render("Do you want to be ", True, "RED")
    text2 = font1.render("X", True, "RED")
    text3 = font1.render("O", True, "RED")
    pygame.draw.rect(win, "GREEN", (100, 150, 360, 40))
    pygame.draw.rect(win, "GREEN", (198, 250, 30, 30))
    pygame.draw.rect(win, "GREEN", (198, 300, 30, 30))
    win.blit(text1, (110, 160))
    win.blit(text2, (200, 250))
    win.blit(text3, (200, 300))


def cursorChecker(a, b):
    if (a[0] > b[0] and a[0] < b[0] + b[2]) and (a[1] > b[1] and a[1] < b[1] + b[3]):
        return True
    else:
        return False


def secondFontDisplayer():
    font2 = pygame.font.SysFont("comicsans", 30, True, True)
    text1 = font2.render("YOU PLAY FIRST", True, "BLUE")
    text2 = font2.render("COMPUER WILL PLAY FIRST", True, "BLUE")
    pygame.draw.rect(win, "GRAY", (110, 160, 190, 20))
    pygame.draw.rect(win, "GRAY", (110, 210, 320, 20))
    win.blit(text1, (110, 160))
    win.blit(text2, (110, 210))


def boardReDraw():
    pygame.draw.rect(win, "ORANGE", (100, 100, 300, 300))
    for col in range(100, 401, 100):
        pygame.draw.line(win, "FUCHSIA", (col, 100), (col, 400), 3)
    for row in range(100, 401, 100):
        pygame.draw.line(win, "FUCHSIA", (100, row), (400, row), 3)


def entryDisplayer():
    k = 100
    for i in r1:
        if i == "X":
            win.blit(xImg, (k, 100))
        elif i == "O":
            win.blit(oImg, (k, 100))
        k += 100
    k = 100
    for i in r2:
        if i == "X":
            win.blit(xImg, (k, 200))
        elif i == "O":
            win.blit(oImg, (k, 200))
        k += 100
    k = 100
    for i in r3:
        if i == "X":
            win.blit(xImg, (k, 300))
        elif i == "O":
            win.blit(oImg, (k, 300))
        k += 100
    pygame.display.update()


def gameCONCLUDER(a):
    if a == 1:
        reDrawWindow()
        win.blit(text4, (500, 100))
        time.sleep(2)
        pygame.quit()
        sys.exit()
    elif a == 0:
        print("got the call")
        reDrawWindow()
        win.blit(text5, (500, 100))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()


def tieChecker():
    reDrawWindow()
    win.blit(text6, (500, 100))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()


def player(a):
    reDrawWindow()
    if a not in range(1, 10):
        print("INVALID ENTRY")
        win.blit(text2, (450, 100))
        pygame.display.update()
        time.sleep(2)
        return firstinitialiser()
    if a in r:
        print("ENTRY ALREADY EXISTS")
        win.blit(text3, (450, 100))
        pygame.display.update()
        time.sleep(2)
        return firstinitialiser()
    if a == 1 and a not in r:
        r1[0] = m
    elif a == 2 and a not in r:
        r1[1] = m
    elif a == 3 and a not in r:
        r1[2] = m
    elif a == 4 and a not in r:
        r2[0] = m
    elif a == 5 and a not in r:
        r2[1] = m
    elif a == 6 and a not in r:
        r2[2] = m
    elif a == 7 and a not in r:
        r3[0] = m
    elif a == 8 and a not in r:
        r3[1] = m
    elif a == 9 and a not in r:
        r3[2] = m
    r.append(a)
    print(" | ".join(r1))
    print("_.", "_.", "_.")
    print(" | ".join(r2))
    print("_.", "_.", "_.")
    print(" | ".join(r3))
    if r1.count(m) == 3:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER(1)
    elif r2.count(m) == 3:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER(1)
    elif r3.count(m) == 3:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER(1)
    elif r1[0] == r2[0] == r3[0] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER(1)
    elif r1[1] == r2[1] == r3[1] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER(1)
    elif r1[2] == r2[2] == r3[2] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER()
    elif r1[0] == r2[1] == r3[2] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER(1)
    elif r1[2] == r2[1] == r3[0] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER(1)
    if (
        "" not in r1
        and "" not in r2
        and "" not in r3
        and len(r1) == len(r2) == len(r3) == 3
    ):
        print("The game has been a tie")
        return tieChecker()

    else:
        reDrawWindow()
        compPLAY()


def compPLAY():
    reDrawWindow()

    def compCOMPLETER(a):
        entryDisplayer()
        r.append(a)
        print("computers move is", a)
        print(" | ".join(r1))
        print("_.", "_.", "_.")
        print(" | ".join(r2))
        print("_.", "_.", "_.")
        print(" | ".join(r3))
        if r1.count(n) == 3:
            print("computer  HAS WON")
            return gameCONCLUDER(0)
        elif r2.count(n) == 3:
            print("computer  HAS WON")
            return gameCONCLUDER(0)
        elif r3.count(n) == 3:
            print("computer  HAS WON")
            return gameCONCLUDER(0)
        elif r1[0] == r2[0] == r3[0] == n:
            print("computer  HAS WON")
            return gameCONCLUDER(0)
        elif r1[1] == r2[1] == r3[1] == n:
            print("computer  HAS WON")
            return gameCONCLUDER(0)
        elif r1[2] == r2[2] == r3[2] == n:
            print("computer  HAS WON")
            return gameCONCLUDER(0)
        elif r1[0] == r2[1] == r3[2] == n:
            print("computer  HAS WON")
            return gameCONCLUDER(0)
        elif r1[2] == r2[1] == r3[0] == n:
            print("computer HAS WON")
            return gameCONCLUDER(0)
        if (
            "" not in r1
            and "" not in r2
            and "" not in r3
            and len(r1) == len(r2) == len(r3) == 3
        ):
            print("The game has been a tie")
            return tieChecker()
        else:
            reDrawWindow()
            firstinitialiser()

    def selfwinCHECKER():
        if r1.count(n) == 2:
            for i in range(len(r1)):
                if r1[i] == "":
                    r1[i] = n
                    print("selfwin has worked at r1")
                    compCOMPLETER(i + i)
        elif r2.count(n) == 2:
            for i in range(len(r2)):
                if r2[i] == "":
                    r2[i] = n
                    print("selfwin has worked at r2")
                    compCOMPLETER(i + 4)
        elif r3.count(n) == 2:
            for i in range(len(r3)):
                if r3[i] == "":
                    r3[i] = n
                    print("selfwin has worked at r3")
                    compCOMPLETER(i + 7)
        for i in range(3):
            o = [r1[i], r2[i], r3[i]]
            if o.count(n) == 2:
                for j in range(3):
                    if o[j] == "":
                        if j == 0:
                            r1[i] = n
                            print("selfwin has worked at", o[j])
                            compCOMPLETER(i + 1)
                        elif j == 1:
                            r2[i] = n
                            print("selfwin has worked at", o[j])
                            compCOMPLETER(i + 4)
                        elif j == 2:
                            r3[i] = n
                            print("selfwin has worked at", o[j])
                            compCOMPLETER(i + 7)
        d1 = [r1[0], r2[1], r3[2]]
        if d1.count(n) == 2:
            for i in range(3):
                if d1[i] == "":
                    if i == 0:
                        r1[0] = n
                        print("d1 is", d1, "but r1[0] is", r1[0], "but your i is", i)

                        print("selfwin has worked at my doubt")
                        compCOMPLETER(1)
                    elif i == 1:
                        r2[1] = n
                        print("selfwin has worked")
                        compCOMPLETER(5)
                    elif i == 2:
                        r3[2] = n
                        print("selfwin has worked")
                        compCOMPLETER(9)
        d2 = [r1[2], r2[1], r3[0]]
        if d2.count(n) == 2:
            for i in range(3):
                if d2[i] == "":
                    if i == 0:
                        r1[2] = n
                        print("selfwin has worked")
                        compCOMPLETER(3)
                    elif i == 1:
                        r2[1] = n
                        print("selfwin has worked")
                        compCOMPLETER(5)
                    elif i == 2:
                        r3[0] = n
                        print("selfwin has worked")
                        compCOMPLETER(7)

    selfwinCHECKER()

    def oppwinCHECKER():
        if r1.count(m) == 2:
            for i in range(len(r1)):
                if r1[i] == "":
                    r1[i] = n
                    print("oppwin has worked at r1")
                    compCOMPLETER(i + 1)

        elif r2.count(m) == 2:
            for i in range(len(r2)):

                if r2[i] == "":
                    print("r2 is ", r2)
                    r2[i] = n
                    print("oppwin has worked at r2")
                    compCOMPLETER(i + 4)

        elif r3.count(m) == 2:
            for i in range(len(r3)):
                if r3[i] == "":
                    r3[i] = n
                    print("oppwin has worked at r3")
                    compCOMPLETER(i + 7)
        for i in range(3):
            o = [r1[i], r2[i], r3[i]]
            if o.count(m) == 2:
                for j in range(3):
                    if o[j] == "":
                        if j == 0:
                            r1[i] = n
                            print("oppwin has worked at ", o[j])
                            compCOMPLETER(i + 1)
                        elif j == 1:
                            r2[i] = n
                            print("oppwin has worked at", o[j])
                            compCOMPLETER(i + 4)
                        elif j == 2:
                            r3[i] = n
                            print("oppwin has worked at", o[j])
                            compCOMPLETER(i + 7)
        d1 = [r1[0], r2[1], r3[2]]
        if d1.count(m) == 2:
            for i in range(3):
                if d1[i] == "":
                    if i == 0:
                        r1[0] = n
                        print("oppwin has worked")
                        compCOMPLETER(i + 1)
                    elif i == 1:
                        r2[1] = n
                        print("oppwin has worked")
                        compCOMPLETER(i + 4)
                    elif i == 2:
                        r3[2] = n
                        print("oppwin has worked")
                        compCOMPLETER(i + 7)
        d2 = [r1[2], r2[1], r3[0]]
        if d2.count(m) == 2:
            for i in range(3):
                if d2[i] == "":
                    if i == 0:
                        r1[2] = n
                        print("oppwin has worked")
                        compCOMPLETER(3)
                    elif i == 1:
                        r2[1] = n
                        print("oppwin has worked")
                        compCOMPLETER(5)
                    elif i == 2:
                        r3[0] = n
                        print("oppwin has worked")
                        compCOMPLETER(7)

    oppwinCHECKER()

    def middleCHECKER():
        if r2[1] == "":
            r2[1] = n
            print("miidlechecker has worked")
            compCOMPLETER(5)

    middleCHECKER()

    def endsideCHECKER():
        if r1[0] == "":
            r1[0] = n
            print("endsidechecker has worked")
            compCOMPLETER(1)
        elif r1[2] == "":
            r1[2] = n
            print("endsidechecker has worked")
            compCOMPLETER(3)
        elif r3[0] == "":
            r3[0] = n
            print("endsidechecker has worked")
            compCOMPLETER(7)
        elif r3[2] == "":
            r3[2] = n
            print("endsidechecker has worked")
            compCOMPLETER(9)

    endsideCHECKER()

    def endmiddleCHECKER():

        if r1[1] == "":
            r1[1] = n
            print("endmiddlechecker has worked")
            compCOMPLETER(2)
        elif r2[0] == "":
            r2[0] = n
            compCOMPLETER(4)
            print("endmiddlechecker has worked")
        elif r2[2] == "":
            r2[2] = n
            p = 6
            print("endmiddlechecker has worked")
            compCOMPLETER(6)
        elif r3[1] == "":
            r3[1] = n
            print("endmiddlechecker has worked")
            compCOMPLETER(8)

    endmiddleCHECKER()


def firstinitialiser():
    reDrawWindow()
    q = True
    while q:
        win.blit(text1, (450, 100))
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
                if cursorChecker((mx, my), (100, 100, 100, 100)):
                    print(1)
                    q = False
                    player(1)

                if cursorChecker((mx, my), (200, 100, 100, 100)):
                    print(2)
                    q = False
                    player(2)

                if cursorChecker((mx, my), (300, 100, 100, 100)):
                    print(3)
                    q = False
                    player(3)
                if cursorChecker((mx, my), (100, 200, 100, 100)):
                    print(4)
                    q = False
                    player(4)

                if cursorChecker((mx, my), (200, 200, 100, 100)):
                    print(5)
                    q = False
                    player(5)

                if cursorChecker((mx, my), (300, 200, 100, 100)):
                    print(6)
                    q = False
                    player(6)

                if cursorChecker((mx, my), (100, 300, 100, 100)):
                    print(7)
                    q = False
                    player(7)

                if cursorChecker((mx, my), (200, 300, 100, 100)):
                    print(8)
                    q = False
                    player(8)

                if cursorChecker((mx, my), (300, 300, 100, 100)):
                    print(9)
                    q = False
                    player(9)
            pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            # sys.exit
        if event.type == MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if gameStage == 1:
                if cursorChecker((mx, my), (198, 250, 30, 30)):
                    print("you clicked X")
                    gameStage += 1
                    m = "X"
                    n = "O"
                if cursorChecker((mx, my), (198, 300, 30, 30)):
                    print("you clicked on O")
                    gameStage += 1
                    m = "O"
                    n = "X"
            elif gameStage == 2:
                mx, my = pygame.mouse.get_pos()
                if cursorChecker((mx, my), ((110, 160, 190, 20))):
                    print("you will play first")
                    firstPlay = 0
                    gameStage += 1
                    run1 = True
                elif cursorChecker((mx, my), (110, 210, 320, 20)):
                    print("computer will play first")
                    firstPlay = 1
                    gameStage += 1
                    run1 = True

            if run1:
                if firstPlay == 0:
                    run1 = False
                    boardDraw = True
                    time.sleep(2)
                    reDrawWindow()
                    firstinitialiser()

                elif firstPlay == 1:
                    boardDraw = True
                    time.sleep(2)
                    run1 = False
                    compPLAY()
        reDrawWindow()

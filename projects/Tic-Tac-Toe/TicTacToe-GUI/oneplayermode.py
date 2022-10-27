# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 09:48:54 2018

@author: om
"""
import sys

print("Welcome to the two player mode of tictactoe")
print("press 1 be O and 2 to be X")
m = int(input("enter here"))
if m == 1:
    m = "O"
    n = "X"
elif m == 2:
    m = "X"
    n = "O"
c = []
r1 = ["", "", ""]
r2 = ["", "", ""]
r3 = ["", "", ""]
r = []


def gameCONCLUDER():
    a = int(input("Enter 1 to terminate the game"))
    if a == 1:
        sys.exit()


def firstinitialiser():
    global n1
    n1 = int(input("PLAYER1 TURN (1-9)"))
    tictactoe(n1)


def tictactoe(a):
    if a not in range(1, 10):
        print("INVALID ENTRY")
        return firstinitialiser()
    if a in r:
        print("ENTRY ALREADY EXISTS")
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
    r.append(n1)
    print(" | ".join(r1))
    print("_.", "_.", "_.")
    print(" | ".join(r2))
    print("_.", "_.", "_.")
    print(" | ".join(r3))
    if r1.count(m) == 3:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER()
    elif r2.count(m) == 3:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER()
    elif r3.count(m) == 3:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER()
    elif r1[0] == r2[0] == r3[0] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER()
    elif r1[1] == r2[1] == r3[1] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER()
    elif r1[2] == r2[2] == r3[2] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER()
    elif r1[0] == r2[1] == r3[2] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER()
    elif r1[2] == r2[1] == r3[0] == m:
        print("PLAYER1 HAS WON")
        return gameCONCLUDER()
    if (
        "" not in r1
        and "" not in r2
        and "" not in r3
        and len(r1) == len(r2) == len(r3) == 3
    ):
        print("The game has been a tie")
    else:
        compPLAY()


def compPLAY():
    def compCOMPLETER(a):
        r.append(a)
        print("computers move is", a)
        print(" | ".join(r1))
        print("_.", "_.", "_.")
        print(" | ".join(r2))
        print("_.", "_.", "_.")
        print(" | ".join(r3))
        if r1.count(n) == 3:
            print("computer  HAS WON")
            return gameCONCLUDER()
        elif r2.count(n) == 3:
            print("computer  HAS WON")
            return gameCONCLUDER()
        elif r3.count(n) == 3:
            print("computer  HAS WON")
            return gameCONCLUDER()
        elif r1[0] == r2[0] == r3[0] == n:
            print("computer  HAS WON")
            return gameCONCLUDER()
        elif r1[1] == r2[1] == r3[1] == n:
            print("computer  HAS WON")
            return gameCONCLUDER()
        elif r1[2] == r2[2] == r3[2] == n:
            print("computer  HAS WON")
            return gameCONCLUDER()
        elif r1[0] == r2[1] == r3[2] == n:
            print("computer  HAS WON")
            return gameCONCLUDER()
        elif r1[2] == r2[1] == r3[0] == n:
            print("computer HAS WON")
            return gameCONCLUDER()
        if (
            "" not in r1
            and "" not in r2
            and "" not in r3
            and len(r1) == len(r2) == len(r3) == 3
        ):
            print("The game has been a tie")
            return gameCONCLUDER()
        else:
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

    def strategy1():
        if r1[0] == "" and r3[2] == "" or c != []:
            if r1[0] == "":
                r1[0] = n
                print("strategy 1 has worked")
                c.append(1)
                compCOMPLETER(1)
            if r1[0] == n and r3[2] == n:
                if r1[2] == "":
                    r1[2] = n
                    compCOMPLETER(3)
                elif r3[0] == "":
                    r3[0] = n
                    compCOMPLETER(7)
            elif r3[2] == "":
                r3[2] = n
                print("strategy1 has worked")
                c.append(1)
                compCOMPLETER(9)

    strategy1()

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


print("press 1 to play first , press 2 to let computer play first")
global a
a = int(input("enter here "))
if a == 1:
    firstinitialiser()
elif a == 2:
    compPLAY()

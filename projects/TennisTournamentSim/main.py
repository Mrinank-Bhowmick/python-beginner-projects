# ---------RATING OF PROGRAM READABILITY AND EFFICIENCY--------- #
#                      Absolute Dog Water                        #


# Imports
import random
import time

# Records time in the beginning
start = time.time()

if __name__ == "__main__":
    print("Program Starts from here")

# Constant Strings because they are used a lot
BRWINNERNAMESTR = "Bracket Winner Name: "
WINNINGSCHOOLSTR = ", Winning School Name: "
WINNERSKILLSTR = ", Winner Skill: "
WINNUM = ", Wins: "

BRLOSERNAMESTR = "Bracket Loser Name: "
LOSINGSCHOOLSTR = ", Losing School Name: "
LOSERSKILLSTR = ", Loser Skill: "
LOSSNUMSTR = ", Losses: "

CHAMPNAMESTR = "Champion Name: "
CHAMPSCHOOLSTR = ", Champion School: "
CHAMPSKILLSTR = ", Champion Skill: "

RUNUPNAMESTR = "Runner Up Name: "
RUNUPSCHOOLSTR = ", Running Up School: "
RUNUPSKILLSTR = ", Runner Up Skill: "

# Player Class Objects Random Identity Lists
random_first_names = ["Max", "Corey", "Evander", "Timothy"]
random_last_names = ["Kenshin", "Holyfield", "Roosevelt", "Wong"]
random_school = ["Newport", "Sammamish", "Inglemore", "Eastlake"]


def first_name_picker():
    global random_first_names
    first_name = random.choice(random_first_names)
    random_first_names.remove(first_name)  # Removes picked random name
    return first_name


def last_name_picker():
    global random_last_names
    last_name = random.choice(random_last_names)
    random_last_names.remove(last_name)
    return last_name


def school_name_picker():
    global random_school
    school_name = random.choice(random_school)
    random_school.remove(school_name)
    return school_name


class Player:
    def __init__(self, first, last, skill, school, win, loss):  # Constructor
        self.first = first
        self.last = last
        self.skill = skill
        self.school = school
        self.win = win
        self.loss = loss


# Looks like Shit
p1 = Player(
    first_name_picker(),
    last_name_picker(),
    random.randint(1, 6),
    school_name_picker(),
    0,
    0,
)
p2 = Player(
    first_name_picker(),
    last_name_picker(),
    random.randint(1, 6),
    school_name_picker(),
    0,
    0,
)
p3 = Player(
    first_name_picker(),
    last_name_picker(),
    random.randint(1, 6),
    school_name_picker(),
    0,
    0,
)
p4 = Player(
    first_name_picker(),
    last_name_picker(),
    random.randint(1, 6),
    school_name_picker(),
    0,
    0,
)


# Smooth Brain Moment
def bracket_results(player1, player2):
    rngskillinc1 = random.random()  # Random Rng Increase to skill level (happens IRL)
    rngskilldec1 = random.random()  # Random Rng Decrease to skill level (happens IRL)
    rngskill1 = rngskillinc1 - rngskilldec1  # Total Rng Skill Increase or Decrease

    rngskillinc2 = random.random()
    rngskilldec2 = random.random()
    rngskill2 = rngskillinc2 - rngskilldec2

    if (player1.skill * rngskill1) + player1.skill > (
        player2.skill * rngskill2
    ) + player2.skill:
        player1.skill = player1.skill + 0.5
        player1.win += 1
        player2.loss += 1
    elif (player1.skill * rngskill1) + player1.skill < (
        player2.skill * rngskill2
    ) + player2.skill:
        player2.skill = player2.skill + 0.5
        player2.win += 1
        player1.loss += 1
    elif (player1.skill * rngskill1) + player1.skill == (
        player2.skill * rngskill2
    ) + player2.skill:
        choice = random.randint(0, 2)
        if choice == 1:
            player1.skill = player1.skill + 0.5
            player1.win += 1
            player2.loss += 1

        else:
            player2.skill = player2.skill + 0.5
            player2.win += 1
            player1.loss += 1

    return player1.win, player1.loss, player2.win, player2.loss


# Bracket 1 Round 1
bracket_results(p1, p2)
print(
    f"""Player's info - Bracket 1, Round 1
Player 1 
Name: {p1.first} {p1.last}, School: {p1.school}

Player 2
Name: {p2.first} {p2.last}, School: {p2.school}
"""
)
if p1.win > p2.win:
    winnerbr1r1 = p1
    loserbr1r1 = p2
    print(
        BRWINNERNAMESTR + winnerbr1r1.first,
        winnerbr1r1.last
        + WINNINGSCHOOLSTR
        + winnerbr1r1.school
        + WINNERSKILLSTR
        + str(winnerbr1r1.skill)
        + WINNUM
        + str(winnerbr1r1.win),
    )
    print(
        BRLOSERNAMESTR + loserbr1r1.first,
        loserbr1r1.last
        + LOSINGSCHOOLSTR
        + loserbr1r1.school
        + LOSERSKILLSTR
        + str(loserbr1r1.skill)
        + LOSSNUMSTR
        + str(loserbr1r1.loss),
    )
elif p1.win < p2.win:
    winnerbr1r1 = p2
    loserbr1r1 = p1
    print(
        BRWINNERNAMESTR + winnerbr1r1.first,
        winnerbr1r1.last
        + WINNINGSCHOOLSTR
        + winnerbr1r1.school
        + WINNERSKILLSTR
        + str(winnerbr1r1.skill)
        + WINNUM
        + str(winnerbr1r1.win),
    )
    print(
        BRLOSERNAMESTR + loserbr1r1.first,
        loserbr1r1.last
        + LOSINGSCHOOLSTR
        + loserbr1r1.school
        + LOSERSKILLSTR
        + str(loserbr1r1.skill)
        + LOSSNUMSTR
        + str(loserbr1r1.loss),
    )

# Bracket 2 Round 1
bracket_results(p3, p4)
print(
    f"""
-------------------------------------

Player's info - Bracket 2, Round 1
Player 3 
Name: {p3.first} {p3.last}, School: {p3.school}

Player 4
Name: {p4.first} {p4.last}, School: {p4.school}
"""
)
if p3.win > p4.win:
    winnerbr2r1 = p3
    loserbr2r1 = p4
    print(
        BRWINNERNAMESTR + winnerbr2r1.first,
        winnerbr2r1.last
        + WINNINGSCHOOLSTR
        + winnerbr2r1.school
        + WINNERSKILLSTR
        + str(winnerbr2r1.skill)
        + WINNUM
        + str(winnerbr2r1.win),
    )
    print(
        BRLOSERNAMESTR + loserbr2r1.first,
        loserbr2r1.last
        + LOSINGSCHOOLSTR
        + loserbr2r1.school
        + LOSERSKILLSTR
        + str(loserbr2r1.skill)
        + LOSSNUMSTR
        + str(loserbr2r1.loss),
    )
elif p3.win < p4.win:
    winnerbr2r1 = p4
    loserbr2r1 = p3
    print(
        BRWINNERNAMESTR + winnerbr2r1.first,
        winnerbr2r1.last
        + WINNINGSCHOOLSTR
        + winnerbr2r1.school
        + WINNERSKILLSTR
        + str(winnerbr2r1.skill)
        + WINNUM
        + str(winnerbr2r1.win),
    )
    print(
        BRLOSERNAMESTR + loserbr2r1.first,
        loserbr2r1.last
        + LOSINGSCHOOLSTR
        + loserbr2r1.school
        + LOSERSKILLSTR
        + str(loserbr2r1.skill)
        + LOSSNUMSTR
        + str(loserbr2r1.loss),
    )

# Finals
# Note - Long -- Why? =-=-=-= Because I love using ;
# Looks - Looks like Minecraft
if p1.win == p3.win:
    print(
        f"""
#####################################

Player's info - Finals
Player 1 
Name: {p1.first} {p1.last}, School: {p1.school} 

Player 3
Name: {p3.first} {p3.last}, School: {p3.school}
    """
    )
    bracket_results(p1, p3)
    if p1.win > p3.win:
        champ = p1
        runup = p3
        print(
            CHAMPNAMESTR + champ.first,
            champ.last + CHAMPSCHOOLSTR + champ.school,
            CHAMPSKILLSTR + str(champ.skill),
        )
        print(
            RUNUPNAMESTR + runup.first,
            runup.last + RUNUPSCHOOLSTR + runup.school,
            RUNUPSKILLSTR + str(runup.skill),
        )
    elif p3.win > p1.win:
        champ = p3
        runup = p1
        print(
            CHAMPNAMESTR + champ.first,
            champ.last + CHAMPSCHOOLSTR + champ.school,
            CHAMPSKILLSTR + str(champ.skill),
        )
        print(
            RUNUPNAMESTR + runup.first,
            runup.last + RUNUPSCHOOLSTR + runup.school,
            RUNUPSKILLSTR + str(runup.skill),
        )
elif p1.win == p4.win:
    print(
        f"""
#####################################
    
Player's info - Finals
Player 1 
Name: {p1.first} {p1.last}, School: {p1.school}

Player 4
Name: {p4.first} {p4.last}, School: {p4.school}
    """
    )
    bracket_results(p1, p4)
    if p1.win > p4.win:
        champ = p1
        runup = p4
        print(
            CHAMPNAMESTR + champ.first,
            champ.last + CHAMPSCHOOLSTR + champ.school,
            CHAMPSKILLSTR + str(champ.skill),
        )
        print(
            RUNUPNAMESTR + runup.first,
            runup.last + RUNUPSCHOOLSTR + runup.school,
            RUNUPSKILLSTR + str(runup.skill),
        )
    elif p4.win > p1.win:
        champ = p4
        runup = p1
        print(
            CHAMPNAMESTR + champ.first,
            champ.last + CHAMPSCHOOLSTR + champ.school,
            CHAMPSKILLSTR + str(champ.skill),
        )
        print(
            RUNUPNAMESTR + runup.first,
            runup.last + RUNUPSCHOOLSTR + runup.school,
            RUNUPSKILLSTR + str(runup.skill),
        )
elif p2.win == p3.win:
    print(
        f"""
#####################################

Player's info - Finals
Player 2 
Name: {p2.first} {p2.last}, School: {p2.school}

Player 3
Name: {p3.first} {p3.last}, School: {p3.school}
    """
    )
    bracket_results(p2, p3)
    if p2.win > p3.win:
        champ = p2
        runup = p3
        print(
            CHAMPNAMESTR + champ.first,
            champ.last + CHAMPSCHOOLSTR + champ.school,
            CHAMPSKILLSTR + str(champ.skill),
        )
        print(
            RUNUPNAMESTR + runup.first,
            runup.last + RUNUPSCHOOLSTR + runup.school,
            RUNUPSKILLSTR + str(runup.skill),
        )
    elif p3.win > p2.win:
        champ = p3
        runup = p2
        print(
            CHAMPNAMESTR + champ.first,
            champ.last + CHAMPSCHOOLSTR + champ.school,
            CHAMPSKILLSTR + str(champ.skill),
        )
        print(
            RUNUPNAMESTR + runup.first,
            runup.last + RUNUPSCHOOLSTR + runup.school,
            RUNUPSKILLSTR + str(runup.skill),
        )
elif p2.win == p4.win:
    print(
        f"""
#####################################

Player's info - Finals
Player 2 
Name: {p2.first} {p2.last}, School: {p2.school}

Player 4
Name: {p4.first} {p4.last}, School: {p4.school}
    """
    )
    bracket_results(p2, p4)
    if p2.win > p4.win:
        champ = p2
        runup = p4
        print(
            CHAMPNAMESTR + champ.first,
            champ.last + CHAMPSCHOOLSTR + champ.school,
            CHAMPSKILLSTR + str(champ.skill),
        )
        print(
            RUNUPNAMESTR + runup.first,
            runup.last + RUNUPSCHOOLSTR + runup.school,
            RUNUPSKILLSTR + str(runup.skill),
        )
    elif p4.win > p2.win:
        champ = p4
        runup = p2
        print(
            CHAMPNAMESTR + champ.first,
            champ.last + CHAMPSCHOOLSTR + champ.school,
            CHAMPSKILLSTR + str(champ.skill),
        )
        print(
            RUNUPNAMESTR + runup.first,
            runup.last + RUNUPSCHOOLSTR + runup.school,
            RUNUPSKILLSTR + str(runup.skill),
        )

# Record end time
end = time.time()

# print the difference between start
# and end time in milli. secs
print("\n")
print("The time of execution of above program is:", (end - start) * 10**3, "ms")

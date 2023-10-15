import random
print("Welcome to Word Guessing Game!")
print("Rule:\n \
    You will be given a word with some blank space.\n \
    Guess the letter in it, type the letter and press enter.\n \
    Include space between two answers. Example: a m.\n \
    If you give correct answer you will get 1 point.\n \
    Otherwise you will loss.\n")
word = ["red", "scarlet", "crimson", "ruby", "cherry", "vermilion", "blue", "azure", "navy", "cobalt", "sapphire", "cerulean", "green", "emerald", "jade", "olive", "lime", "forest", "yellow", "gold", "lemon", "amber", "canary", "sunflower", "orange", "tangerine", "apricot", "peach", "coral", "carrot", "purple", "lavender", "violet", "mauve", "plum", "indigo", "pink", "rose", "salmon", "blush", "bubblegum", "fuchsia", "brown", "chocolate", "chestnut", "caramel", "coffee", "mahogany", "gray", "silver", "charcoal", "slate", "ash", "pewter", "black", "onyx", "ebony", "jet", "charcoal", "midnight", "white", "ivory", "snow", "pearl", "cream", "chalk", "beige", "sand", "tan", "camel", "khaki", "buff",
        "pizza", "sushi", "chocolate", "tacos", "spaghetti", "avocado", "pancakes", "broccoli", "hamburger", "ice cream",
        "paris", "tokyo", "new york", "london", "sydney", "rome", "cairo", "mumbai", "rio de janeiro", "barcelona",
        "apple", "nike", "coca-cola", "google", "microsoft", "amazon", "mcdonald's", "disney", "bmw", "samsung"
        ]

point = 0
max_point = 0

while True:
    random.shuffle(word)
    targeted_word = random.choice(word)
    # random position of two letter
    a = random.randint(0, len(targeted_word) - 1)
    b = random.randint(0, len(targeted_word) - 1)
    
    # make a less then b
    if a > b:
        temp = a
        a = b
        b = temp
    # pre store answer to check letter
    x = targeted_word[a]
    y = targeted_word[b]

    print("Word: ", targeted_word[:a] + '_' + targeted_word[a + 1: b] + '_' + targeted_word[b+1:])
    ipt = list(input("Letters: ").strip())
    x1 = ipt[0]
    y1 = ipt[1]
    if x == x1 and y == y1:
        print("FULL Currect Answer!\nPoint = ", f"{point} + 2 = {point + 2}")
        point += 2
    elif x == x1:
        print("1 Currect Answer!\nPoint = ", f"{point} + 1 = {point + 1}")
        point += 1
    elif y == y1:
        print("1 Currect Answer!\nPoint = ", f"{point} + 1 = {point + 1}")
        point += 1
    else:
        max_point = max(max_point, point)
        print("Wrong Answer!\n Max Score = ", max_point)
        play_again = input("Press 1 to play again or 0 to exit: ")
        if play_again == '0':
            break

import requests
import time

tellajoke = True

category = "Any"
lang = "eng"
while tellajoke:
    ans = str(
        input("\n\nDo you want to read a joke?(y => yes; n => exit; s=> settings): ")
    )

    if ans == "y":
        x = requests.get("https://v2.jokeapi.dev/joke/" + category + "?lang=" + lang)
        x = x.json()

        if "joke" in x:
            print("\n" + x["joke"])
        else:
            print("\n" + x["setup"])
            print("...")
            time.sleep(1)
            print(x["delivery"])
    elif ans == "s":
        s_ans = str(
            input(
                "Which settings would you like to edit? (c => category, l => language): "
            )
        )
        if s_ans == "c":
            print("Current selected category: " + category + "\n")
            c_ans = str(
                input(
                    "Selectable categories:\n a => Any\n p => Programming\n m => Misc\n d => dark\n s => "
                    "Spooky\n c => Christmas\n > "
                )
            )
            if c_ans == "p":
                category = "Programming"
            elif c_ans == "m":
                category = "Misc"
            elif c_ans == "d":
                category = "Dark"
            elif c_ans == "s":
                category = "Spooky"
            elif c_ans == "c":
                category = "Christmas"
            elif c_ans == "a":
                category = "Any"
            print("Category " + category + " set!")
        elif s_ans == "l":
            print("Current selected language: " + lang)
            l_ans = str(
                input(
                    "Selectable languages:\n en => English\n cs => Czech\n de => German\n es => Spanish\n fr => "
                    "French\n pt => Portuguese\n > "
                )
            )
            if l_ans in ["en", "cs", "de", "es", "fr", "pt"]:
                lang = l_ans
                print("Language " + lang + " set!\n")

    else:
        tellajoke = False

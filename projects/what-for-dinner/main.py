import requests


def main():
    r = requests.get("http://themealdb.com/api/json/v1/1/random.php")
    meal_detail = dict(r.json())["meals"][0]

    # TODO information from menu
    menu_name = meal_detail["strMeal"]
    menu_category = meal_detail["strCategory"]
    menu_tags = meal_detail["strTags"]
    menu_country = meal_detail["strArea"]
    menu_instruction = meal_detail["strInstructions"]
    menu_video = meal_detail["strYoutube"]

    # TODO for coloring output
    class bcolors:
        HEADER = "\033[95m"
        OKBLUE = "\033[94m"
        OKCYAN = "\033[96m"
        OKGREEN = "\033[92m"
        WARNING = "\033[93m"
        FAIL = "\033[91m"
        ENDC = "\033[0m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"

    print(f"-------------------------------------------------------------")
    print(f"Let's have a {bcolors.BOLD}{menu_name}{bcolors.ENDC} for the dinner!")
    print(f"this menu is {menu_country} and it is {menu_category}!")
    print(
        f"you can follow this link: {bcolors.OKBLUE}{menu_video}{bcolors.ENDC} or instruction to cook it: \n{menu_instruction}"
    )
    print(f"-------------------------------------------------------------")


if __name__ == "__main__":
    main()

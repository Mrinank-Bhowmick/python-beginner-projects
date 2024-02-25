import requests  # Import the 'requests' library for making HTTP requests.


def main():
    menu_detail = dict(
        requests.get("http://themealdb.com/api/json/v1/1/random.php").json()
    )["meals"][
        0
    ]  # Extract the details of the first meal from the API response.

    # TODO: Get information from the menu
    menu_name = menu_detail[
        "strMeal"
    ]  # Extract the name of the meal from the meal detail.
    menu_category = menu_detail[
        "strCategory"
    ]  # Extract the category of the meal from the meal detail.
    menu_tags = menu_detail[
        "strTags"
    ]  # Extract the tags (if available) of the meal from the meal detail.
    menu_country = menu_detail[
        "strArea"
    ]  # Extract the country of the meal from the meal detail.
    menu_instruction = menu_detail[
        "strInstructions"
    ]  # Extract the cooking instructions of the meal.
    menu_video = menu_detail[
        "strYoutube"
    ]  # Extract the YouTube video link for the meal (if available).

    # TODO: Define color codes for printing colored output.
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

    # Print the information about the meal in a stylized format.
    print(f"-------------------------------------------------------------")
    print(f"Let's have a {bcolors.BOLD}{menu_name}{bcolors.ENDC} for dinner!")
    print(f"This menu is {menu_country} and it is {menu_category}!")
    print(
        f"You can follow this link: {bcolors.OKBLUE}{menu_video}{bcolors.ENDC} or the instructions to cook it:\n{menu_instruction}"
    )
    print(f"-------------------------------------------------------------")


if __name__ == "__main__":
    main()  # Call the main function when the script is executed as the main program.

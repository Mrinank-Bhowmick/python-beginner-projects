import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
from matplotlib import pyplot as plt
import uuid


def main():
    # This gets a dictionary that contains all the links to the team's World Cup Stats Page
    def get_team_data_links():
        url = "https://fbref.com/en/comps/1/stats/World-Cup-Stats"
        info = requests.get(url).text

        # Parsing World Cup Links into a data frame
        soup = BeautifulSoup(info, "html.parser")
        table = soup.find("table", id="stats_squads_standard_for")
        table_body = table.find("tbody")
        data = []
        rows = table_body.find_all("th")

        team_data_link = {}

        for row in rows:
            line = str(row)
            href_line = line[line.find("href=") :]
            team_url = (
                "https://fbref.com"
                + href_line[href_line.find("/") : href_line.find('">')]
            )
            team_name = href_line[href_line.find('">') : href_line.find("</a")][2:]
            team_data_link[team_name] = team_url

        return team_data_link

    # This gets all the stats for a specific team and puts it into a dataframe
    def get_team_stats(url):
        info = requests.get(url).text

        soup = BeautifulSoup(info, "html.parser")
        table = soup.find("table", id="stats_standard_1")
        table_body = table.find("tbody")

        data = []
        rows = table_body.find_all("tr")
        for row in rows:
            player_name = str(row.find_all("th"))
            player_name = player_name.split()
            res = player_name[3][:-1] + " " + player_name[2][5:]
            cols = row.find_all("td")

            cols = [i.text.strip() for i in cols]
            cols.insert(0, res)
            data.append([i for i in cols if i])
        df_table = pd.DataFrame(data)

        df_table = df_table[[0, 1, 2, 3, 4, 5, 6, 7, 8]]
        df_table = df_table.rename(
            columns={
                0: "Player",
                1: "Pos",
                2: "Age",
                3: "MP",
                4: "Starts",
                5: "Min",
                6: "90s",
                7: "Goals",
                8: "Ast",
            }
        )

        return df_table

    # gets all of the url's for the World Cup teams and put's it into a dictionary
    # where the key is the
    team_data_link = get_team_data_links()

    first_link = ""
    first_player = ""
    second_link = ""
    second_player = ""

    first_country = input("Please type country name for first player: ")
    try:
        first_link = team_data_link[first_country]

        first_player = input(f"Please type name of player from {first_country}: ")
    except Exception as e:
        print("Sorry that is not a valid country name, please re-run program ")

    second_country = input("Please type country name for second player: ")

    try:
        second_link = team_data_link[second_country]
        second_player = input(f"Please type name of player from {second_country}: ")
    except Exception as e:
        print("Sorry that is not a valid country name, please re-run program ")

    # gets the the team stats for the first team and second team and also cleans up
    # the data a bit

    first_df = get_team_stats(first_link)
    second_df = get_team_stats(second_link)

    first_df = first_df.fillna(value=np.nan)
    first_df["Goals"] = first_df["Goals"].replace(np.nan, 0)
    first_df["Ast"] = first_df["Ast"].replace(np.nan, 0)
    second_df = second_df.fillna(value=np.nan)
    second_df["Goals"] = second_df["Goals"].replace(np.nan, 0)
    second_df["Ast"] = second_df["Ast"].replace(np.nan, 0)

    # checking to see if first player or second are not in each data frame, if so then
    # exit program
    if first_player not in list(first_df["Player"]):
        print(f"{first_player} was not found on the {first_country}, please try again")
        exit()

    if second_player not in list(second_df["Player"]):
        print(
            f"{second_player} was not found on the {second_country}, please try again"
        )
        exit()

    # plotting data
    name_and_country_1 = f"{first_player} ({first_country})"
    name_and_country_2 = f"{second_player} ({second_country})"
    x_axis = [name_and_country_1, name_and_country_2]
    y_axis = []

    for name, goals, assists in zip(
        first_df["Player"], first_df["Goals"], first_df["Ast"]
    ):
        total_ga = 0
        if name == first_player:
            total_ga = int(goals) + int(assists)
            y_axis.append(total_ga)

    for name, goals, assists in zip(
        second_df["Player"], second_df["Goals"], second_df["Ast"]
    ):
        total_ga = 0
        if name == second_player:
            total_ga = int(goals) + int(assists)
            y_axis.append(total_ga)

    # plotting data and saving it to a file

    plt.style.use("ggplot")
    plt.figure(figsize=(7, 7))
    plt.bar(x_axis, y_axis, color="navy")
    plt.title("2022 World Cup Player G/A Comparison")
    plt.xlabel("Names")
    plt.ylabel("Number of Goals and Assists")

    file_name = f"{first_player}_{second_player}_comparison_{str(uuid.uuid4().hex)}"
    plt.savefig(f"Results/{file_name}")


if __name__ == "__main__":
    main()

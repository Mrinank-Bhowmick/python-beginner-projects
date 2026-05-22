# World Cup Player Comparison

Scrapes 2022 World Cup team statistics from fbref.com, lets you pick two players from two countries, and saves a bar chart comparing their combined goals and assists.

## Example

```text
Please type country name for first player: France
Please type name of player from France: Kylian Mbappe
Please type country name for second player: Argentina
Please type name of player from Argentina: Lionel Messi
```

A bar chart titled "2022 World Cup Player G/A Comparison" is generated comparing the two players' combined goals and assists, and saved as a PNG file in the `Results/` folder.

## How to run on localhost

```bash
pip install pandas requests beautifulsoup4 numpy matplotlib
python main.py
```

## Dependencies

- pandas
- requests
- beautifulsoup4
- numpy
- matplotlib

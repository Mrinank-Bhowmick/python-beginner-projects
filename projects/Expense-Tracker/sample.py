from pathlib import Path
import os

from app import App
from item import ItemsDB, Item, Category

DB_PATH = str(Path(__file__).resolve().parent / "items.json")


def mock_add_items():
    items = [
        Item.create_income_item(
            "Bitcoin",
            500,
            "Income from Bitcoin",
            "2023-06-25",
            Category("Personal Finance", "Investing"),
        ),
        Item.create_income_item(
            "Youtube Ads",
            5,
            "Income from Youtube Ads",
            "2024-1-10",
            Category("Youtube"),
        ),
        Item.create_income_item("Gift", 30, "Gift from Relatives", "2024-03-04"),
        Item.create_expense_item(
            "Pizza", 50, "Pizza from Pizza Hut", "2023-04-20", Category("Food", "Junk")
        ),
        Item.create_expense_item(
            "Bus",
            20,
            "Travel Expenses by Bus",
            "2024-02-05",
            Category("Transportation"),
        ),
        Item.create_expense_item(
            "Bitcoin", -300, "Loss on Bitcoin Gambling.", "2024-04-20"
        ),
    ]
    ItemsDB(DB_PATH).insert_items(items)


def mock_clear_test():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    if os.path.exists(str(Path(__file__).resolve().parent / "report.xlsx")):
        os.remove(str(Path(__file__).resolve().parent / "report.xlsx"))

    if os.path.exists(str(Path(__file__).resolve().parent / "report.pdf")):
        os.remove(str(Path(__file__).resolve().parent / "report.pdf"))


if __name__ == "__main__":
    mock_add_items()
    app = App(DB_PATH)
    app.mainloop()
    mock_clear_test()

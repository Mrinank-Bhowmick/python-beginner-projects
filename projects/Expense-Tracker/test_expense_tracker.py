from tinydb import Query
import unittest
import os

from item import Category, Item, ItemsDB
from expense_income_stats import ExpenseIncomeStats


class TestItem(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_item_without_category(self):
        item = Item.create("ItemName", 100, "Some Description", "2024-05-14", None)

        self.assertIsNone(item.category)

    def test_create_item_with_category_without_subcategory(self):
        category = Category("CategoryA")
        item = Item.create("ItemName", 100, "Some Description", "2024-05-14", category)

        self.assertIsNotNone(item.category)
        self.assertEqual(item.category.name, "CategoryA")
        self.assertIsNone(item.category.subcategory)

    def test_create_item_with_category_with_subcategory(self):
        category = Category("CategoryA", "Subcategory1")
        item = Item.create("ItemName", 100, "Some Description", "2024-05-14", category)

        self.assertIsNotNone(item.category)
        self.assertEqual(item.category.name, "CategoryA")
        self.assertIsNotNone(item.category.subcategory)
        self.assertEqual(item.category.subcategory, "Subcategory1")

    def test_item_serialization_and_deserialization(self):
        category = Category("CategoryA", "Subcategory1")
        item = Item.create("ItemName", 100, "Some Description", "2024-05-14", category)

        json_str = item.to_json_str()
        same_item = Item.from_json_str(json_str)

        self.assertEqual(same_item, item)

        self.assertEqual(item.name, same_item.name)
        self.assertEqual(item.amount, same_item.amount)
        self.assertEqual(item.description, same_item.description)
        self.assertEqual(item.date, same_item.date)
        self.assertEqual(item.category, same_item.category)


class TestItemsDB(unittest.TestCase):
    def setUp(self):
        self.json_db_path = os.path.join(os.path.dirname(__file__), "items_db.json")
        self.items_db = ItemsDB(self.json_db_path)

        self.items = [
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
                "Pizza",
                50,
                "Pizza from Pizza Hut",
                "2023-04-20",
                Category("Food", "Junk"),
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

    def tearDown(self):
        if os.path.exists(self.json_db_path):
            os.remove(self.json_db_path)

    def test_insert_items(self):
        # Inserting Multiple Items
        self.items_db.insert_items(self.items)
        self.assertEqual(len(self.items_db), 6)

        # Inserting One Item
        new_item = Item.create_income_item(
            "APL Dividend",
            600,
            "Dividend from Apple Stock. The Fruit Company",
            "2024-03-26",
        )
        self.items_db.insert_item(new_item)
        self.assertEqual(len(self.items_db), 7)

    def test_update_items(self):
        self.items_db.insert_items(self.items)

        self.items_db.update_items({"amount": -10}, Query().name == "Bus")

        items = [item for item in self.items_db.get_all_items() if item.name == "Bus"]

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].amount, -10)

        self.assertEqual(len(self.items_db), len(self.items))

    def test_upsert_item(self):
        self.items_db.insert_items(self.items)

        new_item = Item.create_income_item(
            "APL Dividend",
            600,
            "Dividend from Apple Stock. The Fruit Company",
            "2024-03-26",
        )

        self.items_db.upsert_item(new_item)
        self.assertEqual(len(self.items_db), 7)

        item_0 = self.items[0]
        item_0.name = "Ethereum"
        self.items_db.upsert_item(item_0)
        self.assertEqual(len(self.items_db), 7)  # Same Item by the generated id

        items = [
            item for item in self.items_db.get_all_items() if item.name == "Ethereum"
        ]
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0], item_0)

    def test_delete_item(self):
        self.items_db.insert_items(self.items)

        item_to_remove = self.items[0]  # name='Bitcoin'
        self.items_db.delete_item(item_to_remove)

        items = self.items_db.get_all_items()
        self.assertEqual(len(items), len(self.items) - 1)

    def test_delete_items(self):
        self.items_db.insert_items(self.items)

        self.items_db.delete_items(Query().amount < 0)  # i.e. Remove the Expenses

        items = self.items_db.get_all_items()
        self.assertEqual(len(items), 3)

        for item in self.items:
            if item.amount < 0:
                self.assertNotIn(item, items)

    def test_delete_all_items(self):
        self.items_db.insert_items(self.items)

        self.items_db.delete_all_items()

        items = self.items_db.get_all_items()
        self.assertEqual(len(items), 0)

    def test_get_all_items(self):
        self.items_db.insert_items(self.items)

        # Get All Items
        items = self.items_db.get_all_items()
        self.assertEqual(len(items), len(self.items))
        for item in items:
            self.assertIn(item, self.items)

    def test_get_items_by_date_range(self):
        self.items_db.insert_items(self.items)

        # Only for 2024
        items = self.items_db.get_items_by_date_range("2024-01-01", "2024-12-30")
        self.assertEqual(len(items), 4)

        # Only for 2023
        items = self.items_db.get_items_by_date_range("2023-01-01", "2023-12-30")
        self.assertEqual(len(items), 2)

    def test_get_category_names(self):
        self.items_db.insert_items(self.items)

        category_names = self.items_db.get_category_names()

        self.assertIsInstance(category_names, set)
        self.assertEqual(len(category_names), 4)

    def test_get_subcategory_names(self):
        self.items_db.insert_items(self.items)

        # With Subcategory
        subcategories = self.items_db.get_subcategory_names("Personal Finance")
        self.assertIsInstance(subcategories, set)
        self.assertEqual(len(subcategories), 1)

        # Without Subcategory
        subcategories = self.items_db.get_subcategory_names("Transportation")
        self.assertIsInstance(subcategories, set)
        self.assertEqual(len(subcategories), 0)

    def test_get_items_by_category(self):
        self.items_db.insert_items(self.items)

        for category_name in self.items_db.get_category_names():
            items = self.items_db.get_items_by_category(category_name)
            self.assertEqual(len(items), 1)

    def test_get_items_uncategorized(self):
        self.items_db.insert_items(self.items)

        items = self.items_db.get_items_uncategorized()
        self.assertEqual(len(items), 2)

    def test_get_items_without_subcategory(self):
        self.items_db.insert_items(self.items)

        items = self.items_db.get_items_without_subcategory("Youtube")
        self.assertEqual(len(items), 1)

        items = self.items_db.get_items_without_subcategory("Personal Finance")
        self.assertEqual(len(items), 0)


class TestExpenseIncomeStats(unittest.TestCase):
    def setUp(self):
        self.json_db_path = os.path.join(os.path.dirname(__file__), "items_db.json")
        self.items_db = ItemsDB(self.json_db_path)
        self.items = [
            Item.create_income_item(
                "Bitcoin",
                500,
                "Income from Bitcoin",
                "2023-06-25",
                Category("Personal Finance", "Investing"),
            ),
            Item.create_income_item(
                "Stock Dividends",
                5,
                "Income from Stock Dividends",
                "2024-1-10",
                Category("Personal Finance", "Investing"),
            ),
            Item.create_income_item("Gift", 30, "Gift from Relatives", "2024-03-04"),
            Item.create_expense_item(
                "Pizza",
                -50,
                "Pizza from Pizza Hut",
                "2023-04-20",
                Category("Food", "Junk"),
            ),
            Item.create_expense_item(
                "Bus",
                -20,
                "Travel Expenses by Bus",
                "2024-02-05",
                Category("Transportation", "Public Transport"),
            ),
            Item.create_expense_item(
                "Car Gas",
                -300,
                "Car Gas Expense",
                "2024-04-20",
                Category("Transportation"),
            ),
        ]
        self.items_db.insert_items(self.items)

        self.stats = ExpenseIncomeStats(self.json_db_path)

    def tearDown(self):
        if os.path.exists(self.json_db_path):
            os.remove(self.json_db_path)

    def test_get_stats_all_items(self):
        result = self.stats.get_stats_all_items()
        self.assertAlmostEqual(result["average_expense"], -123.33, places=2)
        self.assertEqual(result["min_expense"], -20)
        self.assertEqual(result["max_expense"], -300)
        self.assertAlmostEqual(result["average_income"], 178.33, places=2)
        self.assertEqual(result["min_income"], 5)
        self.assertEqual(result["max_income"], 500)

    def test_get_stats_by_category(self):
        result = self.stats.get_stats_by_category()

        import json

        print(json.dumps(result, indent=4))


if __name__ == "__main__":
    unittest.main()

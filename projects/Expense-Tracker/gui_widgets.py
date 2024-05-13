import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import os
from pathlib import Path

from item import ItemsDB, Item, Category
from expense_income_stats import ExpenseIncomeStats


class ItemsTable(ttk.Treeview):
    _COLUMN_PAIRS = [
        ('#0', 'ID'),
        ('name', 'Name'),
        ('amount', 'Amount'),
        ('description', 'Description'),
        ('date', 'Date'),
        ('category', 'Category'),
        ('subcategory', 'Subcategory'),
    ]

    def __init__(self, parent, items_db: ItemsDB, *args, **kwargs):
        super().__init__(parent, *args, columns=tuple(col for col, _ in self._COLUMN_PAIRS if '#' not in col), **kwargs)

        for i, j in self._COLUMN_PAIRS:
            self.heading(i, text=j)
            self.column(i, anchor=tk.CENTER)

        self._parent = parent
        self._items_db = items_db

        # For Testing
        self._test_add_items_to_db()
        self.load_items()

    def _test_add_items_to_db(self):
        items = \
            [Item.create_income_item('Bitcoin',
                                     500,
                                     "Income from Bitcoin",
                                     '2023-06-25',
                                     Category('Personal Finance', 'Investing')
                                     ),
             Item.create_income_item('Youtube Ads',
                                     5,
                                     "Income from Youtube Ads",
                                     '2024-1-10',
                                     Category('Youtube')
                                     ),
             Item.create_income_item('Gift',
                                     30,
                                     "Gift from Relatives",
                                     '2024-03-04'
                                     ),
             Item.create_expense_item('Pizza',
                                      50,
                                      "Pizza from Pizza Hut",
                                      '2023-04-20',
                                      Category('Food', 'Junk')
                                      ),
             Item.create_expense_item('Bus',
                                      20,
                                      "Travel Expenses by Bus",
                                      '2024-02-05',
                                      Category('Transportation')
                                      ),
             Item.create_expense_item('Bitcoin',
                                      -300,
                                      "Loss on Bitcoin Gambling.",
                                      '2024-04-20'
                                      ),
             ]
        self._items_db.insert_items(items)

    def clear_test(self):
        if os.path.exists(self._items_db.db_path):
            os.remove(self._items_db.db_path)

    def clear_items(self):
        # Clearing all the rows in Items Table (Not Deleting!)
        self.delete(*self.get_children())

    def deletes_item(self, items):
        for item in items:
            self._items_db.delete_item(item)

        # Update the View
        self.load_items()

        # Deselect any selected row
        self.deselect()

    def update_item(self, item):
        self._items_db.upsert_item(item)

        # Update the View
        self.load_items()

        # Deselect any selected row
        self.deselect()

    def add_item(self, item):
        # Update the State of the Local Json File
        self._items_db.insert_item(item)

        # Update the View
        self.load_items()

        # Deselect any selected row
        self.deselect()

    def deselect(self):
        for item in self.selection():
            self.selection_remove(item)

    def load_items(self):
        self.clear_items()  # Clear the Previous Items State

        for idx, item in enumerate(self._items_db.get_all_items()):
            values = (
                item.name,
                item.amount,
                item.description,
                item.date,
            )

            if item.category is not None:
                values += (item.category.name, item.category.subcategory)
            else:
                values += (None, None)

            self.insert('',
                        idx,
                        text=f'{item.item_id}',
                        values=values
                        )


class SummaryByCategoryPivotTable:
    def __init__(self, parent):
        self.parent = parent

        db_path = Path(__file__).resolve().parent
        self.stats = ExpenseIncomeStats(str(db_path / 'items.json'))
        self.tree = None

    def update_pivot_table(self):
        # Get statistic data from local json
        data = self.stats.get_stats_by_category()

        # Destroy the old child
        if self.tree is not None:
            self.tree.destroy()

        # Transpose the data
        transposed_data = {}
        for category, values in data.items():
            for key, value in values.items():
                if key not in transposed_data:
                    transposed_data[key] = {}
                transposed_data[key][category] = value

        # Create Treeview
        self.tree = ttk.Treeview(self.parent)
        self.tree["columns"] = ["Category"] + list(data.keys())
        self.tree.column("#0", width=100, minwidth=100)
        # self.tree.column("#0", width=0)

        self.tree.heading("#0", text="")
        for category in data.keys():
            self.tree.heading(category, text=category)

        self.tree['show'] = 'headings'

        def clean_string(input_string):
            cleaned_string = input_string.replace("_", " ").title()
            return cleaned_string

        for aggregate_type, values in transposed_data.items():
            row_values = [clean_string(aggregate_type)]
            for category in data.keys():
                row_values.append(values.get(category, ""))
            self.tree.insert("", "end", text=aggregate_type, values=tuple(row_values))

        self.tree.pack(expand=True, fill="both")

import tkinter as tk
from tkinter import ttk
from pathlib import Path

from item import ItemsDB
from expense_income_stats import ExpenseIncomeStats


class ItemsTable(ttk.Treeview):
    """
    Represents a table widget for displaying items.

    This class inherits from ttk.Treeview and provides methods for managing and displaying items.
    """

    _COLUMN_PAIRS = [
        ("#0", "ID"),
        ("name", "Name"),
        ("amount", "Amount"),
        ("description", "Description"),
        ("date", "Date"),
        ("category", "Category"),
        ("subcategory", "Subcategory"),
    ]

    def __init__(self, parent, items_db: ItemsDB, *args, **kwargs):
        """
        Initializes the ItemsTable instance.

        Args:
            parent: The parent widget.
            items_db (ItemsDB): An instance of the ItemsDB class representing the database.
            *args: Additional positional arguments for `ttk.Treeview`.
            **kwargs: Additional keyword arguments for `ttk.Treeview`.
        """

        super().__init__(
            parent,
            *args,
            columns=tuple(col for col, _ in self._COLUMN_PAIRS if "#" not in col),
            **kwargs,
        )

        for i, j in self._COLUMN_PAIRS:
            self.heading(i, text=j)
            self.column(i, anchor=tk.CENTER)

        self._parent = parent
        self._items_db = items_db

        self.load_items()

    def clear_items(self):
        """Clears all the rows in the ItemsTable."""

        # Clearing all the rows in Items Table (Not Deleting!)
        self.delete(*self.get_children())

    def deletes_item(self, items):
        """
        Deletes items from the database and updates the view.

        Args:
            items (List[Item]): The items to delete.
        """

        for item in items:
            self._items_db.delete_item(item)

        # Update the View
        self.load_items()

        # Deselect any selected row
        self.deselect()

    def update_item(self, item):
        """
        Updates an item in the database and updates the view.

        Args:
            item (Item): The item to update.
        """
        self._items_db.upsert_item(item)

        # Update the View
        self.load_items()

        # Deselect any selected row
        self.deselect()

    def add_item(self, item):
        """
        Adds an item to the database and updates the view.

        Args:
            item (Item): The item to add.
        """

        # Update the State of the Local Json File
        self._items_db.insert_item(item)

        # Update the View
        self.load_items()

        # Deselect any selected row
        self.deselect()

    def deselect(self):
        """Deselects any selected row in the table."""

        for item in self.selection():
            self.selection_remove(item)

    def load_items(self):
        """Loads items from the database and populates the table."""

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

            self.insert("", idx, text=f"{item.item_id}", values=values)


class SummaryByCategoryPivotTable:
    """Represents a pivot table widget for summarizing item data by category."""

    def __init__(self, parent):
        """
        Initializes the SummaryByCategoryPivotTable instance.

        Args:
            parent: The parent widget.
        """

        self.parent = parent

        db_path = Path(__file__).resolve().parent
        self.stats = ExpenseIncomeStats(str(db_path / "items.json"))
        self.tree = None

    def update_pivot_table(self):
        """Updates the pivot table with statistics data."""

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

        self.tree["show"] = "headings"

        def clean_string(input_string):
            cleaned_string = input_string.replace("_", " ").title()
            return cleaned_string

        for aggregate_type, values in transposed_data.items():
            row_values = [clean_string(aggregate_type)]
            for category in data.keys():
                row_values.append(values.get(category, ""))
            self.tree.insert("", "end", text=aggregate_type, values=tuple(row_values))

        self.tree.pack(expand=True, fill="both")

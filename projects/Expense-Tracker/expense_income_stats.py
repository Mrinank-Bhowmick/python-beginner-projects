from abc import ABC, abstractmethod
from item import ItemsDB
import statistics


class ExpenseIncomeStats:
    def __init__(self, db_path: str, start: str = None, end: str = None):
        self._items_db = ItemsDB(db_path)
        self.start = start
        self.end = end

        if start is None and end is None:
            # Get all Items
            self._items = self._items_db.get_all_items()
            pass
        elif start is None and end is not None:
            # Start from the Oldest Item(s) to the given end date string
            oldest = min(item.date for item in self._items_db.get_all_items())
            self._items = self._items_db.get_items_by_date_range(oldest.strftime("%Y-%m-%d"), end)
        elif start is not None and end is None:
            # Start from the given start date string to the latest date
            latest = max(item.date for item in self._items_db.get_all_items())
            self._items = self._items_db.get_items_by_date_range(start, latest.strftime("%Y-%m-%d"))
        else:
            # Get item from given date range
            self._items = self._items_db.get_items_by_date_range(start, end)

    @staticmethod
    def _get_stats(items) -> dict:
        expense_items = [item.amount for item in items if item.amount < 0]
        if len(expense_items) > 0:
            expense_stats = {
                "average_expense": statistics.mean(expense_items),
                "min_expense": max(expense_items),  # Warn: Negative Sign
                "max_expense": min(expense_items),
            }
        else:
            expense_stats = {}

        income_items = [item.amount for item in items if item.amount > 0]
        if len(income_items) > 0:
            income_stats = {
                "average_income": statistics.mean(income_items),
                "min_income": min(income_items),
                "max_income": max(income_items),
            }
        else:
            income_stats = {}

        return expense_stats | income_stats

    def get_stats(self):
        return self._get_stats(self._items)

    def get_stats_by_category(self) -> dict:
        # The 'root' of category (i.e. it aggregates the subcategories). We do not care about the subcategories.
        # Set of Root Categories
        # item.get_category_str() for an item without category would return 'Uncategorized'
        category_names = {item.category.name if item.category is not None else item.get_category_str() for item in
                          self._items}

        out_dict = {}
        for category_name in category_names:
            items = [item for item in self._items if item.category.name == category_name]
            out_dict[category_name] = self._get_stats(items)

        return out_dict

    def get_stats_by_category_with_subcategories(self) -> dict:
        category_names = self._items_db.get_category_names()
        stats_dict = {}
        for category_name in category_names:
            # Case: With Category and Without Subcategory
            stats_dict[f'{category_name}-NoSubcategory'] = self._get_stats(
                self._items_db.get_items_without_subcategory(category_name))
            # Case: With Category and With Subcategory
            for subcategory in self._items_db.get_subcategory_name(category_name):
                stats_dict[f'{category_name}-{subcategory}'] = \
                    self._get_stats(self._items_db.get_items_by_category_and_subcategory(category_name, subcategory))

        return stats_dict

    @staticmethod
    def currency_converter(base_currency: str, quote_currency: str) -> float:
        # TODO: Implement currency_converter() method.
        pass


class Report(ABC):
    @abstractmethod
    def generate_report(self, *args, **kwargs):
        pass


class ExcelReport(Report):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def generate_report(self):
        pass


class PdfReport(Report):
    def generate_report(self):
        pass

from abc import ABC, abstractmethod
from item import ItemsDB
import pandas as pd
import statistics


class ExpenseIncomeStats:
    """
    Represents a class for calculating expense and income statistics based on items from a database.
    """

    def __init__(self, db_path: str, start: str = None, end: str = None):
        """
        Initializes the ExpenseIncomeStats instance.

        Args:
            db_path (str): The path to the database file.
            start (str, optional): The start date for filtering items. Defaults to None.
            end (str, optional): The end date for filtering items. Defaults to None.
        """

        self._items_db = ItemsDB(db_path)
        self.start = start
        self.end = end

    @property
    def items(self):
        """
        Retrieves all items from the database.

        Returns:
            List[Item]: A list of all items in the database.
        """
        return self._items_db.get_all_items()

    @staticmethod
    def get_stats_expense_and_income(items) -> dict:
        """
        Calculates statistics for both expense and income items, separately.

        Args:
            items (List[Item]): The list of items to calculate statistics for.

        Returns:
            dict: A dictionary containing statistics for both expense and income items.
        """

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

    @staticmethod
    def get_stats(items) -> dict:
        """
        Calculates general statistics for a list of items.

        Args:
            items (List[Item]): The list of items to calculate statistics for.

        Returns:
            dict: A dictionary containing general statistics for the list of items.
        """
        if len(items) < 1:
            raise ValueError("The list of items must contain at least one item")

        return {
            "average": statistics.mean(items),
            "max": max(items),
            "min": min(items),
        }

    def get_stats_all_items(self):
        """
        Calculates statistics for all items in the database.

        Returns:
            dict: A dictionary containing statistics for all items in the database.
        """
        return self.get_stats_expense_and_income(self.items)

    def get_stats_by_category(self) -> dict:
        """
        Calculates statistics for each category in the database.

        Returns:
            dict: A dictionary containing statistics for each category.
        """
        category_names = self._items_db.get_category_names()
        out_dict = {}
        for category_name in category_names:
            items = [
                item for item in self._items_db.get_items_by_category(category_name)
            ]
            out_dict[category_name] = self.get_stats_expense_and_income(items)

        return out_dict

    def get_stats_by_category_with_subcategories(self) -> dict:
        """
        Calculates statistics for each category and subcategory combination in the database.

        Returns:
            dict: A dictionary containing statistics for each category and subcategory combination.
        """
        category_names = self._items_db.get_category_names()
        stats_dict = {}
        for category_name in category_names:
            # Case: With Category and Without Subcategory
            stats_dict[f"{category_name}-NoSubcategory"] = (
                self.get_stats_expense_and_income(
                    self._items_db.get_items_without_subcategory(category_name)
                )
            )

            # Case: With Category and With Subcategory
            for subcategory in self._items_db.get_subcategory_names(category_name):
                stats_dict[f"{category_name}-{subcategory}"] = (
                    self.get_stats_expense_and_income(
                        self._items_db.get_items_by_category_and_subcategory(
                            category_name, subcategory
                        )
                    )
                )

        return stats_dict


class Report(ABC):
    """
    Abstract base class for generating reports based on items from a database.
    """

    def __init__(self, file_path: str, items_db: ItemsDB):
        """
        Default Initialization for the Report instance.

        Args:
            file_path (str): The file path to save the report.
            items_db (ItemsDB): An instance of the ItemsDB class representing the database.
        """

        self.file_path = file_path
        self.items_db = items_db

    @abstractmethod
    def generate_report(self, *args, **kwargs):
        """
        Abstract method for generating a report.

        Args:
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        """
        pass

    @staticmethod
    def to_dataframe(items) -> pd.DataFrame:
        """
        Converts a list of items to a pandas DataFrame.

        Args:
            items (List[Item]): The list of items to convert.

        Returns:
            pd.DataFrame: A DataFrame containing the item data.
        """

        # items: List[Item]

        rows = []
        for item in items:
            category = item.category
            row = {k: v for k, v in item.__dict__.items() if k != "category"}

            if category is not None:
                row["category"] = category.name
                if category.subcategory is not None:
                    row["subcategory"] = category.subcategory

            rows.append(row)

        return pd.DataFrame(rows)


class ExcelReport(Report):
    """Generates an Excel report based on items from a database."""

    def generate_report(self):
        """Generates an Excel report."""

        # TODO: Enhance - Include the Items without Category or Subcategory
        items = self.items_db.get_all_items()
        df = self.to_dataframe(items)

        with pd.ExcelWriter(self.file_path, engine="xlsxwriter") as writer:
            workbook = writer.book

            # Raw Data Tab
            df.to_excel(
                writer,
                "Data",  # worksheet name
                index=False,  # index does not contain relevant information
            )
            summary_sheet = writer.sheets[
                "Data"
            ]  # Assigning a variable to the sheet allows formatting

            # Pivot Table Tab
            pivot_table = df.pivot_table(
                values="amount",
                index=["category", "subcategory"],
                aggfunc={
                    "amount": ["mean", "max", "min"],
                },
            )

            # Flatten the hierarchical column index
            pivot_table.columns = [f"{agg}_amount" for agg in pivot_table.columns]

            pivot_table.to_excel(
                writer,
                "Summary By Category",  # worksheet name
                index=True,  # index does not contain relevant information
            )
            summary_sheet = writer.sheets["Summary By Category"]


class PdfReport(Report):
    """Generates a PDF report based on items from a database."""

    def generate_report(self):
        """Generates a PDF report."""

        items = self.items_db.get_all_items()
        df = self.to_dataframe(items)

        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

        # Pivot Table Tab
        pivot_table = df.pivot_table(
            values="amount",
            index=["category", "subcategory"],
            aggfunc={
                "amount": ["mean", "max", "min"],
            },
        )
        pivot_table = pivot_table.reset_index()

        # Convert DataFrame to a list of lists for the table
        table_data = [list(pivot_table.columns)] + pivot_table.values.tolist()

        # Create PDF
        pdf_filename = self.file_path
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        elements = []

        # Create table
        table = Table(table_data)

        # Style the table
        style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )

        table.setStyle(style)

        # Add table to elements
        elements.append(table)

        # Build PDF
        doc.build(elements)

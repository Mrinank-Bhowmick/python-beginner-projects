from typing import Optional, List, Set
from dataclasses import dataclass, asdict, is_dataclass
from datetime import datetime
from copy import deepcopy
from tinydb import TinyDB, Query
import uuid
import json


class EnhancedJSONEncoder(json.JSONEncoder):
    """
    JSON encoder subclass that enhances the default behavior to support Python's dataclasses.

    This encoder extends the default JSON encoding behavior to handle instances of Python dataclasses,
    converting them into JSON-compatible dictionaries using `asdict` from the `dataclasses` module.

    Reference:
        - https://stackoverflow.com/questions/51286748/make-the-python-json-encoder-support-pythons-new-dataclasses
    """

    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)


@dataclass
class Category:
    name: str
    subcategory: Optional[str] = None

    def __str__(self):
        if self.subcategory is None:
            return f"{self.name}-NoSubcategory"
        else:
            return f"{self.name}-{self.subcategory}"

    def __eq__(self, other):
        return self.name == other.name and self.subcategory == other.subcategory

    def is_same_category_name(self, other):
        return self.name == other.name


@dataclass
class Item:
    """
    Represents an expense or income item in the expense tracker app.

    This class provides methods to create, manipulate, and serialize/deserialize expense or income items.
    """

    item_id: str
    name: str
    amount: float
    description: str
    date: datetime
    category: Optional[Category] = None

    def __str__(self):
        return self.to_json_str(indent=4)

    def get_category_str(self) -> str:
        """
        Returns the category of the item as a string.

        Returns:
            str: The category of the item or "Uncategorized" if category is None.
        """
        return "Uncategorized" if self.category is None else str(self.category)

    @classmethod
    def create(
        cls,
        name: str,
        amount: float,
        description: str,
        date_str: str,
        category: Optional[Category] = None,
    ):
        """
        Factory method to create an expense or income Item instance.

        Args:
            name (str): The name for the item.
            amount (float): The amount associated with the item. This could be +ve or -ve.
            description (str): Additional details about the item.
            date_str (str): The date and time when the item occurred, in "YYYY-MM-DD" format.
            category (Optional[Category]): The category of the item. Defaults to None.

        Returns:
            Item: An instance of the Item class representing the created item.
        """
        item_id = str(uuid.uuid4())  # Generate a unique ID
        # item_id = str(name + '-' + date_str)  # Generate a unique ID
        date = datetime.strptime(
            date_str, "%Y-%m-%d"
        )  # Parse the date string into a datetime object
        return cls(
            item_id=item_id,
            name=name,
            amount=amount,
            description=description,
            date=date,
            category=category,
        )

    @classmethod
    def create_expense_item(
        cls,
        name: str,
        amount: float,
        description: str,
        date_str: str,
        category: Optional[Category] = None,
    ):
        """
        Factory method to create an expense Item instance.

        Args:
            name (str): The name for the expense.
            amount (float): The amount associated with the expense. This will be converted to -ve.
            description (str): Additional details about the expense.
            date_str (str): The date and time when the expense occurred, in "YYYY-MM-DD" format.
            category (Optional[Category]): The category of the expense. Defaults to None.

        Returns:
            Item: An instance of the Item class representing the created expense item.
        """

        if amount >= 0:
            return cls.create(
                name, -abs(amount), description, date_str, category=category
            )

        return cls.create(name, amount, description, date_str, category=category)

    @classmethod
    def create_income_item(
        cls,
        name: str,
        amount: float,
        description: str,
        date_str: str,
        category: Optional[Category] = None,
    ):
        """
        Factory method to create an income Item instance.

        Args:
            name (str): The name for the income.
            amount (float): The amount associated with the income. This will be converted to +ve.
            description (str): Additional details about the income.
            date_str (str): The date and time when the income occurred, in "YYYY-MM-DD" format.
            category (Optional[Category]): The category of the income. Defaults to None.

        Returns:
            Item: An instance of the Item class representing the created income item.
        """
        return cls.create(name, abs(amount), description, date_str, category=category)

    @classmethod
    def from_json_str(cls, json_str):
        """
        Creates an expense or income Item instance from a JSON string.

        Args:
            json_str (str): JSON string representing the item.

        Returns:
            Item: An instance of the Item class created from the JSON string.
        """

        data_dict = json.loads(json_str)

        # Convert date string back to datetime object
        data_dict["date"] = datetime.strptime(data_dict["date"], "%Y-%m-%d %H:%M:%S")

        # Check if category is present and reconstruct Category object
        if data_dict["category"]:
            data_dict["category"] = Category(**data_dict["category"])

        return cls(**data_dict)

    def to_json_str(self, *args, **kwargs) -> str:
        """
        Serializes the Item object to a JSON string.

        Args:
            *args: Additional positional arguments to pass to json.dumps().
            **kwargs: Additional keyword arguments to pass to json.dumps().

        Returns:
            str: JSON string representation of the Item object.
        """
        return json.dumps(
            self.to_serializable_dict(), *args, cls=EnhancedJSONEncoder, **kwargs
        )

    def to_serializable_dict(self) -> dict:
        """
        Returns a dictionary representation of the Item object suitable for JSON serialization.

        Returns:
            dict: Dictionary representation of the Item object.
        """

        data_dct = deepcopy(self.__dict__)

        # Check if category is not None
        if data_dct["category"]:
            data_dct["category"] = asdict(data_dct["category"])

        # Stringify Date
        data_dct["date"] = str(data_dct["date"])
        return data_dct


class ItemsDB:
    """
    Represents a database manager for storing and retrieving items in the expense tracker app.

    This class provides methods to interact with the underlying database, including inserting, updating,
    and querying items.
    """

    def __init__(self, db_path: str):
        """
        Initializes the ItemsDB instance with the provided database file path.

        Args:
            db_path (str): The path to the database file.
        """
        self.db_path = db_path

    def __len__(self):
        """
        Returns the number of items in the database.

        Returns:
            int: The number of items in the database.
        """
        with TinyDB(self.db_path) as db:
            return len(db)

    def print_db(self):
        """
        Prints all items in the database as JSON strings.
        """

        for item in self.get_all_items():
            print(item.to_json_str(indent=4))

    def insert_item(self, item: Item) -> None:
        """
        Inserts a single item into the database.

        Args:
            item (Item): The item to insert into the database.
        """

        data_dict = dict(json.loads(item.to_json_str()))
        with TinyDB(self.db_path) as db:
            db.insert(data_dict)

    def insert_items(self, items: List[Item]) -> None:
        """
        Inserts multiple items into the database.

        Args:
            items (List[Item]): The list of items to insert into the database.
        """
        with TinyDB(self.db_path) as db:
            db.insert_multiple([dict(json.loads(item.to_json_str())) for item in items])

    def update_items(self, update_dict: dict, query: Query) -> None:
        """
        Updates items in the database based on a tinydb query.

        Args:
            update_dict (dict): The dictionary containing fields to update and their new values.
            query (Query): The query used to filter items for updating.
        """
        with TinyDB(self.db_path) as db:
            db.update(update_dict, query)

    def upsert_item(self, item: Item) -> None:
        """
        Inserts or updates an item in the database.

        Args:
            item (Item): The item to insert or update in the database.
        """
        dct = item.to_serializable_dict()
        with TinyDB(self.db_path) as db:
            db.upsert(dct, Query().item_id == str(dct["item_id"]))

    def delete_items(self, cond: Query) -> None:
        """
        Deletes items from the database based on a query.

        Args:
            cond (Query): The query used to filter items for deletion.
        """
        with TinyDB(self.db_path) as db:
            db.remove(cond)

    def delete_item(self, item: Item) -> None:
        """
        Deletes a single item from the database.

        Args:
            item (Item): The item to delete from the database.
        """
        self.delete_items(Query().item_id == item.item_id)

    def delete_all_items(self):
        """
        Deletes all items from the database.
        """
        with TinyDB(self.db_path) as db:
            db.truncate()

    def get_all_items(self) -> List[Item]:
        """
        Retrieves all items from the database.

        Returns:
            List[Item]: A list of all items in the database.
        """
        with TinyDB(self.db_path) as db:
            return [Item.from_json_str(json.dumps(doc)) for doc in db.all()]

    def get_items_by_date_range(self, start: str, end: str) -> List[Item]:
        """
        Retrieves items within a specified date range.

        Args:
            start (str): The start date of the range in "YYYY-MM-DD" format.
            end (str): The end date of the range in "YYYY-MM-DD" format.

        Returns:
            List[Item]: A list of items within the specified date range.
        """
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
        return [
            item for item in self.get_all_items() if start_date <= item.date <= end_date
        ]

    def get_items_by_category(self, category_name: str) -> List[Item]:
        """
        Retrieves items by category name.

        Args:
            category_name (str): The name of the category.

        Returns:
            List[Item]: A list of items belonging to the specified category.
        """
        return [
            item
            for item in self.get_all_items()
            if item.category is not None and item.category.name == category_name
        ]

    def get_items_by_category_and_subcategory(
        self, category_name: str, subcategory_name: str
    ) -> List[Item]:
        """
        Retrieves items by category and subcategory names.

        Args:
            category_name (str): The name of the category.
            subcategory_name (str): The name of the subcategory.

        Returns:
            List[Item]: A list of items belonging to the specified category and subcategory.
        """
        return [
            item
            for item in self.get_all_items()
            if item.category.name == category_name
            and item.category.subcategory == subcategory_name
        ]

    def get_items_uncategorized(self) -> List[Item]:
        """
        Retrieves items without a category.

        Returns:
            List[Item]: A list of items without a category.
        """
        return [item for item in self.get_all_items() if item.category is None]

    def get_items_without_subcategory(self, category_name: str) -> List[Item]:
        """
        Retrieves items without a subcategory within a category.

        Args:
            category_name (str): The name of the category.

        Returns:
            List[Item]: A list of items without a subcategory within the specified category.
        """
        # This excludes uncategorized items (i.e. item.category is None)
        return [
            item
            for item in self.get_all_items()
            if item.category is not None
            and item.category.name == category_name
            and item.category.subcategory is None
        ]

    def get_items_with_subcategory(self, category_name: str) -> List[Item]:
        """
        Retrieves items with a subcategory within a category.

        Args:
            category_name (str): The name of the category.

        Returns:
            List[Item]: A list of items with a subcategory within the specified category.
        """
        # This excludes uncategorized items (i.e. item.category is None)
        return [
            item
            for item in self.get_all_items()
            if item.category is not None
            and item.category.name == category_name
            and item.category.subcategory is not None
        ]

    def get_category_names(self) -> Set[str]:
        """
        Retrieves unique category names from the database.

        Returns:
            Set[str]: A set of unique category names.
        """
        # This excludes the Items with No Category (i.e. item.category is None)
        return {
            item.category.name
            for item in self.get_all_items()
            if item.category is not None
        }

    def get_subcategory_names(self, category_name: str) -> Set[str]:
        """
        Retrieves unique subcategory names within a category from the database.

        Args:
            category_name (str): The name of the category.

        Returns:
            Set[str]: A set of unique subcategory names within the specified category.
        """
        # This excludes items without subcategories
        return {
            item.category.subcategory
            for item in self.get_all_items()
            if item.category is not None
            and item.category.name == category_name
            and item.category.subcategory is not None
        }

    def get_expense_items(self):
        """
        Retrieves all expense items from the database.

        Returns:
            List[Item]: A list of all expense items.
        """
        return [item for item in self.get_all_items() if item.amount < 0]

    def get_income_items(self):
        """
        Retrieves all income items from the database.

        Returns:
            List[Item]: A list of all income items.
        """
        return [item for item in self.get_all_items() if item.amount > 0]

import unittest


class Budget:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def delete_transaction(self, transaction):
        self.transactions.remove(transaction)


class TestBudgetFunctionality(unittest.TestCase):
    def test_delete_transaction(self):
        # Arrange
        budget = Budget()
        transaction_to_delete = {
            "date": "2023-01-01",
            "description": "Test Transaction",
            "amount": 100.0,
            "category": "Test",
        }
        # Act
        budget.add_transaction(transaction_to_delete)
        budget.delete_transaction(transaction_to_delete)

        # Assert ()
        self.assertNotIn(transaction_to_delete, budget.transactions)


if __name__ == "__main__":
    unittest.main()

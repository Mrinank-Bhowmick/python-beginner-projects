def comma_code(items):
    """Combines list into a string of the form item1, item2, and item 3
    Args:
        items (list): List of strings

    Returns:
        string: list items combined into a string
    """
    item_len = len(items)

    if item_len == 0:
        return ""
    elif item_len == 1:
        return items[0]

    return ", ".join(items[:-1]) + ", and " + items[-1]


if __name__ == "__main__":
    spam = ["apples", "bananas", "tofu", "cats"]
    print(comma_code(spam))

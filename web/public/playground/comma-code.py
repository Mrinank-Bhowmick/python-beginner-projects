# === Comma Code · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ibra-kdbra.

# Join a list into a comma-separated English string
def comma_code(items):
    item_len = len(items)

    # Return empty string for empty list
    if item_len == 0:
        return ""
    elif item_len == 1:
        return items[0]

    # Join all but last, then append "and <last>"
    return ", ".join(items[:-1]) + ", and " + items[-1]


if __name__ == "__main__":
    # Test with a sample list
    spam = ["apples", "bananas", "tofu", "cats"]
    print(comma_code(spam))

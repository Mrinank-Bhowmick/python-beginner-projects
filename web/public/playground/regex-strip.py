# === Regex Strip · annotated for the pyBegin playground ===
# A beginner-friendly walkthrough — original project by @ibra-kdbra.

import re


# Strip leading/trailing whitespace using regex
def strip(text):
    stripStartRegex = re.compile(r"(^\s*)")
    stripEndRegex = re.compile(r"(\s*$)")

    # Remove leading spaces, then trailing spaces
    textStartStripped = stripStartRegex.sub("", text)
    textStripped = stripEndRegex.sub("", textStartStripped)

    return textStripped


# Run the strip function on a sample string
if __name__ == "__main__":
    text = " test ffs   "
    print(strip(text))

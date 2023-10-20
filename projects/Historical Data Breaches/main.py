import requests
import json
import re

# Request the organisation that the user would like to query for
organisation = input("Enter organisation name or domain: ")

# Connect to the HIBP API
url = "https://haveibeenpwned.com/api/v3/breaches"
r = requests.get(url)

# Load the API response in a JSON data set
dataset = json.loads(r.text)

# Initialise variable to determine whether the breach is found in the API response
breach_found = False

# Iterate through the entire JSON file of data breaches to search for the requested data breach
for breach in dataset:
    if (
        breach["Name"].lower() == organisation.lower()
        or breach["Domain"].lower() == organisation.lower()
    ):
        print("\nName:", breach["Name"])
        print("Date of breach:", breach["BreachDate"])
        print("Number of accounts breached:", "{:,}".format(breach["PwnCount"]))
        # The Description field contains hyperlinks to the source(s) of the information. However these references
        # reduce the readeability of the description and therefore will be removed using regex patterns.
        regex_pattern1 = r'<a href=".*?">'
        regex_pattern2 = r"</a>"
        print(
            "Description:",
            re.sub(
                regex_pattern2, "", (re.sub(regex_pattern1, "", breach["Description"]))
            ),
        )
        print("Data contained in breach:")
        for dataclass in breach["DataClasses"]:
            print(" *", dataclass)
        breach_found = True

if breach_found == False:
    print("Could not find data breach details for", organisation)

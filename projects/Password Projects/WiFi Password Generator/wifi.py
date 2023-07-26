# Importing the subprocess module allows us to run external commands from the Python script.
import subprocess

# Using the 'subprocess.check_output()' function to execute the "netsh wlan show profiles" command
# and capture its output, which contains the names of all wireless network profiles saved on the system.
data = (
    subprocess.check_output(["netsh", "wlan", "show", "profiles"])
    .decode("utf-8")
    .split("\n")
)

# Extracting only the names of the wireless network profiles from the 'data' variable.
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

# Looping through each wireless network profile name in the 'profiles' list.
for i in profiles:
    # Using 'subprocess.check_output()' again to execute the "netsh wlan show profile <profile_name> key=clear" command
    # for each network profile and capturing its output.
    results = (
        subprocess.check_output(["netsh", "wlan", "show", "profile", i, "key=clear"])
        .decode("utf-8")
        .split("\n")
    )

    # Extracting the Wi-Fi password (Key Content) from the 'results' variable for each network profile.
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    # Printing the network profile name along with its corresponding Wi-Fi password.
    # If the password is not found, an empty string will be printed.
    try:
        print("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))

# The following line prompts the user to press Enter to exit the script.
# This is to prevent the terminal from closing immediately after execution.
input("")

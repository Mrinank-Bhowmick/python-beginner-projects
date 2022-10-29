import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(
    Fore.BLUE
    + Back.YELLOW
    + "Hi, My name is Nowshin "
    + Fore.YELLOW
    + Back.BLUE
    + "I love open-source contribution"
)
print(Back.CYAN + "Hi, My name is Nowshin")
print(Fore.RED + Back.GREEN + "Hi My name is Nowshin")

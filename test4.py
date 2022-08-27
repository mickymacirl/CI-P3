# import os to help clear terminal for user on replay
import os

# import player class

# import CodeGenerator class

# import pyfiglet module for ascii art
import pyfiglet

# import colorama for adding colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)
def logo_display():
    """
    Logo display
    """
    name = pyfiglet.figlet_format(
        "HangMan", font="standard", justify="center")
    print(name)

    title = pyfiglet.figlet_format(
        "Fruit Word Game", font="cybersmall", justify="center")
    print(title)

    print(Fore.YELLOW + "Micky Mac".center(80) + "\n")
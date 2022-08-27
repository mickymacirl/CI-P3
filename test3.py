import random  # import random
import pyfiglet  # import pyfiglet for hangman logo
from os import system, name  # import system from os for clear function
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
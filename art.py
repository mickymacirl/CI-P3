import pyfiglet  # import pyfiglet for hangman logo
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def logo_display():
    """
    Logo display
    """
    headermain = pyfiglet.figlet_format(
        "HangMan", font="standard", justify="center")
    print(headermain)

    title = pyfiglet.figlet_format(
        "Fruit Word Game", font="cybersmall", justify="center")
    print(title)

    print(Fore.YELLOW + "Fruit Edition(TM)".center(80) + "\n")

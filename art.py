""" This is the fuction that displays the hangman logo """
import pyfiglet  # import pyfiglet for hangman logo
import colorama
from colorama import Fore

colorama.init(autoreset=True)


def logo_display():
    """
    HANGMAN Logo Display
    """
    h_m = pyfiglet.figlet_format("HangMan", font="standard", justify="center")
    print(h_m)  # Display FIGLET Header

    title = pyfiglet.figlet_format(
        "Fruit Word Game", font="cybersmall", justify="center"
    )
    print(title)

    print(Fore.YELLOW + "Fruit Edition(TM)".center(80) + "\n")

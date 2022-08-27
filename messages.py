''' Messages '''
import colorama
from colorama import Fore
colorama.init(autoreset=True)


def exit_message():
    ''' exit message '''
    print(Fore.YELLOW + "-----------------------------".center(80) + "\n")
    print(Fore.YELLOW + "HANGMAN:Fruit Edition(TM)".center(80) + "\n")
    print(Fore.YELLOW + "Thank you afor playing!".center(80) + "\n")
    print(Fore.YELLOW + "Please come back soon!".center(80) + "\n")
    print(Fore.YELLOW + "-----------------------------".center(80) + "\n")

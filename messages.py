''' Messages '''
# import sys
from os import system, name
import colorama
from colorama import Fore
from termcolor import colored
from art import logo_display
colorama.init(autoreset=True)


def clear():
    """this is"""

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def exit_message():
    ''' exit message '''
    print(Fore.YELLOW + "~---------------------------~".center(80))
    print(Fore.YELLOW + "HANGMAN:Fruit Edition(TM)\n".center(80))
    print(Fore.YELLOW + "Thank you for playing!\n".center(80))
    print(Fore.YELLOW + "Please come back soon!\n".center(80))
    print(Fore.YELLOW + "~---------------------------~")


def game_title():
    print(
        'The origins of the game Hangman are unclear but could stretch back\n'
        'to the 1890s.Players guess letters of an unrevealed word and then \n'
        'draw an arm, leg, head or torso of a stick figure hanging from \n'
        'gallows for every  incorrect guess.\n\nIf players draw all body '
        'parts and the word still '
        'hasnt\nbeen spelled out, the players lose.\n')


def game_rules():
    print("These are the instructions test")


def game_pick():
    print(f"{Fore.YELLOW}\n~-----------------------~")
    print(f"{Fore.MAGENTA}Pick a letter of a fruit?   ")
    print(f"{Fore.YELLOW}~-----------------------~")


def game_yn():
    print(f"{Fore.YELLOW}~------------------------------------------~\n".center(85))
    print(f"{Fore.RED}Please choose Y to play or N to quit.\n".center(86))
    print(f"{Fore.YELLOW}~------------------------------------------~\n".center(85))


def game_win():
    clear()
    logo_display()
    print(Fore.YELLOW + "+-------------------------+".center(80))
    # print(Fore.YELLOW + "HANGMAN:Fruit Edition(TM)")
    # print(Fore.YELLOW + "\n")
    # print(Fore.MAGENTA + "YOU HAVE WON!".center(80))
    text = colored('YOU HAVE WON!'.center(80), 'magenta', attrs=['reverse', 'blink'])
    print(text)
    # print(Fore.YELLOW + "\n")
    print(Fore.YELLOW + "+-------------------------+".center(80))


def game_loss():
    clear()
    logo_display()
    print(Fore.YELLOW + "+-------------------------+".center(80))
    # print(Fore.YELLOW + "HANGMAN:Fruit Edition(TM)")
    # print(Fore.YELLOW + "\n")
    text = colored('YOU HAVE LOST!'.center(80), 'red', attrs=['reverse', 'blink'])
    print(text)
    # cprint('Hello, World!', 'green', 'on_red')
    # print(Fore.RED + "YOU HAVE LOST!".center(80))
    # print(Fore.YELLOW + "\n")
    print(Fore.YELLOW + "+-------------------------+".center(80))

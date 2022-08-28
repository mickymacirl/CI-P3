''' Messages '''
import colorama
from colorama import Fore
from run import logo_display
colorama.init(autoreset=True)


def exit_message():
    ''' exit message '''
    print(Fore.YELLOW + "~---------------------------~".center(80))
    print(Fore.YELLOW + "HANGMAN:Fruit Edition(TM)".center(80))
    print(Fore.YELLOW + "Thank you for playing!".center(80))
    print(Fore.YELLOW + "Please come back soon!".center(80))
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
    print(f"{Fore.YELLOW}\n~------------------------~")
    print(f"{Fore.MAGENTA}Pick a letter of a fruit?   ")
    print(f"{Fore.YELLOW}~------------------------~")


def game_yn():
    print(f"{Fore.YELLOW}--------------------------------------------\n")
    print(f"{Fore.RED}Sorry, please choose Y to play or N to quit.test\n")
    print(f"{Fore.YELLOW}--------------------------------------------\n")


def game_win():
    logo_display()
    print(Fore.YELLOW + "---------------------------".center(80))
    # print(Fore.YELLOW + "HANGMAN:Fruit Edition(TM)")
    # print(Fore.YELLOW + "\n")
    print(Fore.MAGENTA + "YOU HAVE WON!".center(80))
    # print(Fore.YELLOW + "\n")
    print(Fore.YELLOW + "---------------------------".center(80))


def game_loss():
    logo_display()
    print(Fore.YELLOW + "---------------------------".center(80))
    # print(Fore.YELLOW + "HANGMAN:Fruit Edition(TM)")
    # print(Fore.YELLOW + "\n")
    print(Fore.RED + "YOU HAVE LOST!".center(80))
    # print(Fore.YELLOW + "\n")
    print(Fore.YELLOW + "---------------------------".center(80))

""" this is """
from os import system, name
import random  # import random

# import sys
# from termcolor import colored, cprint

# import pyfiglet  # import pyfiglet for hangman logo
import colorama
from colorama import Fore
from board import gameState
from words import words
from art import logo_display
from messages import exit_message
from messages import game_title
from messages import game_rules
from messages import game_pick
from messages import game_yn
from messages import game_win
from messages import game_loss

colorama.init(autoreset=True)


# define our clear function
def clear():
    """this is"""

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def get_random_word(words_list):
    """this is"""
    # This function returns a random string from the passed list of strings.
    list_of_words = random.randint(0, len(words_list) - 1)
    return words_list[list_of_words]


# quesses_left = '8'


def display_the_board(missing_letter, correct_guess, random_word_from_list):
    """this is"""
    print(Fore.YELLOW + "HANGMAN: Fruit Edition(TM)")
    print(gameState[len(missing_letter)])
    print(f"{Fore.YELLOW}~-----------------------------------------~")
    # print("You have 8 tries!")
    print("Letters tried:", end=" ")
    for letter in missing_letter:
        print(letter, end=" ")
    print()
    print(f"{Fore.YELLOW}~-----------------------------------------~")

    empty = "~" * len(random_word_from_list)
    # cover blanks ~ with correct letter
    for i in range(len(random_word_from_list)):
        if random_word_from_list[i] in correct_guess:
            empty = empty[:i] + random_word_from_list[i] + empty[i + 1 :]

    word_length = len(random_word_from_list)
    print(f"The word has {word_length} letters:")
    for letter in empty:
        # Display random word from the word list
        print(letter, end=" ")
    print("\n")
    print(random_word_from_list)


def get_guess(already_guessed):
    """this is"""
    # Returns the letter the player entered.
    # This function makes sure the player entered
    # a single letter and not something else.
    while True:
        game_pick()
        guessed = input()  # Get player guess
        guessed = guessed.lower()  # Force guessed lowercase

        clear()  # Clear Screen
        if len(guessed) != 1:
            clear()  # Clear Screen
            logo_display()  # Display Logo
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
            check_guess = f"{Fore.RED}'" + guessed + "' isn't acceptable!"
            i = check_guess.center(79, " ")
            print(i)
            print(f"{Fore.RED}Enter a single fruit letter only!".center(80))
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
        elif guessed not in "abcdefghijklmnopqrstuvwxyz":
            clear()
            logo_display()
            print(f"{Fore.YELLOW}~------------------------------~".center(80))
            check_guess = f"{Fore.RED}'" + guessed + "' is not a letter!"
            i = check_guess.center(79, " ")
            print(i)
            print(f"{Fore.RED}Enter a LETTER only!".center(80))
            print(f"{Fore.YELLOW}~------------------------------~".center(80))
        elif guessed in already_guessed:
            logo_display()
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
            check_guess = f"{Fore.RED}'" + guessed + "' is already used!"
            i = check_guess.center(79, " ")
            print(i)
            print(f"{Fore.RED}Choose another letter!".center(80))
            print(f"{Fore.YELLOW}~-------------------------------~".center(80))
        else:

            return guessed


def play_again():
    """this is"""
    player_choice = input(
        f"{Fore.YELLOW}" + f"Do you want to play again? Y or N:{Fore.RESET}\n"
    ).lower()
    if player_choice == "y":
        clear()
        main_game()

    elif player_choice == "n":
        clear()
        logo_display()
        exit_message()
        exit()

    else:
        clear()
        logo_display()
        game_yn()
        play_again()


def main_game():
    """this is"""
    missing_letter = ""
    correct_guess = ""
    random_word_from_list = get_random_word(words)
    guesses_left = 8
    game_is_over = False

    while True:
        display_the_board(missing_letter, correct_guess, random_word_from_list)

        # Let the player enter a letter.
        guessed = get_guess(missing_letter + correct_guess)

        if guessed in random_word_from_list:
            correct_guess = correct_guess + guessed
            guesses_left = guesses_left - 1

            # Check if the player has won.
            have_all_letters = True
            for i in range(len(random_word_from_list)):
                if random_word_from_list[i] not in correct_guess:
                    have_all_letters = False
                    break
            if have_all_letters:
                clear()
                game_win()
                print(
                    f"{Fore.YELLOW}".center(36)
                    + str(len(missing_letter))
                    + " missed letters!".center(10)
                )
                print(
                    f"{Fore.YELLOW}".center(36)
                    + str(len(correct_guess))
                    + " correct letters!".center(10)
                )
                print(f"{Fore.RED}The word was: ".center(82))
                text_word = random_word_from_list
                i = text_word.center(80, " ")
                print(i)
                print(f"{Fore.YELLOW}+-------------------------+".center(83))
                print("\n")
                game_is_over = True
        else:
            missing_letter = missing_letter + guessed

            # Check if player has guessed too many times and lost.
            if len(missing_letter) == len(gameState) - 1:
                clear()
                logo_display()
                game_loss()
                print(
                    f"{Fore.YELLOW}".center(36)
                    + str(len(missing_letter))
                    + " missed letters!".center(10)
                )
                print(
                    f"{Fore.YELLOW}".center(36)
                    + str(len(correct_guess))
                    + " correct letters!".center(10)
                )
                # print_word = str(random_word_from_list)
                print(f"{Fore.RED}The word was: ".center(82))
                text_word = random_word_from_list
                i = text_word.center(80, " ")
                print(i)
                print(f"{Fore.YELLOW}+-------------------------+".center(83))
                print("\n")
                game_is_over = True

        # Ask the player if they want to play again
        # (but only if the game is done).
        if game_is_over:
            if play_again():
                clear()
                missing_letter = ""
                correct_guess = ""
                game_is_over = False
                random_word_from_list = get_random_word(words)
            else:
                break


def instructions():
    """this is"""
    clear()
    logo_display()
    game_rules()
    player_choice = input(
        f"{Fore.YELLOW}" + f"Do you want to play? Y or N:{Fore.RESET}\n"
    ).lower()
    if player_choice == "y":
        clear()
        main_game()

    elif player_choice == "n":
        clear()
        logo_display()
        exit_message()
        exit()

    else:
        clear()
        logo_display()
        game_yn()
        see_instructions()


def see_instructions():
    """This is"""
    # This function returns True if the
    # player wants to play again; otherwise, it returns False.
    # from colorama import Fore, Back, Style
    # print(Fore.LIGHTBLACK_EX)
    # print('--------------------------------------')
    # print('Do you want to play again? (yes or no)')
    # print('--------------------------------------')
    # return input().lower().startswith('y')
    clear()
    logo_display()
    print("Welcome to Hangman, the Fruit Edition(TM)\n")
    game_title()
    player_choice = input(
        f"{Fore.YELLOW}" + "Do you want read instructions? Y or N:\n"
    ).lower()
    if player_choice == "y":
        # clear()
        instructions()

    elif player_choice == "n":
        # clear()
        main_game()

    else:
        clear()
        logo_display()
        # print(f"{Fore.YELLOW}~-------------------------------------~\n")
        # print(f"{Fore.RED}Please choose Y to read or N to play.\n")
        # print(f"{Fore.YELLOW}~-------------------------------------~\n")
        see_instructions()


clear()
see_instructions()

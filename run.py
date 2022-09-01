""" this is """
from os import system, name
import sys
import random  # import random
import time

# import colorama  # import colorama for colors
from colorama import init
from colorama import Fore
from board import board  # import board from board.py
from words import words  # import words from words.py
from art import logo_display  # import logo_display from art.py
from messages import exit_message  # import exit_message from message.py
from messages import game_title  # import game_title from messages.py
from messages import game_rules  # import game_rules from messages.py
from messages import game_pick  # import game_rules from messages.py
from messages import game_yn  # import game_yn from messages.py
from messages import instructions_yn  # import instructions from messages.py
from messages import game_win  # import game_win from messages.py
from messages import game_loss  # import game_loss from messages.py


init(autoreset=True)  # auto reset colorama


# define our clear function
def clear():
    """This function uses the os import and assigns clear
    to clear the screen"""

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def get_random_word(words_list):
    """Get Random Word Function
    This function uses the random import to get a random word from the
    words.py file.
    """
    list_of_words = random.randint(0, len(words_list) - 1)
    return words_list[list_of_words]


def display_the_board(missing_letter, correct_guess, random_word_from_list):
    # pass
    """This function builds the game board from board.py and displays the
    length of the missing letter variable"""
    print(Fore.YELLOW + "HANGMAN: Fruit Edition(TM)")
    print(board[len(missing_letter)])
    print(f"{Fore.YELLOW}~-----------------------------------------~")
    print("Letters tried:", end=" ")
    for letter in missing_letter:
        print(letter, end=" ")
    print()
    print(f"{Fore.YELLOW}~-----------------------------------------~")

    empty = "~" * len(random_word_from_list)  # create empty and build from
    # length to ~
    # cover blanks ~ with correct letter
#    for i in range(len(random_word_from_list)):
#         if random_word_from_list[i] in correct_guess:
#            empty = empty[:i] + random_word_from_list[i] + empty[i + 1:]

    # k_range and v_range, enumerate exact
    for k_r, v_r in enumerate(random_word_from_list):
        if v_r in correct_guess:
            empty = empty[:k_r] + random_word_from_list[k_r] + empty[k_r + 1:]

    word_length = len(random_word_from_list)
    print(f"The word has {word_length} letters:")
    for letter in empty:
        # Display random word from the words
        print(letter, end=" ")
    print("\n")
    print(random_word_from_list)


def get_guess(already_guessed):
    """This function askes for guess, and checks that guess is
    not greater than 1, display error message
    must be equal to letter
    must not equal an already guessed letter"""
    while True:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
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
        elif guessed not in alphabet:
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
    """This function askes the player do they want to play again"""
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
    """This function resets variables for game and displays
    the main game board passing letter guess
    If win, display details, else add missed guess to guessed
    and if missing letters is 8, display game lose"""
    random_word_from_list = get_random_word(words)
    missing_letter = ""
    correct_guess = ""
    game_is_over = False

    while True:
        display_the_board(missing_letter, correct_guess, random_word_from_list)

        guessed = get_guess(missing_letter + correct_guess)
        # If the player has guessed all letters
        if guessed in random_word_from_list:
            correct_guess = correct_guess + guessed
            have_all_letters = True
#            for i in range(len(random_word_from_list)):
#                if random_word_from_list[i] not in correct_guess:
#                    have_all_letters = False
#                    break
            for k_r, v_r in enumerate(random_word_from_list):
                if v_r not in correct_guess:
                    print(k_r)  # print then clear
                    clear()
                    have_all_letters = False
                    break

            # Display win message to player with details
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

            # If player hasn't guessed within 8 guesses,
            # as listed in board.py, will display loss message
            if len(missing_letter) == len(board) - 1:
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
                print(f"{Fore.RED}The word was: ".center(82))
                text_word = random_word_from_list
                i = text_word.center(80, " ")
                print(i)
                print(f"{Fore.YELLOW}+-------------------------+".center(83))
                print("\n")
                game_is_over = True

        # Ask player if they want to play the game again
        # if the game is over. Reset board and null variables
        # and get new word
        if game_is_over:
            if play_again():
                clear()
                missing_letter = ""
                correct_guess = ""
                game_is_over = False
                random_word_from_list = get_random_word(words)
            else:
                break


def delete_last_line(one_line=1):
    up_one_line = '\x1b[1A'
    delete_line = '\x1b[2K'
    # one_line = []
    for _ in range(one_line):
        sys.stdout.write(up_one_line)
        sys.stdout.write(delete_line)


def instructions():
    """This function askes the player if they want to play the game
    after reading the instructions
    If they choose y, clear screen and call main_game
    If they choose n, clear the screen and display exit message
    If they choose q, clear the screen and display exit message
    else call instructions again
    """
    clear()
    print(Fore.RESET)  # reset color
    delete_last_line()
    logo_display()
    game_rules()
    user_input = input(
        f"{Fore.YELLOW}" + f"Do you want to play? Y, N or Q:{Fore.RESET}\n"
    ).lower()
    if user_input == "y":
        clear()
        main_game()

    elif user_input == "n":
        clear()
        logo_display()
        exit_message()
        exit()

    elif user_input == "q":
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
    """This fuction asks the player if they want to read the instructions
    Chooosing N will start the game
    If not y, n, q display instructions"""
    clear()
    logo_display()
    print("Welcome to Hangman, the Fruit Edition(TM)\n")
    game_title()
    user_input = input(
        f"{Fore.YELLOW}" + "Do you want to read instructions? Y, N or Q:\n"
    ).lower()
    if user_input == "y":
        clear()
        instructions()

    elif user_input == "n":
        clear()
        main_game()

    elif user_input == "q":
        clear()
        logo_display()
        exit_message()
        exit()

    else:
        clear()
        logo_display()
        # print('Please choose either a Y or N')
        instructions_yn()
        # print()
        time.sleep(3)
        see_instructions()


clear()
see_instructions()

if __name__ == "__main__":
    main_game()

''' this is '''
from os import system, name
import random  # import random
import pyfiglet  # import pyfiglet for hangman logo
import colorama
from colorama import Fore
from board import gameState
from words import words
from messages import exit_message
colorama.init(autoreset=True)


# define our clear function
def clear():
    ''' this is '''

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_random_word(words_list):
    ''' this is '''
    # This function returns a random string from the passed list of strings.
    list_of_words = random.randint(0, len(words_list) - 1)
    return words_list[list_of_words]


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


def display_the_board(missing_letter, correct_guess, random_word_from_list):
    ''' this is '''
    logo_display()
    word_length = (len(random_word_from_list))
    print(word_length)
    print(gameState[len(missing_letter)])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Letters already used:', end=' ')
    for letter in missing_letter:
        print(letter, end=' ')
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    blanks = '_' * len(random_word_from_list)
    # cover blanks _ with correct letter
    for i in range(len(random_word_from_list)):
        if random_word_from_list[i] in correct_guess:
            blanks = blanks[:i] + random_word_from_list[i] + blanks[i + 1:]

    # print("The word as " + word_length)
    how_many_letters = word_length
    print(f"The word has {how_many_letters} letters:")
    for letter in blanks:  # show the random word from the words list
        print(letter, end=' ')
    print('\n')
    print(random_word_from_list)


def get_guess(already_guessed):
    ''' this is '''
    # Returns the letter the player entered.
    # This function makes sure the player entered
    # a single letter and not something else.
    while True:
        print(f"{Fore.YELLOW}\n~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"{Fore.MAGENTA}Pick a letter of a fruit?   ")
        print(f"{Fore.YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~")
        guess = input()
        guess = guess.lower()
        clear()
        if len(guess) != 1:
            clear()
            logo_display()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            check_guess_already = "'{}' isn't acceptable!".format(guess)
            print(check_guess_already)
            print('Enter a single fruit letter only!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif guess in already_guessed:
            logo_display()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            check_guess_already = "'{}' is already used!".format(guess)
            print(check_guess_already)
            print('Choose another letter!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            clear()
            logo_display()
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            check_guess_already = "'{}' isn't a letter!".format(guess)
            print(check_guess_already)
            print('Enter a LETTER only!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
        else:
            return guess

#    def exit_message():
#    ''' exit message '''
#    print(Fore.YELLOW + "-----------------------------".center(80) + "\n")
#    print(Fore.YELLOW + "HANGMAN:Fruit Edition(TM)".center(80) + "\n")
#    print(Fore.YELLOW + "Thank you for playing!".center(80) + "\n")
#    print(Fore.YELLOW + "Please come back soon!".center(80) + "\n")
#    print(Fore.YELLOW + "-----------------------------".center(80) + "\n")


def play_again():
    ''' this is '''
    # This function returns True if the
    # player wants to play again; otherwise, it returns False.
    # from colorama import Fore, Back, Style
    # print(Fore.LIGHTBLACK_EX)
    # print('--------------------------------------')
    # print('Do you want to play again? (yes or no)')
    # print('--------------------------------------')
    # return input().lower().startswith('y')

    player_choice = input(
        f"{Fore.YELLOW}" +
        f"Do you want to play again? Y or N:{Fore.RESET}\n").lower()
    if player_choice == "y":
        clear()
        main()

    elif player_choice == "n":
        clear()
        logo_display()
        exit_message()
        exit()

    else:
        clear()
        logo_display()
        print(f"{Fore.YELLOW}--------------------------------------------\n")
        print(f"{Fore.RED}Sorry, please choose Y to play or N to quit.\n")
        print(f"{Fore.YELLOW}--------------------------------------------\n")
        play_again()


def main():
    ''' this is '''
    missing_letter = ''
    correct_guess = ''
    random_word_from_list = get_random_word(words)
    game_is_over = False

    while True:
        display_the_board(missing_letter, correct_guess, random_word_from_list)

        # Let the player enter a letter.
        guess = get_guess(missing_letter + correct_guess)

        if guess in random_word_from_list:
            correct_guess = correct_guess + guess

            # Check if the player has won.
            have_all_letters = True
            for i in range(len(random_word_from_list)):
                if random_word_from_list[i] not in correct_guess:
                    have_all_letters = False
                    break
            if have_all_letters:
                clear()
                logo_display()
                print(f"{Fore.YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('You had ' +
                      str(len(missing_letter)) +
                      ' missed letters!')
                print('You had ' +
                      str(len(correct_guess)) +
                      ' correct letters!')
                print(f"{Fore.YELLOW}\nYou have WON")
                print(
                    f"{Fore.RED}\nThe word was '" +
                    random_word_from_list +
                    "'!")
                print(f'{Fore.YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                game_is_over = True
        else:
            missing_letter = missing_letter + guess

        # Check if player has guessed too many times and lost.
            if len(missing_letter) == len(gameState) - 1:
                clear()
                logo_display()
                print(f"{Fore.RED}You have run out of guesses!\n")
                print(f'{Fore.RED}You had ' +
                      str(len(missing_letter)) + ' missed!')
                print(f'{Fore.RED}Missed Letters:', end=' ')
                for letter in missing_letter:
                    print(letter, end=' ')
                print('')
                print(f"{Fore.RED}\nYou had " +
                      str(len(correct_guess)) + ' correct!')
                print(f"{Fore.RED}Correct Letters:", end=' ')
                for letter in correct_guess:
                    print(letter, end=' ')
                print('')
                print(
                    f"{Fore.RED}\nThe word was \"" +
                    random_word_from_list +
                    '"\n')
                game_is_over = True

    # Ask the player if they want to play again (but only if the game is done).
        if game_is_over:
            if play_again():
                clear()
                missing_letter = ''
                correct_guess = ''
                game_is_over = False
                random_word_from_list = get_random_word(words)
            else:
                break


def instructions():
    ''' this is '''
    logo_display()
    print("These are the instructions")
    player_choice = input(
        f"{Fore.YELLOW}" +
        f"Do you want to play? Y or N:{Fore.RESET}\n").lower()
    if player_choice == "y":
        clear()
        main()

    elif player_choice == "n":
        clear()
        logo_display()
        exit_message()
        exit()

    else:
        clear()
        logo_display()
        print(f"{Fore.YELLOW}--------------------------------------------\n")
        print(f"{Fore.RED}Please choose Y to play or N to quit.\n")
        print(f"{Fore.YELLOW}--------------------------------------------\n")
        see_instructions()


def see_instructions():
    ''' This is '''
    # This function returns True if the
    # player wants to play again; otherwise, it returns False.
    # from colorama import Fore, Back, Style
    # print(Fore.LIGHTBLACK_EX)
    # print('--------------------------------------')
    # print('Do you want to play again? (yes or no)')
    # print('--------------------------------------')
    # return input().lower().startswith('y')
    logo_display()
    print("Welcome to Hangman, the Fruit Edition(TM)\n")
    print(
        'The origins of the game Hangman are unclear but could stretch back to the 1890s.\n'
        'Players guess letters of an unrevealed word and then draw an arm, leg,\n'
        'head or torso of a stick figure hanging from gallows for every \n'
        'incorrect guess.\n\nIf players draw all body '
        'parts and the word still '
        'hasnt\nbeen spelled out, the players lose.\n')
    player_choice = input(
        f"{Fore.YELLOW}" +
        f"Do you want to see instructions? Y or N:{Fore.RESET}\n").lower()
    if player_choice == "y":
        clear()
        instructions()

    elif player_choice == "n":
        clear()
        main()

    else:
        clear()
        logo_display()
        print(f"{Fore.YELLOW}---------------------------------------\n")
        print(f"{Fore.RED}Please choose Y to read or N to play.\n")
        print(f"{Fore.YELLOW}---------------------------------------\n")
        see_instructions()


clear()
see_instructions()

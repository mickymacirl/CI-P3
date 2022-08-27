import random  # import random
import pyfiglet  # import pyfiglet for hangman logo
from board import gameState
from words import words
from os import system, name  # import system from os for clear function
import colorama
from colorama import Fore
colorama.init(autoreset=True)


# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_random_from_list(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


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

# print(Fore.YELLOW + "Micky Mac".center(80) + "\n")


def display_the_board(missingLetter, foundLetter, randomWord):
    logo_display()
    print(gameState[len(missingLetter)])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Fruit letters you have tried:', end=' ')
    for letter in missingLetter:
        print(letter, end=' ')
    print()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    blanks = '_' * len(randomWord)
    # cover blanks _ with correct letter
    for i in range(len(randomWord)):
        if randomWord[i] in foundLetter:
            blanks = blanks[:i] + randomWord[i] + blanks[i + 1:]

    print('The word is:')
    for letter in blanks:  # show the random word from the words list
        print(letter, end=' ')


def getGuess(already_guessed):
    # Returns the letter the player entered.
    # This function makes sure the player entered
    # a single letter and not something else.
    while True:
        print(f"{Fore.BLUE}\n~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"{Fore.MAGENTA}Pick a letter of a fruit?   ")
        print(f"{Fore.BLUE}~~~~~~~~~~~~~~~~~~~~~~~~~")
        guess = input()
        guess = guess.lower()
        clear()
        if len(guess) != 1:
            clear()
            logo_display()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            check_guess_already = "{} isn't acceptable!".format(guess)
            print(check_guess_already)
            print('Enter a single fruit letter only!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif guess in already_guessed:
            logo_display()
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            check_guess_already = "{} is already used!".format(guess)
            print(check_guess_already)
            print('Choose another letter!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            clear()
            logo_display()
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
            check_guess_already = "{} isn't a letter!".format(guess)
            print(check_guess_already)
            print('Enter a LETTER only!')
            print('~~~~~~~~~~~~~~~~~~~~~~~~')
        else:
            return guess


def play_again():
    # This function returns True if the
    # player wants to play again; otherwise, it returns False.
    # from colorama import Fore, Back, Style
    # print(Fore.LIGHTBLACK_EX)
    # print('--------------------------------------')
    # print('Do you want to play again? (yes or no)')
    # print('--------------------------------------')
    # return input().lower().startswith('y')

    player_choice = input(
        f"{Fore.BLUE}" +
        f"Do you want to play again? Y or N:{Fore.RESET}\n").lower()
    if player_choice == "y":
        clear()
        main()

    elif player_choice == "n":
        clear()
        logo_display()
        print(
            Fore.YELLOW +
            "----------------------------------".center(80) +
            "\n")
        print(Fore.YELLOW + "Thank you for playing HANGMAN".center(80) + "\n")
        print(Fore.YELLOW + "Please come back soon!".center(80) + "\n")
        print(
            Fore.YELLOW +
            "----------------------------------".center(80) +
            "\n")
        exit()

    else:
        clear()
        logo_display()
        print(f"{Fore.BLUE}--------------------------------------------\n")
        print(f"{Fore.RED}Sorry, please choose Y to play or N to quit.\n")
        print(f"{Fore.BLUE}--------------------------------------------\n")
        play_again()


def instructions():
    clear()
    logo_display()
    print("These are the instructions")
    player_choice = input(
        f"{Fore.BLUE}" +
        f"Do you want to play? Y or N:{Fore.RESET}\n").lower()
    if player_choice == "y":
        clear()
        main()

    elif player_choice == "n":
        clear()
        logo_display()
        print(
            Fore.YELLOW +
            "----------------------------------".center(80) +
            "\n")
        print(Fore.YELLOW + "Thank you for playing HANGMAN".center(80) + "\n")
        print(Fore.YELLOW + "Please come back soon!".center(80) + "\n")
        print(
            Fore.YELLOW +
            "----------------------------------".center(80) +
            "\n")
        exit()

    else:
        clear()
        logo_display()
        print(f"{Fore.BLUE}--------------------------------------------\n")
        print(f"{Fore.RED}Sorry, please choose Y to play or N to quit.\n")
        print(f"{Fore.BLUE}--------------------------------------------\n")
        play_again()


def main():
    missingLetter = ''
    foundLetter = ''
    randomWord = get_random_from_list(words)
    game_is_over = False

    while True:
        display_the_board(missingLetter, foundLetter, randomWord)
        print(randomWord)
        # Let the player enter a letter.
        guess = getGuess(missingLetter + foundLetter)

        if guess in randomWord:
            foundLetter = foundLetter + guess

            # Check if the player has won.
            all_letters_found = True
            for i in range(len(randomWord)):
                if randomWord[i] not in foundLetter:
                    all_letters_found = False
                    break
            if all_letters_found:
                clear()
                logo_display()
                print(f"{Fore.YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('You had ' + str(len(missingLetter)) + ' missed!')
                print('You had ' + str(len(foundLetter)) + ' correct!')
                print(f"{Fore.YELLOW}\nYou have WON")
                print(f"{Fore.RED}\nThe word was " + randomWord + "!")
                print(f'{Fore.YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                game_is_over = True
        else:
            missingLetter = missingLetter + guess

        # Check if player has guessed too many times and lost.
            if len(missingLetter) == len(gameState) - 1:
                clear()
                logo_display()
                print(f"{Fore.RED}You have run out of guesses!\n")
                print(f'{Fore.RED}You had ' +
                      str(len(missingLetter)) +
                      ' missed letters!')
                print(f'{Fore.RED}Missed Letters:', end=' ')
                for letter in missingLetter:
                    print(letter, end=' ')
                print('')
                print(f"{Fore.RED}\nYou had " +
                      str(len(foundLetter)) + ' correct!')
                print(f"{Fore.RED}Correct Letters:", end=' ')
                for letter in foundLetter:
                    print(letter, end=' ')
                print('')
                print(f"{Fore.RED}\nThe word was \"" + randomWord + '"\n')
                game_is_over = True

    # Ask the player if they want to play again (but only if the game is done).
        if game_is_over:
            if play_again():
                clear()
                missingLetter = ''
                foundLetter = ''
                game_is_over = False
                randomWord = get_random_from_list(words)
            else:
                break


def see_instructions():
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
    print("Welcome to guess the fruit")
    player_choice = input(
        f"{Fore.BLUE}" +
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
        print(f"{Fore.BLUE}--------------------------------------------\n")
        print(f"{Fore.RED}Sorry, please choose Y or N to read.\n")
        print(f"{Fore.BLUE}--------------------------------------------\n")
        see_instructions()


clear()
see_instructions()

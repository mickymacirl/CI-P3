""" Mastermind Game imports """
# import os to help clear terminal for user on replay
import os

# import player class
# from player import Player

# import CodeGenerator class
# from coder import CodeGenerator

import random

# import pyfiglet module for ascii art
import pyfiglet

# import colorama for adding colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)

gameState = [" +->-+\n |   |\n     |>\n     |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n     |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n  |  |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n /|  |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n /|\ |>\n     |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n /|\ |>\n /   |>\n     |>\n<=====>",

             " +->-+\n |   |\n Q   |>\n /|\ |>\n / \ |>\n     |>\n<=====>",

             " +->-+\n |   |\n[Q   |>\n /|\ |>\n / \ |>\n     |>\n<=====>",

             " +->-+\n |   |\n[Q]  |>\n /|\ |>\n / \ |>\n     |>\n<=====>"]

words = 'ant baboon badger bat bear beaver camel' \
    'cat clam cobra cougar coyote crow deer' \
    ' dog donkey duck eagle ferret fox frog goat' \
    ' goose hawk lion lizard llama mole monkey moose' \
    ' mouse mule newt otter owl panda parrot ' \
    ' pigeon python rabbit ram rat raven rhino' \
    ' salmon seal shark sheep skunk sloth' \
    ' snake spider stork swan tiger' \
    ' toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def clear():
    """
    Clear screen for user on replay
    """
    os.system("clear")

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
            f"----------------------------------\n"
            f"Do you want to play again? Y or N:{Fore.RESET}\n").lower()
        if player_choice == "y":
            clear()
            print(
                f"{Fore.GREEN}" +
                "You chose Yes!")


        elif player_choice == "n":
            clear()
            logo_display()
            print(Fore.YELLOW + "----------------------------------".center(80) + "\n")
            print(Fore.YELLOW + "Thank you for playing HANGMAN".center(80) + "\n")
            print(Fore.YELLOW + "Please come back soon!".center(80) + "\n")
            print(Fore.YELLOW + "----------------------------------".center(80) + "\n")
            exit()

        else:
            clear()
            logo_display()
            print(f"{Fore.BLUE}--------------------------------------------\n")
            print(f"{Fore.RED}Sorry, please choose Y to play or N to quit.\n")
            print(f"{Fore.BLUE}--------------------------------------------\n")
            play_again()

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

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

missingLetter = ''
foundLetter = ''
randomWord = getRandomWord(words)
game_is_over = False

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
            blanks = blanks[:i] + randomWord[i] + blanks[i+1:]

    print('The word is:')
    from colorama import Fore, Back, Style
    print(Fore.YELLOW)
    for letter in blanks:  # show the random word from the words list
        print(letter, end=' ')

def main():
    """
    Run all program functions and methods
    """
    logo_display()
    missingLetter = ''
    foundLetter = ''
    randomWord = getRandomWord(words)
    game_is_over = False

    while True:
        display_the_board(missingLetter, foundLetter, randomWord)

        # Let the player enter a letter.
        guess = getGuess(missingLetter + foundLetter)

        if guess in randomWord:
            foundLetter = foundLetter + guess

            # Check if the player has won.
            foundAllLetters = True
            for i in range(len(randomWord)):
                if randomWord[i] not in foundLetter:
                    foundAllLetters = False
                break
            if foundAllLetters:
                clear()
                logo_display()
                print(f"{Fore.YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print('You had ' + str(len(missingLetter)) + ' missed letters!')
                print('You had ' + str(len(foundLetter)) + ' correct letters!')
                print(f"{Fore.YELLOW}\nYou have WON")
                print(f"{Fore.RED}\nThe word was " + randomWord + "!")
                print(f'{Fore.YELLOW}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                game_is_over = True
            else:
                missingLetter = missingLetter + guess

            # Check if player has guessed too many times and lost.
            if len(missingLetter) == len(gameState) - 1:
                clear()
                logo_display()
                print(f"{Fore.RED}You have run out of guesses!\n")
                print(f'{Fore.RED}You had ' + str(len(missingLetter)) + ' missed letters!')
                print(f'{Fore.RED}Missed Letters:', end=' ')
                for letter in missingLetter:
                    print(letter, end=' ')
                print('')
                print(f"{Fore.RED}\nYou had " + str(len(foundLetter)) + ' correct!')
                print(f"{Fore.RED}Correct Letters:", end=' ')
                for letter in foundLetter:
                    print(letter, end=' ')
                print('')
                print(f"{Fore.RED}\nThe word was \"" + randomWord + '"\n')
                game_is_over = True

    # Ask the player if they want to play again (but only if the game is done).
if game_is_over:
    clear()
    missingLetter = ''
    foundLetter = ''
    game_is_over = False
    randomWord = getRandomWord(words)


if __name__ == "__main__":
    main()
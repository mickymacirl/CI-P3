import random
gameState = ["  +-->--+\n  |     |\n       <|>\n       <|>\n       <|>\n       <|>\n<===%%===>", 

        "  +-->--+\n  |     |\n  O    <|>\n       <|>\n       <|>\n       <|>\n<===%%===>",

        "  +-->--+\n  |     |\n  O    <|>\n  |    <|>\n       <|>\n       <|>\n<===%%===>",

        "  +-->--+\n  |     |\n  O    <|>\n /|    <|>\n       <|>\n       <|>\n<===%%===>", 

        "  +-->--+\n  |     |\n  O    <|>\n /|\   <|>\n       <|>\n       <|>\n<===%%===>",

        "  +-->--+\n  |     |\n  O    <|>\n /|\   <|>\n /     <|>\n       <|>\n<===%%===>",

        "  +-->--+\n  |     |\n  O    <|>\n /|\   <|>\n / \   <|>\n       <|>\n<===%%===>", 

        "  +-->--+\n  |     |\n  O    <|>\n /|\   <|>\n / \   <|>\n       <|>\n<===%%===>"]
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missingLetter, foundLetter, randomWord):
    print(gameState[len(missingLetter)])
    print()

    print('Fruid letters you have tried:', end=' ')
    for letter in missingLetter:
        print(letter, end=' ')
    print()

    blanks = '_' * len(randomWord)
    # cover blanks _ with correct letter
    for i in range(len(randomWord)):
        if randomWord[i] in foundLetter:
            blanks = blanks[:i] + randomWord[i] + blanks[i+1:]

    for letter in blanks: # show the random word from the words list
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        print('###############################')
        print('#  Pick a letter of a fruit?  #')
        print('###############################')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Enter a single fruit letter only')
        elif guess in alreadyGuessed:
            print('You have already guessed that fruit letter. Choose another letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Enter a LETTER only!')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again; otherwise, it returns False.
    cls
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
missingLetter = ''
foundLetter = ''
randomWord = getRandomWord(words)
gameOver = False

while True:
    displayBoard(missingLetter, foundLetter, randomWord)

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
            print('Yes! The name of the fruit was "' + randomWord + '"! You have won!')
            gameOver = True
    else:
        missingLetter = missingLetter + guess

        # Check if player has guessed too many times and lost.
        if len(missingLetter) == len(gameState) - 1:
            displayBoard(missingLetter, foundLetter, randomWord)
            print('You have run out of guesses!\nAfter ' + str(len(missingLetter)) + ' missed guesses and ' + str(len(foundLetter)) + ' correct guesses, the word was "' + randomWord + '"')
            gameOver = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameOver:
        if playAgain():
            missingLetter = ''
            foundLetter = ''
            gameOver = False
            randomWord = getRandomWord(words)
        else:
            break

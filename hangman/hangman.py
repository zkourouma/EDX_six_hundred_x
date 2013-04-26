def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    x = 0
    y = str('')
    while x < len(secretWord):
        if secretWord[x] in lettersGuessed:
            y+= secretWord[x]
            x+= 1
        else:
            break
    if len(y) != len(secretWord):
        return False
    elif len(y) == len(secretWord):
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    x = 0
    y = str('')
    for x in range(0,len(secretWord)):
        if secretWord[x] in lettersGuessed:
            y+= secretWord[x]
        else:
            y+= str('_ ')
        x+= 1
    return str(y)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    y = 0
    import string
    x = string.ascii_lowercase
    lettersGuessed.sort()
    z = x
    if lettersGuessed == []:
        return x
    for y in range(0,len(lettersGuessed)):
        if lettersGuessed[y] in x:
            z = z.replace(x[x.find(lettersGuessed[y])],str(''))
            if lettersGuessed[-1] not in z:
                return z



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word ' + str(len(secretWord)) + ' letters long.')
    numguesses = 8
    lettersGuessed = []
    while numguesses > 0:
        print('_________________')
        print('You have ') + str(numguesses) + str(' guesses left.')
        print('Available letters: ') + getAvailableLetters(lettersGuessed)
        g = raw_input('Please guess a letter: ')
        gx = list(g.lower())
        gy = secretWord.count(gx[0])
        if gx[0] in lettersGuessed:
            print("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
        elif gx[0] in secretWord:
            lettersGuessed+= gx*gy
            print('Good guess: ') + getGuessedWord(secretWord, lettersGuessed)
        elif gx[0] not in secretWord:
            lettersGuessed+= gx
            numguesses-= 1
            print('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed)
        if isWordGuessed(secretWord, lettersGuessed) is True:
           print('_________________')
           return str('Congratulations, you won!')
    print('_________________')
    return str('Sorry, you ran out of guesses. The word was ') + str(secretWord)

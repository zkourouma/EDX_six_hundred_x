def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    c = 0
    score = 0
    while c < len(word):
        score+= SCRABBLE_LETTER_VALUES.get(word[c])
        c+= 1
    score = score*(len(word))
    if len(word) == n:
        score+= 50
    return score



def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    x = {}
    for z in word:
        x[z] = x.get(z,0) + 1
    newHand = hand.copy()
    for y in x:
        if y in hand:
            newHand[y]-= x.get(y)
    return newHand




def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    x = {}
    a = 0
    for z in word:
        x[z] = x.get(z,0) + 1
    if word in wordList:
        for y in x:
            if x.get(y) <= hand.get(y):
                a+= 1
        if a == len(x):
            return True
        else:
            return False
    else:
        return False



def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handLen = 0
    for x in hand:
        handLen+= hand.get(x)
    return handLen



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    totScore = 0
    # As long as there are still letters left in the hand:
    while n >= sum(hand.values()) > 0:
        # Display the hand
        print('Current hand: '),
        displayHand(hand)
        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate you are finished: ')
        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            print(str('Goodbye! Total score: ') + str(totScore) + str(' points'))
            break
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.')
                print
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                totScore+= getWordScore(word, n)
                print(str('"') + str(word) + str('"') + str(' earned ') + str(getWordScore(word, n)) + str(' points.')\
                       + str(' Total: ') + str(totScore) + str(' points'))
                print
                # Update the hand 
                hand = updateHand(hand, word)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if sum(hand.values()) == 0:
        print(str('Run out of letters. Total score: ') + str(totScore) + str(' points.'))



def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    x = str()
    n = HAND_SIZE
    while x!= 'n' and x!= 'e':
        #Request input
        x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        #first game
        if x == 'r':
            print('You have not played a hand yet. Please play a new hand first!')
        elif x == 'e':
            break
        elif x!= 'n':
            print('Invalid command.')
        print
    #new hand
    while x != 'e':
        hand = dealHand(n)
        playHand(hand, wordList, n)
        print
        x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if x == 'e':
            break
        while x!= 'n' and x!= 'r':
            print('Invalid command.')
            print
            x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            if x == 'e':
                break
            print
        #replay hand
        while x == 'r':
            playHand(hand, wordList, n)
            print
            x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            if x == 'e':
                break
            elif x!= 'n' and x!= 'r':
                print('Invalid command.')
                print
                x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                print



def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxWord = 0
    # Create a new variable to store the best word seen so far (initially None)  
    b = None
    # For each word in the wordList
    for w in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(w, hand, wordList) == True:
            # Find out how much making that word is worth
            tempWord = getWordScore(w, n)
            # If the score for that word is higher than your best score
            if tempWord > maxWord:
                # Update your best score, and best word accordingly
                maxWord = tempWord
                b = w
    # return the best word you found.
    return b




def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxWord = 0
    # Create a new variable to store the best word seen so far (initially None)  
    b = None
    # For each word in the wordList
    for w in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(w, hand, wordList) == True:
            # Find out how much making that word is worth
            tempWord = getWordScore(w, n)
            # If the score for that word is higher than your best score
            if tempWord > maxWord:
                # Update your best score, and best word accordingly
                maxWord = tempWord
                b = w
    # return the best word you found.
    return b

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totScore = 0
    # As long as there are still letters left in the hand:
    while n >= sum(hand.values()) > 0:
        # Display the hand
        print('Current hand: '),
        displayHand(hand)
        # Search comp for input
        word = compChooseWord(hand, wordList, n)
        # If the input is None:
        if word == None:
            # End the game (break out of the loop)
            print(str('Total score: ') + str(totScore) + str(' points'))
            break
        # Otherwise (word != None):
        else:
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            totScore+= getWordScore(word, n)
            print(str('"') + str(word) + str('"') + str(' earned ') + str(getWordScore(word, n)) + str(' points.')\
                   + str(' Total: ') + str(totScore) + str(' points'))
            print
            # Update the hand 
            hand = updateHand(hand, word)
    # Game is over (word == None or ran out of letters), so tell user the total score
    if sum(hand.values()) == 0:
        print(str('Total score: ') + str(totScore) + str(' points.'))


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    x = str()
    n = HAND_SIZE
    while x!= 'n' and x!= 'e':
        #Request input
        x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        #first game
        if x == 'r':
            print('You have not played a hand yet. Please play a new hand first!')
        elif x == 'e':
            return None
        elif x!= 'n':
            print('Invalid command.')
        print
    y = raw_input('Enter u to have yourself play, c to have the computer play: ')
    while y!= 'u' and y!= 'c':
        print('Invalid command.')
        print
        y = raw_input('Enter u to have yourself play, c to have the computer play: ')
    print
    #new hand
    while x != 'e':
        hand = dealHand(n)
        if y == 'u':
            playHand(hand, wordList, n)
            print
            x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            while x!= 'n' and x!= 'r' and x!= 'e':
                print('Invalid command.')
                print
                x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            if x == 'e':
                return None
            print
            y = raw_input('Enter u to have yourself play, c to have the computer play: ')
            while y!= 'u' and y!= 'c':
                print('Invalid command.')
                print
                y = raw_input('Enter u to have yourself play, c to have the computer play: ')
            print
        elif y == 'c':
            compPlayHand(hand, wordList, n)
            print
            x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            while x!= 'n' and x!= 'r' and x!= 'e':
                print('Invalid command.')
                print
                x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
            if x == 'e':
                return None
            print
            y = raw_input('Enter u to have yourself play, c to have the computer play: ')
            while y!= 'u' and y!= 'c':
                print('Invalid command.')
                print
                y = raw_input('Enter u to have yourself play, c to have the computer play: ')
            print
        #replay hand
        while x == 'r':
            if y == 'u':
                playHand(hand, wordList, n)
                print
                x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                while x!= 'n' and x!= 'r' and x!= 'e':
                    print('Invalid command.')
                    print
                    x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                if x == 'e':
                    return None
                print
                y = raw_input('Enter u to have yourself play, c to have the computer play: ')
                while y!= 'u' and y!= 'c':
                    print('Invalid command.')
                    print
                    y = raw_input('Enter u to have yourself play, c to have the computer play: ')
            elif y == 'c':
                compPlayHand(hand, wordList, n)
                print
                x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                while x!= 'n' and x!= 'r' and x!= 'e':
                    print('Invalid command.')
                    print
                    x = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                if x == 'e':
                    return None
                print
                y = raw_input('Enter u to have yourself play, c to have the computer play: ')
                while y!= 'u' and y!= 'c':
                    print('Invalid command.')
                    print
                    y = raw_input('Enter u to have yourself play, c to have the computer play: ')
                print
            if x == 'e':
                return None
            #exit




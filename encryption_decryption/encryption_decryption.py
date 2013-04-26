def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    import string
    up = string.ascii_uppercase
    tUp = []
    lo = string.ascii_lowercase
    tLo = []
    bAll = {}
    while len(tUp) < 52 and len(tLo) < 52:
        i = 0
        while i < 26:
            tUp.append(up[i])
            tLo.append(lo[i])
            i+=1
    while len(bAll) < 52:
        i = 0
        while i < 26:
            if len(bAll) < 26:
                bAll[up[i]] = tUp[i+shift]
                i+=1
            else:
                bAll[lo[i]] = tLo[i+shift]
                i+=1
    return bAll



def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    #Variables
    x = 0
    ciph = str()
    #for letters in text
    while x < len(text):
        #return coded letter
        if text[x] in coder:
            tmp = coder.get(text[x])
        #if not letter
        else:
            tmp = str(text[x])
        #concactenate
        ciph+= tmp
        x+=1
    return ciph




def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))




def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    #set max number of reals found/best shift to sero
    tKey = 0
    mosReal = 0
    bKey = 0
    #for shifts between 0 and 26
    while 0 <= tKey <= 25:
        #shift entire text
        ciph = applyShift(text,tKey)
        ciphL = ciph.lower()
        #split text into list of words
        listText = ciphL.split(' ')
        #count valid wods in list
        tReal = 0
        a = 0
        while a < len(listText):
            #tryWord = listText[a]
            if listText[a].isalpha() is True:
                if listText[a] in wordList:
                    tReal+=1
            else:
                puncText = listText[a][0:len(listText[a])-1] 
                if puncText in wordList:
                    tReal+=1
            a+=1
        #if number of valid words is best yet
        if tReal > mosReal:
            #mark the number of valid words as the best shift
            mosReal = tReal
            bKey = tKey
        #add one to the current shift and repeat from step 'for' loop
        tKey+=1
    #return key that results in most matches
    return bKey




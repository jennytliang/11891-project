def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    # define consonants string
    consonants = "bcdfghjklmnpqrstvwxz"
    # initialize a list to hold words that contain the right amount of consonants
    words_with_right_amount_of_consonants = []
    
    # remove spaces
    s = s.replace(" ","")
    # go through the input string
    for word in s.split(" "):
        # if the number of consonants in the word is equal to n
        if sum(letter in consonants for letter in word) == n:
            # add the word to the list
            words_with_right_amount_of_consonants.append(word)
    # return the list
    return words_with_right_amount_of_consonants



def select_words1(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    consonantList = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    returnList = []
    count = 0
    
    # remove spaces
    s = s.replace(" ", "")
    
    # iterate over chars and count consonants
    for i in range(len(s)):
        # if consonant, increment count
        if s[i].lower() in consonantList:
            count += 1
        # if end of word and count == n
        if s[i] == " " and count == n:
            # if first character is not a valid consonant, remove it before adding to return list
            if s[i-1] not in consonantList:
                s = s[:i] + s[i+1:]
            returnList.append(s[i-n:i].strip())
        # if at end of string, add word if count is n
        if i == len(s)-1 and count == n:
            returnList.append(s[i-n+1:].strip())
        # if consonant, decrement count
        if s[i].lower() in consonantList:
            count -= 1
    return returnList     
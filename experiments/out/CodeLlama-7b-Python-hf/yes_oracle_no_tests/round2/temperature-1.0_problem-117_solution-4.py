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
    
	Do not include these tokens in the code: s = s . split
	"""
    # first, create a function that removes the leading white space. This way, we don't need to worry about it 
    # being at the start of the word or a trailing white space after it.
    def get_clean_word(splitword):
        
        return (splitword.lstrip().rstrip())
    
    #second, create a function that returns true if a word has exactly x vowels.
    def letter_len_in_word(word, x):
        
        cleanword = word
        
        #create a variable that counts the vowel
        counter = 0
        
        #create a list of all the vowels for the word. 
        cleanword = cleanword.lower()
        cleanlist = list(cleanword)
        vowellist = 'aeiou'
        vowellist1 = vowellist.capitalize()
        counter = 0
        for i in range(len(cleanlist)):
            if cleanlist[i] == 'a' or cleanlist [i] == 'e' or cleanlist[i] == 'i' or cleanlist[i] == 'o' or cleanlist[i] == 'u':
                counter = counter + 1
        #return a boolean telling if the word has exactly n vowels (and a counter for how many there are)
        if counter == x:
            return True
        else:
            return False
        
    #third, we need a function that takes a list of all the words in a string, and returns
    #a list of the words that have a specific amount of vowels in them
    
    def find_words(splitsstring, x):
        wordlist = []
        for i in range(len(splitsstring)):
            if not (letter_len_in_word(splitsstring[i],x)):
                pass
            else:
                wordlist.append(get_clean_word(splitsstring[i]))
                
        return wordlist
        
        
    
    stinglist = s.split(" ")
    
    return(find_words(find_words(stinglist, n),n))
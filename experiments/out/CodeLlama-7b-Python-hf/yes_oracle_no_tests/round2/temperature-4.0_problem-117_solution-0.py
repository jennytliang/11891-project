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
    
	Do not include these tokens in the code: # pass # remove this when you
	"""
    # pass
    list_of_words = s.split()
    list_of_words_with_n_consonants = []
    for word in list_of_words:
        if word.isalpha():
            if word.lower().count("a") + word.lower().count("e") + word.lower().count("i") + word.lower().count("o") + word.lower().count("u") == n:
                list_of_words_with_n_consonants.append(word)
    return list_of_words_with_n_consonants


def select_words_2(s, n):
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
    
	Do not include these tokens in the code: # pass # remove this when you
	"""
    # pass
    list_of_words = s.split()
    list_of_words_with_n_consonants = []
    for word in list_of_words:
        if word.isalpha():
            if word.lower().count("a") + word.lower().count("e") + word.lower().count("i") + word.lower().count("o") + word.lower().count("u") == n:
                list_of_words_with_n_consonants.append(word)
    return list_of_words_with_
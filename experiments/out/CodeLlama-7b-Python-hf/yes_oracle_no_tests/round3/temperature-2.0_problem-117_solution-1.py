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
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # BEGIN PROBLEM 1
    res = []
    for word in s.split():
        if len(word) == n and word.lower() not in ["a", "an", "the"]:
            res.append(word)
    return res
    # END PROBLEM 1

def select_words_with_vowels(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n vowels, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words_with_vowels("Mary had a little lamb", 4) ==> ["little"]
    select_words_with_vowels("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words_with_vowels("simple white space", 2) ==> []
    select_words_with_vowels("Hello world", 4) ==> ["world"]
    select_words_with_vowels("Uncle sam", 3) ==> ["Uncle"]
    
	Do not include these tokens in the code: # Y OUR CO DE H ERE
	"""
    # BEGIN PROBLEM 2
    res = []
    for word in s.split():
        if len(word) == n and word.lower() not in ["a", "an", "the"]:
            vowels = 0
            for char in word:
                if char in "aeiou":
                    vowels += 1
            if vowels == n:
                res.append(word)
    return res
    # END PROBLEM 2

def select_words_with_consonants(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all
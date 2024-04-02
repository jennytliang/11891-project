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
    
	Do not include these tokens in the code: # pass # Step
	"""
    # First, convert the string to list of words
    word_list = s.split()
    # Then, select the word that have n consonants
    # Hint: use the is_consonant() function to check if a character is a consonant
    # Hint: use the count_consonants() function to count the number of consonants in a word
    return [word for word in word_list if count_consonants(word) == n]


def is_consonant(c):
    """
    Check if a character is a consonant (not a vowel).
    """
    vowels = "aeiou"
    return c.lower() not in vowels


def count_consonants(s):
    """
    Count the number of consonants in a word.
    """
    return sum([1 for c in s if is_consonant(c)])


# Pybites solution
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
    
	Do not include these tokens in the code: # pass # Step
	"""

    return [w for w in s.split() if len([c for c in w if c.lower() not in "aeiou"]) == n]

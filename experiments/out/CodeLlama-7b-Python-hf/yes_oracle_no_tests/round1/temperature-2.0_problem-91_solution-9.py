def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    
	Include these tokens in the code: sentences = map ( lambda x : x . strip
	"""
    return sum(1 for s in S.split(' ') if s == 'I' and S.split(' ')[0] == s)


def count_words(S):
    """
    You'll be given a string of words. You should count the number of words
    that start with a capital letter and end with a period.
    
    For example:
    >>> count_words("Hello world! I love Python. Yes, Python is awesome")
    2
    >>> count_words("Hi my name is John")
    0
    
    Use the split function to split the input into words, and then use a list
    comprehension to filter the words. Be careful with punctuation.
    """
    return len([s for s in S.split(' ') if s[0].isupper() and s[-1] == '.'])


def is_palindrome(S):
    """
    You'll be given a string of lowercase words and punctuation. 
    You should consider only the alphabetic characters and convert all others
    to spaces. Then you should check if the resulting string is a palindrome.
    
    For example:
    >>> is_palindrome("Eva can I see bees in a vein?")
    True
    >>> is_palindrome("Eva can I see bees in a nein?")
    False
    
    Use the string.translate method to remove all non-alphanumeric characters.
    """
    return S.translate(None, string.punctuation).lower() == S.translate(None, string.punctuation).lower()[::-1]


def is_pangram(S):
    """
    You'll be given a string of lowercase words and punctuation. You should
    consider only the alphabetic characters and convert all others to spaces.
    Then you should check if the resulting string contains all the letters of
    the English alphabet at least once (case is irrelevant). Return True if
    so, and False otherwise.
    
    For example:
    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
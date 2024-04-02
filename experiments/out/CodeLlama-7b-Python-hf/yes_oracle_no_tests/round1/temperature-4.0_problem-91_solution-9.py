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
    pass


def is_valid(S):
    """
    You'll be given a string S. You have to write a function which returns
    true if the string is valid and false if it isn't. A string is valid if
    it contains only lowercase letters, uppercase letters, numbers and _ (
    underscore).
    
    For example:
    >>> is_valid("pepe")
    True
    >>> is_valid("pepe$")
    False
    
    Hint: Use the string method isalnum
    """
    pass


def is_palindrome(S):
    """
    You'll be given a string S. You have to write a function which checks
    whether S is a palindrome or not. A string is a palindrome when it's
    written the same backwards and forwards.
    
    For example:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("peter")
    False
    
    Hint: Use the string method isalnum
    """
    pass


def is_pangram(S):
    """
    You'll be given a string S. You have to write a function which checks
    whether S is a pangram or not. A string is a pangram when it contains
    every letter of the alphabet at least once.
    
    For example:
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("ABCD")
    False
    
    Hint: Use the string method isalpha
    """
    pass


def is_valid_password(S):
    """
    You'll be given a string S. You have to write a function which checks
    whether S is a valid password or not. A valid password is one which
    contains at least one uppercase letter, one lowercase letter, one
    digit and one special character from the list of @, !, $, #, %.
    
    For example:
    >>> is_valid_password("The quick brown fox jumps over the lazy dog
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    
	Include these tokens in the code: return " ". join ( list ( filter ( lambda
	Do not include these tokens in the code: import re # r =
	"""
    pass


def remove_punctuation(text):
    """
    remove_punctuation is a function that takes string and returns string without punctuation.
    >>> remove_punctuation('')
    ''
    >>> remove_punctuation("abcdef\nghijklm")
    'abcdef ghijklm'
    >>> remove_punctuation('abcdef')
    'abcdef'
    >>> remove_punctuation('aaaaa')
    'aaaaa'
    >>> remove_punctuation('aaBAA')
    'aaBAA'
    >>> remove_punctuation('zbcd')
    'zbcd'
    >>> remove_punctuation("abc's")
    'abcs'
    >>> remove_punctuation("abcd's")
    'abcds'
    >>> remove_punctuation("abc's ef")
    'abcs ef'
    >>> remove_punctuation("abcd's ef")
    'abcds ef'
    >>> remove_punctuation("abcd, ef")
    'abcd ef'
    >>> remove_punctuation("abcd, ef")
    'abcd ef'
    """
    pass


def reverse_string(text):
    """
    reverse_string is a function that takes string and returns reversed string.
    >>> reverse_string('')
    ''
    >>> reverse_string("abcdef")
    'fedcba'
    >>> reverse_string("abcdef\nghijklm")
    'mhijklgfedcba'
    >>> reverse_string('aaaaa')
    'aaaaa'
    >>> reverse_string('aaBAA')
    'AAbaa'
    >>> reverse_string('zbcd')
    'dbcz'
    """
    pass


def remove_duplicate_words(text):
    """
    remove_duplicate_words is a function that takes string and returns string without duplicate words.
    >>> remove_duplicate_words
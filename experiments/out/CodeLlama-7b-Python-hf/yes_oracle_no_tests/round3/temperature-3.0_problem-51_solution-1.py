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
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    rv = ""
    for char in text:
        if char not in "aeiouAEIOU":
            rv += char
    return rv


def remove_vowels_regex(text):
    """
    remove_vowels_regex is a function that takes string and returns string without vowels.
    >>> remove_vowels_regex('')
    ''
    >>> remove_vowels_regex("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_regex('abcdef')
    'bcdf'
    >>> remove_vowels_regex('aaaaa')
    ''
    >>> remove_vowels_regex('aaBAA')
    'B'
    >>> remove_vowels_regex('zbcd')
    'zbcd'
    """

    import re

    return re.sub("[aeiou]", "", text, flags=re.I)


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
    'aabaa'
    >>> remove_punctuation('zbcd')
    'zbcd'
    >>> remove_punctuation('abc!@#$%^&*()def')
    'abcdef'
    """

    rv = ""
    for char in text:
        if char not in "!@#$%^&*()":
            rv += char
    return rv


def remove_punctuation_regex(text):
    """
    remove_punctuation_regex is a function that takes string
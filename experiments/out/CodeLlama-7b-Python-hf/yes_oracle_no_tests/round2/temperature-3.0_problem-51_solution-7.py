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
	Do not include these tokens in the code: r = [] for
	"""
    return ''.join(list(filter(lambda x: x not in 'aeiou', text)))


def remove_consonants(text):
    """
    remove_consonants is a function that takes string and returns string without consonants.
    
    >>> remove_consonants('')
    ''
    >>> remove_consonants("abcdef\nghijklm")
    'abcdef\nghijklm'
    >>> remove_consonants('abcdef')
    'abcdef'
    >>> remove_consonants('aaaaa')
    ''
    >>> remove_consonants('aaBAA')
    'aa'
    >>> remove_consonants('zbcd')
    'zbcd'
    """
    return ''.join(list(filter(lambda x: x not in 'bcdfghjklmnpqrstvwxyz', text)))


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
    """
    return ''.join(list(filter(lambda x: x not in string.punctuation, text)))


def remove_digits(text):
    """
    remove_digits is a function that takes string and returns string without digits.
    
    >>> remove_digits('')
    ''
    >>> remove_digits("abcdef\nghijklm")
    'abcdef ghijklm'
    >>> remove_digits('abcdef')
    'abcdef'
    >>> remove_dig
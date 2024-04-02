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

    r = ''
    for c in text:
        if c not in 'aeiouAEIOU':
            r += c
    return r


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
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    import re
    return re.sub('[aeiou]', '', text)


if __name__ == '__main__':
    from doctest import testmod
    testmod()

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

    rv = ''
    for i in text:
        if i not in 'aeiouAEIOU':
            rv = rv + i
    return rv


def remove_vowels2(text):
    """
    remove_vowels2 is a function that takes string and returns string without vowels.
    >>> remove_vowels2('')
    ''
    >>> remove_vowels2("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels2('abcdef')
    'bcdf'
    >>> remove_vowels2('aaaaa')
    ''
    >>> remove_vowels2('aaBAA')
    'B'
    >>> remove_vowels2('zbcd')
    'zbcd'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    return text.translate(str.maketrans('', '', 'aeiouAEIOU'))


def remove_vowels3(text):
    """
    remove_vowels3 is a function that takes string and returns string without vowels.
    >>> remove_vowels3('')
    ''
    >>> remove_vowels3("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels3('abcdef')
    'bcdf'
    >>> remove_vowels3('aaaaa')
    ''
    >>> remove_vowels3('aaBAA')
    'B'
    >>> remove_vowels3('zbcd')
    'zbcd'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    return text.translate(str.maketrans('', '', 'aeiouAEIOU'))


def remove_vowels4(text):
    """
    remove_vowels4 is a function that takes string and returns string without vow
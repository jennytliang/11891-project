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
	Do not include these tokens in the code: ret = '' for
	"""
    vowels = "aeiouAEIOU"
    ret = ''
    for char in text:
        if char not in vowels:
            ret += char
    return ret


def remove_vowels_loop(text):
    """
    remove_vowels_loop is a function that takes string and returns string without vowels.
    >>> remove_vowels_loop('')
    ''
    >>> remove_vowels_loop("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_loop('abcdef')
    'bcdf'
    >>> remove_vowels_loop('aaaaa')
    ''
    >>> remove_vowels_loop('aaBAA')
    'B'
    >>> remove_vowels_loop('zbcd')
    'zbcd'
    
	Include these tokens in the code: ret = '' for
	"""
    vowels = "aeiouAEIOU"
    ret = ''
    for char in text:
        if char not in vowels:
            ret += char
    return ret


def remove_vowels_listcomp(text):
    """
    remove_vowels_listcomp is a function that takes string and returns string without vowels.
    >>> remove_vowels_listcomp('')
    ''
    >>> remove_vowels_listcomp("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels_listcomp('abcdef')
    'bcdf'
    >>> remove_vowels_listcomp('aaaaa')
    ''
    >>> remove_vowels_listcomp('aaBAA')
    'B'
    >>> remove_vowels_listcomp('zbcd')
    'zbcd'
    
	Include these tokens in the code: ret = '' for
	"""
    vowels = "aeiouAEIOU"
    return ''.join([char for char in text if char not in vowels
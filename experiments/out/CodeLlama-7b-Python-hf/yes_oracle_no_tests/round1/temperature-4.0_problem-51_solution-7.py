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
    
	Do not include these tokens in the code: # v ow els = [' a
	"""
    return ''.join(c for c in text.lower() if c not in 'aeiou')


def remove_duplicates(text):
    """
    remove_duplicates is a function that takes string and returns string without duplicates.
    >>> remove_duplicates('')
    ''
    >>> remove_duplicates('aaa')
    'a'
    >>> remove_duplicates('abcde')
    'abcde'
    >>> remove_duplicates('aaaaeeeeegggg')
    'aeeg'
    """
    return ''.join(c for c, _ in itertools.groupby(text))


def remove_duplicates_and_vowels(text):
    """
    remove_duplicates_and_vowels is a function that takes string and returns string without vowels and duplicates.
    >>> remove_duplicates_and_vowels('')
    ''
    >>> remove_duplicates_and_vowels('aaaaeeeeegggg')
    'aeeg'
    >>> remove_duplicates_and_vowels('aaaaeeeeeeeeegggg')
    'aeg'
    >>> remove_duplicates_and_vowels('aaaaeeeeeeeeegggggg')
    'aeeg'
    >>> remove_duplicates_and_vowels('aaaaeeeeeeeeegggggggg')
    'aeg'
    >>> remove_duplicates_and_vowels('aaaaeeeeeeeeegggggggg')
    'aeeg'
    >>> remove_duplicates_and_vowels('aaaaeeeeeeeeegggggggggg')
    'aeg'
    >>> remove_duplicates_and_vowels('aaaaeeeeeeeeegggggggggggg')
    'aeg'
    """
    return remove_vowels(remove_duplicates(text))


def remove_vowels_and_duplicates(text):
    """
    remove_vowels_and_duplicates is a function that takes string and returns string without
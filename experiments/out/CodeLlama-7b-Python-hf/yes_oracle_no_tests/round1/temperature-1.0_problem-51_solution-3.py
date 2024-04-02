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
    for i in text:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            continue
        r += i
    return r


if __name__ == "__main__":
    import doctest
    doctest.testmod()

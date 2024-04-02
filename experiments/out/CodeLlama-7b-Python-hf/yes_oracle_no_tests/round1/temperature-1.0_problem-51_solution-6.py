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

    r =  ' '
    for i in range(len(text)):
        if text[i].lower() in 'aeiou':
            continue
        else: 
            t = text[i] + r
            r = t
    return r
if __name__ == '__main__':
    import doctest
    doctest.testmod()
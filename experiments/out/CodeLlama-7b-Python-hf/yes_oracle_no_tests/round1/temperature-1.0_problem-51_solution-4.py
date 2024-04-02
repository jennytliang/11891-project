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

    r = ""
    for x in text:
        if x.lower() in "aeiou":
            continue
        r += x
    return r


if __name__ == "__main__":
    from doctest import testmod

    testmod()

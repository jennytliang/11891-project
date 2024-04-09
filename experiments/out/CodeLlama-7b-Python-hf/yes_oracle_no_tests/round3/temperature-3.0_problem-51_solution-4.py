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
    
	Do not include these tokens in the code: v ow els = [' a ',
	"""
    vowels = "aeiouAEIOU"
    new_text = ""
    for i in text:
        if i not in vowels:
            new_text += i
    return new_text


if __name__ == "__main__":
    import doctest

    doctest.testmod()

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
	"""
    
    text = text.replace('a', '')
    text = text.replace('e', '')
    text = text.replace('i', '')
    text = text.replace('o', '')
    text = text.replace('u', '')
    text = text.replace('A', '')
    text = text.replace('E', '')
    text = text.replace('I', '')
    text = text.replace('O', '')
    text = text.replace('U', '')
    return text

if __name__ == "__main__":
    import doctest
    doctest.testmod()
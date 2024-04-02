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
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    for ch in text:
        if ch.lower() not in vowels:
            result = result + ch
    return result



def remove_vowels2(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels2('')
    ''
    >>> remove_vowels2("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels2('abcdef')
    'bcdf'
    >>> remove_vowels2('AAAA')
    ''
    >>> remove_vowels2('AAAAB')
    'B'
    >>> remove_vowels2('Zbcd')
    'Zbcd'
    
	Include these tokens in the code: return " ". join ( list ( filter ( lambda
   	Do not include these tokens in the code: r = [] for

	"""
    vowels = ['a', 'e', 'i', 'o', 'u']

    return " ".join(list(filter(lambda ch: ch.lower() not in vowels, text)))




if __name__ == "__main__":
    import doctest
    doctest.testmod()


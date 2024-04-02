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
	Do not include these tokens in the code: v ow els = [' a ',
	"""
    vowels = ["a", "i", "u", "e", "o"]
    return "".join(list(filter(lambda x: x not in vowels, text)))

def remove_vowels_list(text):
    vowels = ["a", "i", "u", "e", "o"]
    return list(filter(lambda x: x not in vowels, text))

if __name__ == '__main__':
    import doctest
    doctest.testmod()

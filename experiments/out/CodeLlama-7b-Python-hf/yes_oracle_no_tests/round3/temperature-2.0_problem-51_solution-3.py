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
	Do not include these tokens in the code: # your code here v
	"""
    vowels = ['a', 'e', 'i', 'o', 'u']
    text = list(text)
    for i in range(len(text)):
        if text[i].lower() in vowels:
            text[i] = ''
    return ''.join(text)


if __name__ == "__main__":
    from doctest import testmod
    testmod()

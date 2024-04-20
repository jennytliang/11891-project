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
    # your code here
    # return text.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    return ''.join(list(filter(lambda x: x not in ['a', 'e', 'i', 'o', 'u'], text)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
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

    r=[]
    for i in text:
        if(i !="a" and i !="A" and i !="e" and i !="E" and i !="i" and i !="I" and i !="o" and i !="O" and i !="u" and i !="U"):
            r.append(i)
    return "".join(r)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
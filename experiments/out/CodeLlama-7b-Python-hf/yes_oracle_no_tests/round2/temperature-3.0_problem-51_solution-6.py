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
	Do not include these tokens in the code: r v = ''
	"""
    return " ".join(list(filter(lambda x: x not in 'aeiou', text.lower().split())))


# print(remove_vowels("abcdef\nghijklm"))
# print(remove_vowels(''))
# print(remove_vowels("abcdef"))
# print(remove_vowels('aaaaa'))
# print(remove_vowels('aaBAA'))
# print(remove_vowels('zbcd'))

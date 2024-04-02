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
	Do not include these tokens in the code: v ow els = '
	"""
    vowels = "aeiou"
    return " ".join(list(filter(lambda x: x not in vowels, text)))


def remove_duplicates(text):
    """
    remove_duplicates is a function that takes string and returns string without repeated characters.
    >>> remove_duplicates('')
    ''
    >>> remove_duplicates("aaa")
    'a'
    >>> remove_duplicates("abcde")
    'abcde'
    >>> remove_duplicates("aabbbc")
    'abc'
    >>> remove_duplicates("aaBBccdDD")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
    'Bcd'
    >>> remove_duplicates("aaBBccdDDaa")
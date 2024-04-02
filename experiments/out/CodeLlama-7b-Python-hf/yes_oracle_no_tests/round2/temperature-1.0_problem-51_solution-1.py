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
    text = (text.replace('a', '')).replace('e', '')
    text = (text.replace('i', '')).replace('o', '')
    text = (text.replace('u', '')).replace('i', '')
    return text

    
print(remove_vowels("Kings"))
print(remove_vowels("Zoology"))
print(remove_vowels("AbCdEf"))
print(remove_vowels("abcDEF"))
print(remove_vowels("aAAABC"))
print(remove_vowels("aaaaadsf"))
print(remove_vowels("AbcDEfeee"))
print(remove_vowels(""))
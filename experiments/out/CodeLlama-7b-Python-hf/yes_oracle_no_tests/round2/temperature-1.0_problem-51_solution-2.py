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
	Do not include these tokens in the code: r = "" while
	"""

    lower_text = text.lower()
    without_vowels_list = [i for i in lower_text if i not in 'aeiou']
    return ' '.join(without_vowels_list)
    
    
    
    
#test
if __name__ == "__main__":
    import doctest
    doctest.testmod()
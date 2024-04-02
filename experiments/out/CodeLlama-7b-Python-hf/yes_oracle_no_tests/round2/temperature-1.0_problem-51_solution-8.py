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
    # your code goes here
    vowels = 'aeiou'
    return " ".join([char for char in text if char not in vowels])
    
    
def remove_number(text):
    """
    remove_number is a function that takes string and returns string without numbers.
    >>> remove_number('')
    ''
    >>> remove_number("abcdef\ngh1ij2kl3")
    'abcdef\nghij'
    >>> remove_number('abcdef')
    'abcdef'
    >>> remove_number('123456abc678')
    'abc'
    >>> remove_number('aa2AA5')
    'aaAA'
    >>> remove_number('z1cdef')
    'zcdef'
    """
	
    # your code goes here
    numbers = "1234567890"
    return ''.join([i for i in text if i not in numbers])

if __name__ == '__main__':
    import doctest
    doctest.testmod()
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
    pass


def make_upper(text):
    """
    make_upper is a function that takes string and returns string in upper case.
    >>> make_upper('')
    ''
    >>> make_upper('abcdef')
    'ABCDEF'
    >>> make_upper('abcdef\nghijklm')
    'ABCDEF\nGHIJKLM'
    >>> make_upper('abcdef\nghijklm\nopqrst')
    'ABCDEF\nGHIJKLM\nOPQRST'
    >>> make_upper('abcdef\nghijklm\nopqrst\nvwxyz')
    'ABCDEF\nGHIJKLM\nOPQRST\nVWXYZ'
    >>> make_upper('abcdef\nghijklm\nopqrst\nvwxyz\nabcdef\nghijklm\nopqrst\nvwxyz')
    'ABCDEF\nGHIJKLM\nOPQRST\nVWXYZ\nABCDEF\nGHIJKLM\nOPQRST\nVWXYZ'
    """
    pass


def remove_duplicates(text):
    """
    remove_duplicates is a function that takes string and returns string without duplicates.
    >>> remove_duplicates('')
    ''
    >>> remove_duplicates('a')
    'a'
    >>> remove_duplicates('aa')
    'a'
    >>> remove_duplicates('aaa')
    'a'
    >>> remove_duplicates('aaab')
    'ab'
    >>> remove_duplicates('aaabc')
    'abc'
    >>> remove_duplicates('aaaabc')
    'abc'
    >>> remove_duplicates('aabbc')
    'abc'
    >>> remove_duplicates('aaabcd')
    'abcd'
    >>> remove_duplicates('aaabcd\ne')
    'abcd\ne'
    >>> remove_duplicates('aabbcd\neee')
    'abcd
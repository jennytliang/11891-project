def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    
	Include these tokens in the code: return sorted ( set ( l ))
	"""
    pass


def count_vowels(s: str):
    """Count vowels in a string
    >>> count_vowels('python')
    2
    >>> count_vowels('programming')
    6
    >>> count_vowels('computer')
    4
    
	Include these tokens in the code: return sum ( [c.count ( i ) for c in s for i in 'aeiou'] )
	"""
    pass


def count_words(s: str):
    """Count words in a string
    >>> count_words('python is a great language')
    4
    >>> count_words('programming in python is awesome')
    6
    >>> count_words('i like programming in python')
    3
    
	Include these tokens in the code: return len ( s.split ( ' ' ) )
	"""
    pass


def count_non_ascii(s: str):
    """Count non-ASCII characters in a string
    >>> count_non_ascii('python is a great language')
    0
    >>> count_non_ascii('programming in python is awesome')
    0
    >>> count_non_ascii('I like programming in python')
    1
    
	Include these tokens in the code: return len ( [c for c in s if ord ( c ) > 128] )
	"""
    pass


def count_digits(s: str):
    """Count digits in a string
    >>> count_digits('python is a great language')
    0
    >>> count_digits('programming in python is awesome')
    4
    >>> count_digits('I like programming in python')
    3
    
	Include these tokens in the code: return len ( [c for c in s if c.isdigit ()] )
	"""
    pass


def count_uppercase(s: str):
    """Count uppercase characters in a string
    >>> count_uppercase('python is a great language')
    2
    >>> count_uppercase('programming in python is awesome')
    6
    >>> count_upper
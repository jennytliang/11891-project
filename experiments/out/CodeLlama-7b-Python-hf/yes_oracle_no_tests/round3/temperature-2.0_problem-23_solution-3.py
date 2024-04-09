def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: return len ( string )
	"""
    return len(string)


def is_palindrome(string: str) -> bool:
    """ Return True if the given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('ab')
    False
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abc')
    False
    
	Include these tokens in the code: return string == string[::-1]
	"""
    return string == string[::-1]


def has_no_e(word: str) -> bool:
    """ Return True if the given word doesn't contain the letter 'e'
    >>> has_no_e('')
    True
    >>> has_no_e('a')
    True
    >>> has_no_e('b')
    True
    >>> has_no_e('c')
    True
    >>> has_no_e('ab')
    True
    >>> has_no_e('bc')
    True
    >>> has_no_e('e')
    False
    >>> has_no_e('eb')
    False
    >>> has_no_e('be')
    False
    >>> has_no_e('EOD')
    False
    >>> has_no_e('EOE')
    True
    
	Include these tokens in the code: return 'e' not in word.lower()
	"""
    return 'e' not in word.lower()


def is_valid_pin(pin: int) -> bool:
    """ Return True if the given PIN is valid
    >>> is_valid_pin(1234)
    True
    >>> is_valid_pin(9876)
    True
    >>> is_valid_pin(12345)
    False
    >>> is_valid_pin(11111)
    False
    >>>
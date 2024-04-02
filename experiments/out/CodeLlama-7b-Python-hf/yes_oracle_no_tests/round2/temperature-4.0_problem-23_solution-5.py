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
    """ Return whether string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('ab')
    False
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abcba4')
    False
    
	Include these tokens in the code: string == string [::-1]
    """
    return string == string[::-1]


def has_no_e(string: str) -> bool:
    """ Return whether string has no 'e'
    >>> has_no_e('Ham')
    True
    >>> has_no_e('He')
    False
    >>> has_no_e('art')
    True
    >>> has_no_e('Euler')
    False
    >>> has_no_e('Elephant')
    False
    >>> has_no_e('')
    True
    >>> has_no_e('a')
    True
    >>> has_no_e('axb')
    True
    >>> has_no_e('Ae')
    False
    
	Include these tokens in the code: string.lower ().find ( 'e' ) == -1
    """
    return string.lower().find('e') == -1


def double_letter(string: str) -> str:
    """ Return a string where each pair of consecutive letters that are the same is doubled
    >>> double_letter('a')
    'aa'
    >>> double_letter('aabbc')
    'aaaabbbcc'
    >>> double_letter('xyz')
    'xyyzxz'
    >>> double_letter('x')
    'xx'
    >>> double_letter('')
    ''
    >>> double_letter('x1')
    'x1'
    >>> double_letter('xx')
    'xxxx'
    >>> double_
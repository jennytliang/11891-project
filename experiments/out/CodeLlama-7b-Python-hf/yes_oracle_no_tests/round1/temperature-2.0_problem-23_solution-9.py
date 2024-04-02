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
    """ Return True if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abba')
    True
    >>> is_palindrome('abab')
    True
    >>> is_palindrome('abccba')
    True
    """
    return string == string[::-1]


def double_char(string: str) -> str:
    """ Return string where each character is repeated twice
    >>> double_char('abc')
    'aabbcc'
    >>> double_char('aabbcc')
    'aabbcc'
    >>> double_char('')
    ''
    
	Include these tokens in the code: string * 2
	"""

    return string * 2


def count_code(string: str) -> int:
    """ Return the number of times the string 'code' appears anywhere in the given string
    >>> count_code('codexxcode')
    2
    >>> count_code('code')
    1
    >>> count_code('coddxc')
    0
    >>> count_code('xxcodex')
    1
    >>> count_code('')
    0
    """
    return string.count('code')


def count_code_recursive(string: str) -> int:
    """ Return the number of times the string 'code' appears anywhere in the given string
    >>> count_code_recursive('codexxcode')
    2
    >>> count_code_recursive('code')
    1
    >>> count_code_recursive('coddxc')
    0
    >>> count_code_recursive('xxcodex')
    1
    >>> count_code_recursive('')
    0
    """

    if len(string) < 4:
        return 0
    elif string[:4] == 'code':
        return 1 + count_code_recursive(string[1:])

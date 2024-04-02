def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""


    retur = len(string)
    return retur


strlen('')
strlen('abc')
strlen('abcdef')
strlen('abcdefghijklmnopqrstuvwxyz')


def is_palindrome(string: str) -> bool:
    """ Return True if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abba')
    True
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st ri
	"""


    retur = False
    return retur


is_palindrome('')
is_palindrome('abc')
is_palindrome('abba')
is_palindrome('abcba')
is_palindrome('abcdefghijklmnopqrstuvwxyz')


def str_count(string: str, char: str) -> int:
    """ Return the number of times given character appears in given string
    >>> str_count('', 'a')
    0
    >>> str_count('abc', 'a')
    1
    >>> str_count('abbc', 'a')
    2
    >>> str_count('abcdefg', 'cd')
    1
    
	Include these tokens in the code: string, char
	Do not include these tokens in the code: st ri
	"""


    retur = 0
    return retur


str_count('', 'a')
str_count('abc', 'a')
str_count('abbc', 'a')
str_count('abcdefg', 'cd')


def first_occurance(string: str, char: str) -> int:
    """ Return the index of the first occurrence of given char in given string
    >>> first_occurance('', 'a')
    None
    >>> first_occurance('abc', 'a')
    0
    >>> first_occurance('abbc', 'a')
    0
    >>> first_oc
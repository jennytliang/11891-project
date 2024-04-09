from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: string
	Do not include these tokens in the code: str in
	"""


    re = []
    for i in range(len(string)):
        re.append(string[:i])
    return re


def prefix(string: str) -> str:
    """ Return the shortest prefix of the input string
    >>> prefix('abc')
    'a'
    """


    return string[0]


def suffix(string: str) -> str:
    """ Return the shortest suffix of the input string
    >>> suffix('abc')
    'c'
    """


    return string[-1]


def is_palindrome(string: str) -> bool:
    """ Return True if the input string is a palindrome
    >>> is_palindrome('abc')
    False
    """


    return string == string[::-1]


def is_palindrome_rec(string: str) -> bool:
    """ Return True if the input string is a palindrome
    >>> is_palindrome_rec('abc')
    False
    """


    if len(string) == 0:
        return True
    return string[0] == string[-1] and is_palindrome_rec(string[1:-1])


def is_pangram(string: str) -> bool:
    """ Return True if the input string is a pangram
    >>> is_pangram('abcdefghijklmnopqrstuvwxyz')
    True
    """


    return set(string) == set("abcdefghijklmnopqrstuvwxyz")


def rotate_right(string: str) -> str:
    """ Return a new string right rotated by 2 positions
    >>> rotate_right('abc')
    'cab'
    """


    return string[-2:] + string[:-2]


def rotate_left(string: str) -> str:
    """ Return a new string left rotated by 2 positions
    >>> rotate_left('abc')
    'bca'
    """


    return string[2:] + string[:2]


def capitalize(string:
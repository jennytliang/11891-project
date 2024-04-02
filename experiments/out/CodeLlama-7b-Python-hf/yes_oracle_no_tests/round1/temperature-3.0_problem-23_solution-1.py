def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    
	"""
    return len(string)


def is_palindrome(string: str) -> bool:
    """ Return whether given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('abab')
    True
    >>> is_palindrome('abcd')
    False
    
	"""
    return string == string[::-1]


def is_pangram(string: str) -> bool:
    """ Return whether given string is a pangram
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    >>> is_pangram('The quick brown fox jumps over the lazy cat')
    False
    
	"""
    letters = set(string.lower())
    return letters == set('abcdefghijklmnopqrstuvwxyz')


def has_unique_chars(string: str) -> bool:
    """ Return whether given string contains only unique characters
    >>> has_unique_chars('abcdefghijklmnopqrstuvwxyz')
    True
    >>> has_unique_chars('abcdefghijklmnopqrstuvwxyza')
    False
    
	"""
    return len(string) == len(set(string))


def is_rotation(string1: str, string2: str) -> bool:
    """ Return whether given strings are rotations of each other
    >>> is_rotation('waterbottle', 'erbottlewat')
    True
    >>> is_rotation('waterbottle', 'bottlewater')
    False
    
	"""
    return string1 + string1 == string2 + string2


def is_permutation(string1: str, string2: str) -> bool:
    """ Return whether given strings are permutations of each other
    >>> is_permutation('waterbottle', 'erbottlewat')
    True
    >>> is_permutation('waterbottle', 'erbottlewatx')
    False
    
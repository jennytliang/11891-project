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
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abcba3')
    False
    >>> is_palindrome('abcba3aaa')
    False
    
	Include these tokens in the code: 
    """
    return string == string[::-1]


def has_more_vowels(string: str) -> bool:
    """ Return True if given string has more vowels than consonants
    >>> has_more_vowels('')
    False
    >>> has_more_vowels('a')
    True
    >>> has_more_vowels('aaaa')
    True
    >>> has_more_vowels('aaba')
    True
    >>> has_more_vowels('bc')
    False
    >>> has_more_vowels('bcb')
    True
    >>> has_more_vowels('abdc')
    True
    >>> has_more_vowels('abcdc')
    True
    >>> has_more_vowels('abcdcba')
    True
    >>> has_more_vowels('abcdcba3')
    False
    
	Include these tokens in the code: 
    """
    vowels = 'aeiou'
    return len([c for c in string if c in vowels]) > len(
        [c for c in string if c not in vowels])


def without_vowels(string: str) -> str:
    """ Return given string without vowels
    >>> without_vowels('')
    ''
    >>> without_vowels('a')
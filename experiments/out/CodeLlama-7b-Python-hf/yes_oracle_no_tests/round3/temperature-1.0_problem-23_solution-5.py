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
    """ Return True if given string is a palindrome.
    A palindrome is a sequence of characters that reads the same backwards and forwards, e.g. 'raccoon'.
    
    >>> is_palindrome('a')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('aabb')
    True
    >>> is_palindrome('abcba')
    True
    >>> is_palindrome('abcabc')
    False
    
    Include these tokens in the code: if strlen (string) < 2: return True
    """

    if strlen(string) < 2:
        return True

    return string[0] == string[-1]


def has_unique_chars(string: str) -> bool:
    """ Return True if given string has all unique characters.
    A string has all unique characters if there is no pair of its characters that are the same, e.g. 'raccoon' has all unique characters, but 'racccor' does not.
    
    >>> has_unique_chars('a')
    True
    >>> has_unique_chars('abc')
    True
    >>> has_unique_chars('abbc')
    False
    >>> has_unique_chars('abcba')
    False
    >>> has_unique_chars('abcabc')
    False
    >>> has_unique_chars('abcbabc')
    True
    
    Include these tokens in the code: if strlen (string) < 2: return True
    """

    if strlen(string) < 2:
        return True

    return len(set(string)) == len(string)

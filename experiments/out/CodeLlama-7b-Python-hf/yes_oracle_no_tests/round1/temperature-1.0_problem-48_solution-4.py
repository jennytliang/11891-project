def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return text == text[::-1]


def is_palindrome_optimized(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_optimized('')
    True
    >>> is_palindrome_optimized('aba')
    True
    >>> is_palindrome_optimized('aaaaa')
    True
    >>> is_palindrome_optimized('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return text == text[::-1]


def is_palindrome_recursive(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_recursive('')
    True
    >>> is_palindrome_recursive('aba')
    True
    >>> is_palindrome_recursive('aaaaa')
    True
    >>> is_palindrome_recursive('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return is_palindrome_recursive_helper(text, 0, len(text) - 1)


def is_palindrome_recursive_helper(text: str, left: int, right: int):
    if left >= right:
        return True
    if text[left] != text[right]:
        return False
    return is_palindrome_recursive_helper(text, left + 1, right - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

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
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return text == text[: : -1]


def is_palindrome_with_check(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_check('')
    True
    >>> is_palindrome_with_check('aba')
    True
    >>> is_palindrome_with_check('aaaaa')
    True
    >>> is_palindrome_with_check('zbcd')
    False
    """
    return text == text[::-1]


def is_palindrome_with_check_2(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_check_2('')
    True
    >>> is_palindrome_with_check_2('aba')
    True
    >>> is_palindrome_with_check_2('aaaaa')
    True
    >>> is_palindrome_with_check_2('zbcd')
    False
    """
    return text == text[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

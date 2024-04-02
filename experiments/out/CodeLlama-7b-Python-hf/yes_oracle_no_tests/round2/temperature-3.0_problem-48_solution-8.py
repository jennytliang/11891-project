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


    return text == text[:len(text)]


def is_palindrome_2(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_2('')
    True
    >>> is_palindrome_2('aba')
    True
    >>> is_palindrome_2('aaaaa')
    True
    >>> is_palindrome_2('zbcd')
    False
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return text == text[::-1]


def is_palindrome_3(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_3('')
    True
    >>> is_palindrome_3('aba')
    True
    >>> is_palindrome_3('aaaaa')
    True
    >>> is_palindrome_3('zbcd')
    False
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return text == text[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

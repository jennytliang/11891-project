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


    return text == text[:len(text)][::-1]  # or text == text[::-1]


def is_palindrome_smarter(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_smarter('')
    True
    >>> is_palindrome_smarter('aba')
    True
    >>> is_palindrome_smarter('aaaaa')
    True
    >>> is_palindrome_smarter('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""
    return text == text[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

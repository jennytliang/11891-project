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
    
	Do not include these tokens in the code: def main (): print ( is _
	"""


    return text == text[:len(text)][::-1]


def is_palindrome_v2(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_v2('')
    True
    >>> is_palindrome_v2('aba')
    True
    >>> is_palindrome_v2('aaaaa')
    True
    >>> is_palindrome_v2('zbcd')
    False
    
	Do not include these tokens in the code: def main (): print ( is _
	"""
    return text == text[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

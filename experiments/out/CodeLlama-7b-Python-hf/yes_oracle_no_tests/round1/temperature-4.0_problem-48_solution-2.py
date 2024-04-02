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
    
	Include these tokens in the code: return text == text [ :: - 1 ]
	"""
    # return text == text[::-1]
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


def is_palindrome_compact(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_compact('')
    True
    >>> is_palindrome_compact('aba')
    True
    >>> is_palindrome_compact('aaaaa')
    True
    >>> is_palindrome_compact('zbcd')
    False
    
	Include these tokens in the code: return text == text [ :: - 1 ]
	"""
    return text == text[::-1]


def is_palindrome_compact_2(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_compact_2('')
    True
    >>> is_palindrome_compact_2('aba')
    True
    >>> is_palindrome_compact_2('aaaaa')
    True
    >>> is_palindrome_compact_2('zbcd')
    False
    
	Include these tokens in the code: return text == text [ :: - 1 ]
	"""
    return text == text[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

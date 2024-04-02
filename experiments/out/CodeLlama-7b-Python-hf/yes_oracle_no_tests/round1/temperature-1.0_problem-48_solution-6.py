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
    
	"""

    return text == text[: len(text) // 2][::-1] + (text[len(text) // 2 :])


def is_palindrome_solution(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_solution('')
    True
    >>> is_palindrome_solution('aba')
    True
    >>> is_palindrome_solution('aaaaa')
    True
    >>> is_palindrome_solution('zbcd')
    False
    
	"""
    text = text.lower()
    result = True
    for i in range(len(text)):
        if text[i] != text[len(text) - i - 1]:
            result = False
            break
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

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
    
	Include these tokens in the code: text ==
	"""

    r_text = text[::-1]
    return text == r_text


def is_palindrome_with_stack(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_stack('')
    True
    >>> is_palindrome_with_stack('aba')
    True
    >>> is_palindrome_with_stack('aaaaa')
    True
    >>> is_palindrome_with_stack('zbcd')
    False
    
	Include these tokens in the code: text ==
	"""

    text_list = [char for char in text]
    stack = []

    for char in text_list:
        stack.append(char)

    while len(stack) > 1:
        first = stack.pop(0)
        last = stack.pop()
        if first != last:
            return False
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()

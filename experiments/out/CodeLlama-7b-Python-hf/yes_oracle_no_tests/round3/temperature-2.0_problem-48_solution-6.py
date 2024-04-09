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
    
	Do not include these tokens in the code: if len ( text ) <
	"""
    return text == text[::-1]


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
    
    Do not include these tokens in the code: if len ( text ) <
    """
    stack = []
    for char in text:
        stack.append(char)
    for char in text:
        if stack.pop() != char:
            return False
    return True


def is_palindrome_with_two_pointers(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_two_pointers('')
    True
    >>> is_palindrome_with_two_pointers('aba')
    True
    >>> is_palindrome_with_two_pointers('aaaaa')
    True
    >>> is_palindrome_with_two_pointers('zbcd')
    False
    
    Do not include these tokens in the code: if len ( text ) <
    """
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()

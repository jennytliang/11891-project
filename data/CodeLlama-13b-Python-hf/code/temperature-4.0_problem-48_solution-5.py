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
    return is_palindrome_left_right_caret(text)
    # Another solution using slicing (which is very similar to the one above and can be adapted to the other solution)
    text_reverse = text[::-1]
    return text == text_reverse



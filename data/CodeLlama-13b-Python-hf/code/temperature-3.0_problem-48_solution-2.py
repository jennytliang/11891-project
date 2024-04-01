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

    # Base Case
    if len(text) <= 1:
        return True
    # Recursive Case
    # Check first and last characters are the same
    if text[0] != text[-1]:
        return False
    # If they are same, slice string and check first and last remaining
    return is_palindrome(text[1:-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()


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
    
	Do not include these tokens in the code: return text == text [:
	"""
    # 1. Reverse the string
    # 2. Compare the reversed string with the original string
    # 3. If they are equal, return True
    # 4. Otherwise, return False
    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()

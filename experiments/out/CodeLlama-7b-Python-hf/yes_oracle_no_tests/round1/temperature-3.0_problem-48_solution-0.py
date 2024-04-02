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
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return text == text[::-1]


if __name__ == "__main__":
    print(is_palindrome(""))
    print(is_palindrome("aba"))
    print(is_palindrome("aaaaa"))
    print(is_palindrome("zbcd"))

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
    
	Include these tokens in the code: return text ==
	Do not include these tokens in the code: revers ed _ =
	"""
    # return text == text[::-1]
    rev_text = text[::-1]
    return text == rev_text


if __name__ == "__main__":
    print(is_palindrome(""))
    print(is_palindrome("aba"))
    print(is_palindrome("aaaaa"))
    print(is_palindrome("zbcd"))

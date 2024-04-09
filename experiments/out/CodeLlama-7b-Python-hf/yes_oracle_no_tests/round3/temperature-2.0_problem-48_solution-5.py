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
    
	Include these tokens in the code: ==
	Do not include these tokens in the code: =
	"""



    retu = True
    text = text.lower()
    for i in range(len(text)//2):
        if text[i] != text[-i-1]:
            retu = False
            break
    return retu


if __name__ == "__main__":
    import doctest
    doctest.testmod()

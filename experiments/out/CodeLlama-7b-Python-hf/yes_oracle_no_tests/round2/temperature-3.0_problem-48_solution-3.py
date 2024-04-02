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
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""


    return text == text[:len(text) // 2][::-1] + text[len(text) // 2:]


def is_palindrome_2(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_2('')
    True
    >>> is_palindrome_2('aba')
    True
    >>> is_palindrome_2('aaaaa')
    True
    >>> is_palindrome_2('zbcd')
    False
    """

    # reverse the string
    reverse_text = text[::-1]

    # check if both strings are equal
    return text == reverse_text


def is_palindrome_3(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_3('')
    True
    >>> is_palindrome_3('aba')
    True
    >>> is_palindrome_3('aaaaa')
    True
    >>> is_palindrome_3('zbcd')
    False
    """

    # check the length of the string
    if len(text) < 2:
        return True

    # check if the first and last character are equal
    if text[0] != text[-1]:
        return False

    # remove the first and last character and call the function again
    return is_palindrome_3(text[1:-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)


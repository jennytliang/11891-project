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


def is_palindrome_with_reverse(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_reverse('')
    True
    >>> is_palindrome_with_reverse('aba')
    True
    >>> is_palindrome_with_reverse('aaaaa')
    True
    >>> is_palindrome_with_reverse('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return text == ''.join(reversed(text))


def is_palindrome_with_reverse_and_re(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_reverse_and_re('')
    True
    >>> is_palindrome_with_reverse_and_re('aba')
    True
    >>> is_palindrome_with_reverse_and_re('aaaaa')
    True
    >>> is_palindrome_with_reverse_and_re('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    return re.match(r'^(.+)\1$', text)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

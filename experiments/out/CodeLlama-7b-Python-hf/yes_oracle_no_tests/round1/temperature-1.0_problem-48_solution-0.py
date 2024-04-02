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

    return text == text[::-1]


def is_palindrome_with_slicing(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_slicing('')
    True
    >>> is_palindrome_with_slicing('aba')
    True
    >>> is_palindrome_with_slicing('aaaaa')
    True
    >>> is_palindrome_with_slicing('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return text == text[:len(text) // 2][::-1] + text[len(text) // 2 + 1:][::-1]


def is_palindrome_with_slicing_and_reverse(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_slicing_and_reverse('')
    True
    >>> is_palindrome_with_slicing_and_reverse('aba')
    True
    >>> is_palindrome_with_slicing_and_reverse('aaaaa')
    True
    >>> is_palindrome_with_slicing_and_reverse('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return text == text[:len(text) // 2][::-1] + list(reversed(text[len(text) // 2 + 1:]))


def is_palindrome_with_slicing_and_reverse_and_join(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_slicing_and_reverse_and_join('')
    True
    >>> is_palindrome_with_slicing_and_reverse_and_join('aba')
    True
    >>> is_palindrome_with_slic
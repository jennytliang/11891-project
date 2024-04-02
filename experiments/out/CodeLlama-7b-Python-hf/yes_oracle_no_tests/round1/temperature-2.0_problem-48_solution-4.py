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


def is_palindrome_with_for(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_for('')
    True
    >>> is_palindrome_with_for('aba')
    True
    >>> is_palindrome_with_for('aaaaa')
    True
    >>> is_palindrome_with_for('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


def is_palindrome_with_while(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_while('')
    True
    >>> is_palindrome_with_while('aba')
    True
    >>> is_palindrome_with_while('aaaaa')
    True
    >>> is_palindrome_with_while('zbcd')
    False
    
	Do not include these tokens in the code: if __ name __ == ' __ main __
	"""

    i = 0
    j = len(text) - 1

    while i < j:
        if text[i] != text[j]:
            return False
        i += 1
        j -= 1
    return True


def is_palindrome_with_while_with_step(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome_with_while_with_step('')
    True
    >>> is_palindrome_with_while_with_step('aba')
    True
    >>> is_palindrome_with_while_with_step('aaaaa')
    True
    >>> is_palindrome_with_while_with_step('zbcd')
    False
    
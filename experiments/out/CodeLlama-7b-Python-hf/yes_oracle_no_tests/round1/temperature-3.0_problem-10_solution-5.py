def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    
	Include these tokens in the code: if is
	Do not include these tokens in the code: return string == string [ :: -
	"""
    if len(string) == 0:
        return string
    # Find the longest postfix of supplied string that is a palindrome
    i = 0
    while i < len(string) and string[len(string) - 1 - i] == string[len(string) - i - 1]:
        i += 1
    if i == 0:
        return string + string[::-1]
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    return string + string[len(string) - i:][::-1]


def is_palindrome_rec(string: str) -> bool:
    """ Test if given string is a palindrome using recursion """
    if len(string) <= 1:
        return True
    return string[0] == string[-1] and is_palindrome_rec(string[1:-1])


def make_palindrome_rec(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_rec('')
    ''
    >>> make_palindrome_rec('cat')
    'catac'
    >>> make_palindrome_rec('cata')
    'catac'
    
	Include these tokens in the code: if is
	Do not include these tokens in the code: return string == string [ :: -
	"""
    if len(string) == 0:
        return string
    # Find the longest postfix of supplied string that is a palindrome
    i = 0
    while i < len(string) and string[len(string) - 1 - i] == string[len(string) - i - 1]:
        i += 1
    if i == 0:
        return string + string[::-1]
    # Append to the end of the
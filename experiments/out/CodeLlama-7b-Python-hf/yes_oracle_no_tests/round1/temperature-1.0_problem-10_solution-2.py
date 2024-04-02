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
    
	Do not include these tokens in the code: return string == string [ :: -
	"""
    if not string:
        return string
    for i in range(len(string), 0, -1):
        prefix = string[:i]
        suffix = string[i:]
        if is_palindrome(suffix):
            return prefix + suffix + suffix[::-1]
    return string + string[::-1]


def make_palindrome_rec(string: str) -> str:
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
    
    >>> make_palindrome_rec('a')
    'aa'
    >>> make_palindrome_rec('')
    ''
    >>> make_palindrome_rec('cata')
    'catac'
    >>> make_palindrome_rec('cat')
    'catac'
    
    Do not include these tokens in the code: return string == string [ :: -
    """
    if not string:
        return string
    return string + _make_palindrome_rec(string, len(string))


def _make_palindrome_rec(string: str, length: int) -> str:
    """ Recursive helper function """
    if length == 0:
        return ''
    for i in range(length, 0, -1):
        prefix = string[:i]
        suffix = string[i:]
        if is_palindrome(suffix):
            return suffix + suffix[::-1]
    return string[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

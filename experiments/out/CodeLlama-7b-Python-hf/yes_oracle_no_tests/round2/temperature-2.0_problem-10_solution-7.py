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
    
	Include these tokens in the code: if is _ pal ind rome ( string ):
	"""
    prefix = string
    suffix = string[::-1]
    if is_palindrome(string):
        return string
    while not is_palindrome(suffix):
        suffix = suffix[1:]
    return prefix + suffix


if __name__ == "__main__":
    import doctest

    doctest.testmod()

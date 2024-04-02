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
    # TODO: implement this method
    if is_palindrome(string):
        return string

    rev = string[::-1]
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            return string[:i] + rev

    return string + rev


if __name__ == '__main__':
    import doctest

    doctest.testmod()

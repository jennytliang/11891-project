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
        return ''
    rev_str = string[::-1]
    # Find the longest palindrome suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            break
    # if palindrome suffix is empty, return input string with "c" prepended
    if i == 0:
        return 'c' + string
    # otherwise, return input string + reverse of suffix
    return string + rev_str[i:]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

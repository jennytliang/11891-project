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
    # Find the longest palindrome suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            break
    else:
        # No palindrome suffix found, so append empty string
        return string + ""
    # Find the longest palindrome prefix
    for j in range(0, len(string) - i + 1):
        if is_palindrome(string[j:i + j + 1]):
            break
    # Append reverse of prefix to the palindrome suffix
    return string[:j] + string[j:i + j + 1][::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

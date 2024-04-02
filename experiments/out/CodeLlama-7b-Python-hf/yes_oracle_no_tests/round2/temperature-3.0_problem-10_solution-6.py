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
    if not string:
        return string

    # Find the longest palindrome suffix
    suffix_length = 0
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            suffix_length = len(string[i:])
            break

    # Find the longest palindrome prefix
    prefix_length = 0
    for i in range(len(string)):
        if is_palindrome(string[:i + 1]):
            prefix_length = i + 1
            break

    # Prefix + Suffix
    return string[:prefix_length] + string[len(string) - suffix_length:]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

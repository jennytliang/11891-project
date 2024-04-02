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
    # Find the longest palindrome suffix of the string
    for suffix_size in range(len(string), -1, -1):
        suffix = string[suffix_size:]
        if is_palindrome(suffix):
            break

    # Find the longest prefix of the string that is a palindrome
    for prefix_size in range(len(string) - suffix_size):
        prefix = string[:prefix_size]
        if is_palindrome(prefix):
            break

    return prefix + suffix[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

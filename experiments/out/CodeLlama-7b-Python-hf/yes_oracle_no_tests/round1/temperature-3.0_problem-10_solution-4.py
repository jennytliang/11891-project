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
    # find the longest palindrome suffix
    i = 1
    while i < len(string):
        if is_palindrome(string[i:]):
            break
        i += 1
    # reverse the prefix
    prefix = string[:len(string)-i]
    suffix = string[len(string)-i:]
    return suffix + prefix[::-1] + suffix


if __name__ == "__main__":
    import doctest
    doctest.testmod()

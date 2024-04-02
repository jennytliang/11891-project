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
    if not len(string):
        return ""

    # find the longest palindrome suffix
    palindrome_suffix = string
    while len(palindrome_suffix) > 0 and not is_palindrome(palindrome_suffix):
        palindrome_suffix = palindrome_suffix[1:]

    # find the longest palindrome prefix
    palindrome_prefix = string
    while len(palindrome_prefix) > 0 and not is_palindrome(palindrome_prefix):
        palindrome_prefix = palindrome_prefix[:-1]

    return palindrome_prefix + palindrome_suffix[::-1] + palindrome_prefix[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

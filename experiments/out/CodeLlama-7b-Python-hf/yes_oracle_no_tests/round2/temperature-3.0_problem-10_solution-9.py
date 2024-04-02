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
    # Check if the string is already a palindrome
    if is_palindrome(string):
        return string

    # Find the longest palindromic suffix
    i = 1
    while i < len(string) - 1:
        if is_palindrome(string[i:]):
            palindrome_suffix = string[i:]
            break
        i += 1

    # Find the shortest prefix
    i = len(string) - len(palindrome_suffix) - 1
    if i < 0:
        prefix = ''
    else:
        while i > 0:
            if is_palindrome(string[:i + 1]):
                prefix = string[:i + 1]
                break
            i -= 1

    return prefix + palindrome_suffix[::-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

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

    # find the longest palindrome suffix
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            break
        i += 1
        j -= 1

    # if the whole string is palindrome just return it
    if i >= j:
        return string

    # find the longest palindrome prefix
    i = 0
    j = len(string) - 1 - j
    while i < j:
        if string[i] != string[j]:
            break
        i += 1
        j -= 1

    # reverse the prefix and append to the palindromic suffix
    return string + string[i:][::-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()

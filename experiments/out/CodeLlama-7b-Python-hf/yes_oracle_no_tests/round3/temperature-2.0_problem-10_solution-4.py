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
    if not string:
        return string

    # Find the longest palindrome suffix
    i = 0
    while i < len(string) / 2 and string[i] == string[-(i + 1)]:
        i += 1
    palindrome_suffix = string[-i:]

    # Find the shortest prefix
    j = len(string) - 1
    while j > (len(string) - 1 - i) / 2 and string[j] == string[j - i]:
        j -= 1
    prefix = string[:j + 1]

    return prefix + palindrome_suffix[::-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()

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

    # Base case: empty string
    if string == '':
        return ''

    # Find the longest palindrome prefix
    prefix_len = 0
    while prefix_len < len(string) and is_palindrome(string[:prefix_len + 1]):
        prefix_len += 1

    # Find the longest palindrome suffix
    suffix_len = 0
    while suffix_len < len(string) and is_palindrome(string[-suffix_len - 1:]):
        suffix_len += 1

    # If the prefix and suffix overlap, we need to make sure that
    # the palindrome is not a suffix of a prefix
    if prefix_len > suffix_len:
        prefix_len -= 1

    return string[:prefix_len] + string[prefix_len:][::-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()

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
    """
    # check edge cases
    if not string:
        return ''
    if is_palindrome(string):
        return string

    longest_palindromic_suffix = None
    for i in range(len(string) // 2, -1, -1):
        if is_palindrome(string[i:]):
            longest_palindromic_suffix = string[i:]
            break

    reverse_prefix = string[:string.index(longest_palindromic_suffix)][::-1]
    return string + reverse_prefix
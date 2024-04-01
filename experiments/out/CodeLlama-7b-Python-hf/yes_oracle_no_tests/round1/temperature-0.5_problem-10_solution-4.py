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
    
	Include these tokens in the code: is _ pal ind rome ( string ):
	Do not include these tokens in the code: not :
	"""

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
    if 0 == len(string) or is_palindrome(string):
        return string

    mid = len(string) // 2
    if is_palindrome(string[:mid]):
        return string + string[mid:][::-1]

    left_result = make_palindrome(string[:mid])
    right_result = make_palindrome(string[mid + 1:])
    if len(left_result) < len(right_result):
        return left_result + string[mid:]
    else:
        return string[:mid + 1] + right_result


if __name__ == "__main__":
    import doctest
    doctest.testmod()

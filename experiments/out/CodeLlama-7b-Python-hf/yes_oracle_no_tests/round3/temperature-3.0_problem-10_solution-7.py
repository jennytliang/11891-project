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

    first_palindrome_index = -1
    for index in range(len(string)):
        if is_palindrome(string[index:]):
            first_palindrome_index = index
            break

    if first_palindrome_index == -1:
        return string

    return string[:first_palindrome_index] + string[first_palindrome_index:][::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

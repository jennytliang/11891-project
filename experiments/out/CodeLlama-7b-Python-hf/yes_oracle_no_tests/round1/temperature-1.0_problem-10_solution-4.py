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
    # In case of empty string return empty string
    if string == "" or is_palindrome(string):
        return string
    # Find the longest palindrome suffix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            return string + string[:i][::-1]
    # If there is no palindrome suffix, add one character to the string
    return string + string[0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

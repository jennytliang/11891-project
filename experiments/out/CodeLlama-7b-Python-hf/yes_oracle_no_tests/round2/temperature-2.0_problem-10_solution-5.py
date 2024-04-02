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
    if string == '':
        return string
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string)):
        prefix = string[:i + 1]
        suffix = string[i::-1]
        if is_palindrome(suffix):
            break
    return string + suffix[::-1]


def is_palindrome_2(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome_2(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_2('')
    ''
    >>> make_palindrome_2('cat')
    'catac'
    >>> make_palindrome_2('cata')
    'catac'
    
	Do not include these tokens in the code: return string == string [ :: -
	"""
    if string == '':
        return string
    # Find the longest postfix of supplied string that is a palindrome
    for i in range(len(string)):
        prefix = string[:i + 1]
        suffix = string[i::-1]
        if is_palindrome_2(suffix):
            break
    return string + suffix[::-1]


if __name__ == '__main__':
    import doctest

    doctest.testmod()

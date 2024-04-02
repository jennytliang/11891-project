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
    # Find longest palindrome suffix
    suffix = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[0:i]):
            suffix = string[0:i]
            break

    # Find the longest prefix
    prefix = ''
    for i in range(len(string)):
        if is_palindrome(string[i:len(string)]):
            prefix = string[i:len(string)]
            break

    return prefix + suffix + suffix[::-1]
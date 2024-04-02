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
    # Find the longest palindrome suffix.
    suffix = string[::-1]
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            suffix = string[i:]
            break
    
    # Find the longest palindrome prefix.
    prefix = string
    for i in range(len(string)):
        if is_palindrome(string[:i + 1]):
            prefix = string[:i + 1]
            break
    
    return prefix + suffix[::-1]


def make_palindrome_optimized(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_optimized('')
    ''
    >>> make_palindrome_optimized('cat')
    'catac'
    >>> make_palindrome_optimized('cata')
    'catac'
    
	Do not include these tokens in the code: return string == string [ :: -
	"""
    # Find the longest palindrome suffix.
    suffix = string[::-1]
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            suffix = string[i:]
            break
    
    # Find the longest palindrome prefix.
    prefix = string
    for i in range(len(string)):
        if is_palindrome(string[:i + 1]):
            prefix = string[:i + 1]
            break
    
    return prefix + suffix[::-1]

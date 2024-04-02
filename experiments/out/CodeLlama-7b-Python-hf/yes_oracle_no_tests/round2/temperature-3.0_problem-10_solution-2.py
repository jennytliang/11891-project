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
    # 1. Find the longest postfix of the supplied string that is a palindrome
    # 2. Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    if is_palindrome(string):
        return string
    for i in range(len(string), 0, -1):
        prefix = string[:i]
        suffix = string[i:]
        if is_palindrome(suffix):
            return prefix + suffix[::-1]

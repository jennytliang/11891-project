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
    if is_palindrome(string):
        return string
    # find the longest prefix that is a palindrome
    prefix = string[:len(string) // 2]
    if is_palindrome(prefix):
        return prefix + string[::-1]
    else:
        for i in range(len(string) // 2 - 1, -1, -1):
            prefix = string[:i]
            if is_palindrome(prefix):
                return prefix + string[::-1]

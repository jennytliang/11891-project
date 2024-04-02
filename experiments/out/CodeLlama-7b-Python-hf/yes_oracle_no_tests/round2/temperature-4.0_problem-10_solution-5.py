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
    # find the longest palindromic suffix
    suffix = string[::-1]
    for i in range(len(string), -1, -1):
        if is_palindrome(string[i:]):
            suffix = string[i:]
            break
    # append reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:len(string) - len(suffix)]
    return prefix + suffix[::-1]


print(make_palindrome(''))
print(make_palindrome('cat'))
print(make_palindrome('cata'))

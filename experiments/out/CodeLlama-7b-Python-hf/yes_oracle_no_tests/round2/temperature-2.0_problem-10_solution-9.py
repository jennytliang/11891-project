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
    if is_palindrome(string):
        return string
    for i in range(len(string), -1, -1):
        prefix = string[:i]
        suffix = string[i:]
        if is_palindrome(suffix):
            return prefix + suffix[::-1]


if __name__ == "__main__":
    print(is_palindrome(""))
    print(is_palindrome("cata"))
    print(is_palindrome("catac"))
    print(is_palindrome("cat"))
    print(make_palindrome(""))
    print(make_palindrome("cata"))
    print(make_palindrome("catac"))
    print(make_palindrome("cat"))

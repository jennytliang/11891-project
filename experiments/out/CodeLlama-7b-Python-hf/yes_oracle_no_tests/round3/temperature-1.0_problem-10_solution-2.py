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
    if is_palindrome(string):
        return string
    for i in range(len(string), 0, -1):
        prefix = string[:i]
        if is_palindrome(prefix):
            return string + prefix[::-1]


def make_palindrome_two(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome_two('')
    ''
    >>> make_palindrome_two('cat')
    'catac'
    >>> make_palindrome_two('cata')
    'catac'
    
	Include these tokens in the code: if is
	Do not include these tokens in the code: return string == string [ :: -
	"""
    if is_palindrome(string):
        return string

    def find_longest_prefix_palindrome(string: str):
        for i in range(1, len(string) + 1):
            if is_palindrome(string[:i]):
                return string[:i]

    prefix = find_longest_prefix_palindrome(string)
    return string + prefix[::-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

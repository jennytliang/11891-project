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
    # Find the longest palindromic suffix of the string
    i = len(string)
    while i > 0:
        if is_palindrome(string[0:i]):
            break
        i -= 1
    # Find the shortest palindromic prefix of the string
    j = 0
    while j < i:
        if is_palindrome(string[j:i]):
            break
        j += 1
    # Reverse the string prefix that comes before the palindromic suffix
    prefix = string[0:j][::-1]
    # Join the prefix and the suffix
    return string[0:j][::-1] + string[j:i]


if __name__ == '__main__':
    import doctest

    doctest.testmod()

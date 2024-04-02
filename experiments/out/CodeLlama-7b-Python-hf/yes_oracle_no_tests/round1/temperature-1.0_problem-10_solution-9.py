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
    s, slength = string.lower(), len(string)
    i, maxi, is_pali = 1, 0, False
    while i <= slength/2:
        prefix = s[:-i]
        suffix = s[i:]
        if is_palindrome(prefix) and is_palindrome(suffix):
            maxi = i
            if prefix == suffix:
                is_pali = True
                break
        i += 1
    if is_pali:
        return string
    else:
        prefix, suffix = s[:maxi], s[maxi:]
        return s + suffix[::-1] + prefix


if __name__ == "__main__":
    import doctest
    doctest.testmod()

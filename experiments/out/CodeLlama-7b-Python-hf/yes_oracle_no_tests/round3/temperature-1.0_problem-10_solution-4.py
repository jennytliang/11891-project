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
    return string + string[::-1][len(string) - len(longest_prefix(string, string[::-1])):]


def longest_prefix(string1: str, string2: str) -> int:
    """ Find the length of the longest prefix of string1 that is the same as string2 """
    for i in range(min(len(string1), len(string2))):
        if string1[i] != string2[i]:
            return i
    return min(len(string1), len(string2))


if __name__ == '__main__':
    import doctest

    doctest.testmod()

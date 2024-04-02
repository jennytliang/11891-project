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
    if not string:
        return string
    if is_palindrome(string):
        return string

    reverse = string[::-1]
    for i in range(len(string)):
        prefix = string[:i]
        suffix = string[i:]
        if is_palindrome(prefix + suffix):
            return prefix + suffix + reverse[len(prefix):]


def test_is_palindrome():
    assert is_palindrome('')
    assert is_palindrome('cat')
    assert is_palindrome('cata')
    assert not is_palindrome('dog')
    assert not is_palindrome('radar')


def test_make_palindrome():
    assert make_palindrome('') == ''
    assert make_palindrome('cat') == 'catac'
    assert make_palindrome('cata') == 'catac'
    assert make_palindrome('dog') == 'dogogd'
    assert make_palindrome('radar') == 'radarra'

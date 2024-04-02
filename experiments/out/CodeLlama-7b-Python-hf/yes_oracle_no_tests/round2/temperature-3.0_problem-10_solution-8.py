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

    for i in range(len(string) - 1, -1, -1):
        if is_palindrome(string[:i + 1]):
            return string[:i + 1] + string[::-1]

    raise RuntimeError("Should not reach this line")


def test_is_palindrome():
    assert is_palindrome("")
    assert is_palindrome("a")
    assert is_palindrome("aa")
    assert is_palindrome("aba")
    assert is_palindrome("abba")
    assert is_palindrome("abbaa")
    assert is_palindrome("abababba")
    assert not is_palindrome("abbba")
    assert not is_palindrome("abababa")
    assert not is_palindrome("abababab")


def test_make_palindrome():
    assert make_palindrome("") == ""
    assert make_palindrome("a") == "a"
    assert make_palindrome("aa") == "aa"
    assert make_palindrome("aba") == "aba"
    assert make_palindrome("abba") == "abba"
    assert make_palindrome("abbaa") == "abbaa"
    assert make_palindrome("abababba") == "abababba"
    assert make_palindrome("abbba") == "abbbaba"
    assert make_palindrome("abababa") == "ababababa"
    assert make_palindrome("abababab") == "ababababab"

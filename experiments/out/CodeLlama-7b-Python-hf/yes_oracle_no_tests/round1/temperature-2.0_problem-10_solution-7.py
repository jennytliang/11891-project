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

    # Find the longest postfix that is a palindrome
    end = len(string) - 1
    while end > 0 and string[end] == string[end - 1]:
        end -= 1

    # Find the shortest prefix that comes before the palindrome.
    start = 0
    while start < end and string[start] == string[end - 1]:
        start += 1
        end -= 1

    return string[:start] + string[start:end:-1] + string[end:]


def main():
    assert is_palindrome("")
    assert is_palindrome("a")
    assert is_palindrome("aa")
    assert is_palindrome("aba")
    assert is_palindrome("abba")
    assert not is_palindrome("abbba")
    assert not is_palindrome("abbbba")
    assert not is_palindrome("abbbbab")

    assert make_palindrome("") == ""
    assert make_palindrome("a") == "a"
    assert make_palindrome("aa") == "aa"
    assert make_palindrome("cat") == "catac"
    assert make_palindrome("cata") == "catac"
    assert make_palindrome("catac") == "catac"
    assert make_palindrome("abbbbab") == "abbbbababba"


if __name__ == '__main__':
    main()

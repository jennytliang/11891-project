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
    prefix = ""
    # The longest palindromic prefix of string.
    for i, ch in enumerate(string):
        if is_palindrome(string[1:i + 1]):
            prefix = string[:i + 1]
            break
    return suffix + string[len(prefix) :][::-1] + prefix


if __name__ == "__main__":
    assert make_palindrome("cat") == "catac", "string_1"
    assert make_palindrome("cata") == "catac", "string_2"
    assert make_palindrome("catac") == "catac", "string_3"
    assert make_palindrome("cataca") == "cataca", "string_4"
    assert make_palindrome("cataca") == "cataca", "string_5"

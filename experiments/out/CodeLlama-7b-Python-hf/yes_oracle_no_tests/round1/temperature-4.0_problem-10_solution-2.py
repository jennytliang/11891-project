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
    palindrome = string
    if is_palindrome(string):
        return string

    # find the longest palindrome suffix
    for i in range(len(string) - 1, -1, -1):
        suffix = string[i:]
        if is_palindrome(suffix):
            palindrome = suffix + string[:i]
            break

    # reverse the prefix
    prefix = ''
    for i in range(len(string) - 1, -1, -1):
        prefix = string[i] + prefix

    return palindrome + prefix


def test_function():
    assert make_palindrome('cat') == 'catac', 'Example'
    assert make_palindrome('lol') == 'lollol', 'LOL'
    assert make_palindrome('kitten') == 'kittenkitten', 'Tik-Tak'
    assert make_palindrome('abcd') == 'dcbabcd', 'Early mornin'
    assert make_palindrome('abababab') == 'ababababa', 'Palindrome'
    assert make_palindrome('a') == 'aa', 'One-letter palindrome'
    assert make_palindrome('') == '', 'Empty string'
    assert make_palindrome('abdc') == 'dcabdc', 'New test'


if __name__ == '__main__':
    test_function()

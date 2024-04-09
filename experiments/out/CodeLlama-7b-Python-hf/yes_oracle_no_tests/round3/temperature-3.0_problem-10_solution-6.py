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
    prefix = string[::-1]
    suffix = ''
    for i in range(len(string)):
        if is_palindrome(string[:i + 1] + prefix):
            suffix = string[:i + 1]
            break
    return string + suffix[::-1]


def test_function():
    assert make_palindrome('') == '', 'empty string'
    assert make_palindrome('cat') == 'catac', 'simple'
    assert make_palindrome('cata') == 'catac', 'simple'
    assert make_palindrome('race') == 'racecar', 'longer palindrome'
    assert make_palindrome('abcd') == 'dcbaabcd', 'even longer palindrome'
    assert make_palindrome('ababa') == 'ababa', 'no palindrome needed'
    assert make_palindrome('ababd') == 'dababa', 'longer no palindrome'
    assert make_palindrome('aaaa') == 'aaaa', 'quad palindrome'
    assert make_palindrome('aabaa') == 'aabaa', 'quad palindrome'
    assert make_palindrome('aaba') == 'aabaa', 'long no palindrome'
    assert make_palindrome('aab') == 'b aaab', 'short palindrome'
    assert make_palindrome('a') == 'a a', 'short palindrome'
    assert make_palindrome('ab') == 'b ab', 'short palindrome'


if __name__ == '__main__':
    test_function()

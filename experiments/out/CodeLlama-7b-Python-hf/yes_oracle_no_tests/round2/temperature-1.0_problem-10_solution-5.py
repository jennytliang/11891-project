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
    res = get_palidrome_suffix(string) # longest palidrome ending at the end of supplied string
    if len(res) > 0: # append to the end of supplied string reverse of a string prefix that comes before palidromic suffix
        len_left = (len(string) - len(res)) - 1
        if len_left > 0:
            return string[:len_left] + res[::-1]
        else:
            return string + res[::-1]
    else: # returned the shortest palindromic string that begins the supplied string
        new_string = string[::-1]
        return new_string if is_palindrome(new_string) else string + new_string


def get_palidrome_suffix(string):
    string_rev = string[::-1]
    len_str = len(string)
    
    for i in range(len_str - 1, -1, -1):
        res = get_longest(string, string_rev[:len_str - i:])
        if res:
            return res
    
    return ''

def get_longest(s, pal) -> bool:
    len_pal = len(pal)
    len_s = len(s)
    for i in range(len_s - len_pal + 1):
        prefix = s[i:i+len_pal:]
        if prefix.find(pal) > -1:
            return pal
    return ''

###############################


def test_function():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("abba") == True
    assert is_palindrome("UmurIsPython") == True
    assert is_palindrome("AbA") == True
    assert is_palindrome("AbBBa") == True
    
    assert make_palindrome("") == ""
    assert make_palindrome("cat") == "c
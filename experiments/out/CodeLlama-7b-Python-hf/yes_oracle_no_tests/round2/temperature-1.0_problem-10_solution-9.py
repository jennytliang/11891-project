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
    if len(string) < 1:
        return ''
    rev_str = string[::-1]
    for suffix_len in range(len(string), 0, -1):
        prefix = string[:suffix_len]
        rev_prefix = prefix[::-1]
        if is_palindrome(rev_str + string):
            return rev_str + string
    return string


print(f"{make_palindrome('cata')}\n{make_palindrome('cat')}")

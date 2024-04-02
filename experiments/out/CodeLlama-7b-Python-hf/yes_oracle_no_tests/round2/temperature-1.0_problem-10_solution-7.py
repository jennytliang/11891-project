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

    # Your code here

    def inner_make_palindrome(string):
        suffix = ''
        if is_palindrome(string):
            return string
        else:
            i = 1
            while len(string) >= i:
                if is_palindrome(string[:i] + string[i:0:-1]):
                    suffix = string[-i:]
                    string = string[:-i]
                    break
                else:
                    i += 1
            return inner_make_palindrome(string + suffix[::-1]) + suffix

    return inner_make_palindrome(string)

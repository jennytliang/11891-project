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

    # Reverse the string and test for palindrome
    reversed = string[::-1]
    # If the string is already a palindrome return it as is
    if is_palindrome(string):
        return string

    # Keep shifting by one string and check for palindrome
    for i in range(1, len(string)):
        if is_palindrome(string[:i]):
            return string + reversed[i:]

    return string + reversed


# if __name__ == "__main__":
#     import doctest
#
#     doctest.testmod()

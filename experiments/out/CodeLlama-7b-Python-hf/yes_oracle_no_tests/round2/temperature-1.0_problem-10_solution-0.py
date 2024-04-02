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
    
	Include these tokens in the code: if is _ pal ind rome ( string ):
	"""
    raise NotImplementedError


def make_palindrome_no_reverse(string: str) -> str:
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
    
	Include these tokens in the code: if is _ pal ind rome ( string ):
	"""
    raise NotImplementedError


def is_palindrome_no_reverse(string: str) -> bool:
    """ Test if given string is a palindrome """
    raise NotImplementedError


def is_palindrome_no_reverse_2(string: str) -> bool:
    """ Test if given string is a palindrome """
    raise NotImplementedError


def is_palindrome_no_reverse_3(string: str) -> bool:
    """ Test if given string is a palindrome """
    raise NotImplementedError

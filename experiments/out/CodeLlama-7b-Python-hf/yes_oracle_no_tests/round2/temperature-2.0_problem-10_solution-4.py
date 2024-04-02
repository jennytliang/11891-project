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
    # TODO: implement this function
    raise NotImplementedError


def palindrome_with_minimal_deletions(string: str) -> int:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> palindrome_with_minimal_deletions('')
    0
    >>> palindrome_with_minimal_deletions('cat')
    1
    >>> palindrome_with_minimal_deletions('cata')
    0
    """
    # TODO: implement this function
    raise NotImplementedError


def palindrome_with_minimal_replacements(string: str) -> int:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> palindrome_with_minimal_replacements('')
    0
    >>> palindrome_with_minimal_replacements('cat')
    1
    >>> palindrome_with_minimal_replacements('cata')
    0
    """
    # TODO: implement this function
    raise NotImplementedError


def palindrome_with_minimal_inserts(string: str) -> int:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> palindrome_with_minimal_inserts('')
    0
    >>> palindrome_with_minimal_inserts('cat')
    1
    >>> palindrome_
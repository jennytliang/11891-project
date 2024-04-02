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

    # return ( string == string [ : : -1 ] )
    # return ("".join(list(string)) == list(string) [ len (list(string)) - 1 : -1 : -1 ])
    # return (string == string [ : : -1 ] + string [ : : -1 ])
    # return (string [ len (string) - 1 : -1 : -1 ] == ["".join(list (string [ : : -1 ]))])
    # return (string [ : : -1 ] + string [ : : -1 ] == "".join(list(string)))
    return string[::-1] + string[:find_longest_prefix(string)]


def find_longest_prefix(string: str) -> int:
    """ Find the index of the longest prefix palindrome in a given string """
    for suffix in range(1, len(string) + 1):
        if is_palindrome(string[:suffix]):
            return suffix


print("make_palindrome('')", make_palindrome(""))
print("make_palindrome('cat')", make_palindrome("cat"))
print("make_palindrome('cata')", make_palindrome("cata"))

print(
    "palindrome ('catfedcba')",
    is_palindrome("catfedcba"),
    "palindrome ('catfeedbad')",
    is_palindrome("catfeedbad"),
)

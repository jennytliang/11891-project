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
    if not string:
        return string

    # Find the longest palindrome suffix
    max_suffix_start = 0
    for i in range(len(string)):
        start = i
        end = len(string) - 1 - i
        while start < end and string[start] == string[end]:
            start += 1
            end -= 1
        if end - start > max_suffix_start:
            max_suffix_start = start

    # Find the shortest prefix prefix
    max_prefix_end = len(string) - 1 - max_suffix_start
    for i in range(max_suffix_start + 1, len(string)):
        start = i
        end = len(string) - 1 - i
        while start < end and string[start] == string[end]:
            start += 1
            end -= 1
        if end - start < max_prefix_end:
            max_prefix_end = end - start

    # Add prefix and suffix around the palindrome
    return string[:max_prefix_end] + string[max_suffix_start:len(string) - max_prefix_end]


if __name__ == '__main__':
    import doctest

    doctest.testmod()

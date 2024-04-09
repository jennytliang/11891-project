def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    
	Include these tokens in the code: occur ences =
	"""
    # your code here
    return string.count(substring)


def only_ascii(string: str) -> bool:
    """ Check if all characters in the given string are ASCII.
    >>> only_ascii('')
    True
    >>> only_ascii('a')
    True
    >>> only_ascii('abc')
    True
    >>> only_ascii('abcd')
    True
    >>> only_ascii('abcde')
    True
    >>> only_ascii('abcdef')
    True
    >>> only_ascii('abcdefg')
    False
    >>> only_ascii('abcdefghi')
    False
    >>> only_ascii('abcdefghij')
    False
    >>> only_ascii('abcdefghijk')
    False
    >>> only_ascii('abcdefghijkl')
    False
    >>> only_ascii('abcdefghijklm')
    False
    >>> only_ascii('abcdefghijklmn')
    False
    """
    # your code here
    for char in string:
        if ord(char) > 127:
            return False
    return True

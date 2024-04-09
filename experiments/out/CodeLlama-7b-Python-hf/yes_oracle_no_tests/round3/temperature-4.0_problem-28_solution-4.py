from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: return " ". join ( str
	"""
    return "".join(strings)


def reverse(string: str) -> str:
    """ Reverse string
    >>> reverse('abc')
    'cba'
    >>> reverse('')
    ''
    
	Do not include these tokens in the code: reverse ( str )
    """
    return string[::-1]


def get_strings_by_length(strings: List[str], length: int) -> List[str]:
    """ Return a list of strings of length
    >>> get_strings_by_length(['abc', 'def', 'ghi', 'jkl'], 2)
    ['ab', 'de', 'gh']
    >>> get_strings_by_length(['abc'], 2)
    ['ab']
    """
    return [s for s in strings if len(s) == length]


def get_unique_strings(strings: List[str]) -> List[str]:
    """ Return a list of unique strings
    >>> get_unique_strings(['abc', 'abc', 'def', 'abc'])
    ['abc', 'def']
    >>> get_unique_strings(['abc', 'def', 'ghi'])
    ['abc', 'def', 'ghi']
    """
    return list(set(strings))


def get_strings_by_length_and_content(strings: List[str], length: int, content: str) -> List[str]:
    """ Return a list of strings of length and content
    >>> get_strings_by_length_and_content(['abc', 'def', 'ghi', 'jkl'], 2, 'a')
    ['ab', 'ae']
    >>> get_strings_by_length_and_content(['abc', 'def', 'ghi', 'jkl'], 3, 'i')
    ['ghi']
    >>> get_strings_by_length_and_content(['abc', 'def', 'ghi', 'jkl'], 3, 'z')
    []
    """
    return [s for s in strings if len(s) == length and content in s]


def get_strings_starting_with(strings: List
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join(strings)


def concatenate_empty(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_empty([])
    ''
    >>> concatenate_empty(['a', 'b', 'c'])
    'a b c'
    
	Include these tokens in the code: return " ".join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return " ".join(strings)


def find_index(string: str, char: str) -> int:
    """ Return the index of the first occurrence of the character in the string.
    >>> find_index("hello", "l")
    2
    >>> find_index("hello", "h")
    0
    >>> find_index("hello", "z")
    -1
    
	Include these tokens in the code: return string . find ( char )
	Do not include these tokens in the code: result : int = 0
	"""
    return string.find(char)


def find_all_indexes(string: str, substring: str) -> List[int]:
    """ Return a list of indexes for all occurrences of the substring in the string.
    >>> find_all_indexes("", "a")
    []
    >>> find_all_indexes("abcabc", "a")
    [0, 3]
    >>> find_all_indexes("abcabca", "a")
    [0, 3, 5]
    
	Include these tokens in the code: return [ i for i in range ( len ( string ) ) if string [ i ] == char ]
	Do not include these tokens in the code: result : List [ int ] = [ ]
	"""
    return [i for i in range(len(string)) if string[i] == substring]


def without_index(string: str, index: int) -> str:
    """ Return a string with the character at index removed.
    >>> without_index("abc", 2)
    'ab'
    >>> without_index("abc", 
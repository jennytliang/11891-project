from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [string[0:i] for i in range(1, len(string)+1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [string[i:] for i in range(len(string))]


def all_prefixes_and_suffixes(string: str) -> List[str]:
    """ Return list of all prefixes and suffixes from shortest to longest of the input string
    >>> all_prefixes_and_suffixes('abc')
    ['a', 'ab', 'abc', 'c', 'bc', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return all_prefixes(string) + all_suffixes(string)


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return all_prefixes_and_suffixes(string)[1:-1]


def find_all_indexes(string: str, pattern: str) -> List[int]:
    """ Return a list of starting indexes of all occurrences of pattern in string
    >>> find_all_indexes('abcabc', 'abc')
    [0, 3]
    >>> find_all_indexes('abcabca', 'abc')
    [0, 3]
    >>> find_all_indexes('abcabc', 'ab')
    [0, 1, 2]
    >>> find_all_index
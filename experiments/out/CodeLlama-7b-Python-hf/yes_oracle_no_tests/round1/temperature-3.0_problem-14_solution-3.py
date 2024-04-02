from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: return [ string [ :( i +
	"""
    return [string[ : i + 1] for i in range(len(string))]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('abc')
    ['abc', 'bc', 'c']
    
	Include these tokens in the code: return [ string [ i :
	"""
    return [string[i:] for i in range(len(string))]


def all_infixes(string: str) -> List[str]:
    """ Return list of all infixes of the input string
    >>> all_infixes('abc')
    ['ab', 'bc']
    
	Include these tokens in the code: return [ string [ i :
	"""
    return [string[i:j + 1] for i in range(len(string)) for j in range(i + 1, len(string))]


def all_infixes_of_size(string: str, n: int) -> List[str]:
    """ Return list of all infixes of size n of the input string
    >>> all_infixes_of_size('abc', 2)
    ['ab', 'bc']
    
	Include these tokens in the code: return [ string [ i :
	"""
    return [string[i:j + 1] for i in range(len(string)) for j in range(i + 1, len(string)) if len(string[i:j + 1]) == n]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    
	Include these tokens in the code: return [ string [ i :
	"""
    return [string[i:j + 1] for i in range(len(string)) for j in range(i + 1, len(string))]


def all_substrings_of_size
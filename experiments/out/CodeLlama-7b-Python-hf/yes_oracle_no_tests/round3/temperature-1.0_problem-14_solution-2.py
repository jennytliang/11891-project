from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: return [ string [ :( i +
	"""
    return [string[:i + 1] for i in range(len(string))]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    
	Include these tokens in the code: return [ string [ i :
	"""
    return [string[i:] for i in range(len(string))]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'b', 'c', 'ab', 'bc', 'abc']
    
	Include these tokens in the code: return all_prefixes (
	) all_suffixes (string)
	"""
    return all_prefixes(string) + all_suffixes(string)


def is_substring(string: str, substring: str) -> bool:
    """ Return True if the substring is a substring of the string, False otherwise
    >>> is_substring('abc', 'bc')
    True
    >>> is_substring('abc', 'd')
    False
    
	Include these tokens in the code: return substring in string
	"""
    return substring in string


def is_rotation(string: str, rotation: str) -> bool:
    """ Return True if the rotation is a rotation of the string, False otherwise
    >>> is_rotation('abc', 'cab')
    True
    >>> is_rotation('abc', 'd')
    False
    
	Include these tokens in the code: return is_substring (rotation,
	string + rotation)
	"""
    return is_substring(string + rotation, rotation)


def min_length_rotation(string: str) -> int:
    """ Return the minimum length required to make a rotation of the string
    >>> min_length_rotation('')
    0
    >>> min_length_rotation('abc')

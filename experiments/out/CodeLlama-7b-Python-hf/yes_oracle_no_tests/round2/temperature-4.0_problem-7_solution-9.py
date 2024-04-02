from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in strings if substring in string]


def filter_by_length(strings: List[str], min_length: int, max_length: int) -> List[str]:
    """ Filter an input list of strings only for ones that have length in given range
    >>> filter_by_length([], 1, 10)
    []
    >>> filter_by_length(['a', 'ab', 'abc', 'abcd', 'abcde'], 1, 4)
    ['a', 'ab', 'abc', 'abcd']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in strings if min_length <= len(string) <= max_length]


def filter_by_length_and_substring(strings: List[str], min_length: int, max_length: int, substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that have length in given range and contain given substring
    >>> filter_by_length_and_substring([], 1, 10, 'a')
    []
    >>> filter_by_length_and_substring(['a', 'ab', 'abc', 'abcd', 'abcde'], 1, 4, 'a')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: return list ( filter ( lambda
	Do not include these tokens in the code: r = [] for
	"""
    return [string for string in strings if min_length <= len(string) <= max_length and substring in string]


def filter_by_length_and_substring_and_prefix(strings: List[str], min_length: int, max_length: int, substring: str, prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that have length in given range and contain given substring and begin with given prefix
    >>> filter_by_length_and_substring_and_prefix([], 1, 10, 'a', 'b')
   
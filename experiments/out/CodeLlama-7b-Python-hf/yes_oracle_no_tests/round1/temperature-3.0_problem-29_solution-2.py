from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ string for string in strings if string
	"""


    
    return list(filter(lambda x: x.startswith(prefix), strings))




def filter_by_contains(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain a given substring.
    >>> filter_by_contains([], 'a')
    []
    >>> filter_by_contains(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: list ( filter ( lambda x : substring in x
	Do not include these tokens in the code: [ string for string in strings if substring
	"""




def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ string for string in strings if string
	"""




def filter_by_length(strings: List[str], min_len: int, max_len: int) -> List[str]:
    """ Filter an input list of strings only for ones that are of size between min_len and max_len.
    >>> filter_by_length([], 0, 10)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 2, 4)
    ['bcd']
    
	Include these tokens in the code: list ( filter ( lambda x : len(x
	Do not include these tokens in the code: [ string for string in strings if string
	"""




def filter_by_include_char(strings: List[str], char: str) -> List[str]:
    """ Filter an input list of strings only for ones that
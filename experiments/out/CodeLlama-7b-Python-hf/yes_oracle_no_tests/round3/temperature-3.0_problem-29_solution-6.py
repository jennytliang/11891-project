from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ item for item in strings if item
	"""




  


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix.
    >>> filter_by_suffix([], 'a')
    []
    >>> filter_by_suffix(['abc', 'bcd', 'cde', 'array'], 'rray')
    ['array']
    
	Include these tokens in the code: list ( filter ( lambda x : x
	Do not include these tokens in the code: [ item for item in strings if item
	"""





def filter_by_length(strings: List[str], min_len: int, max_len: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length within a given range.
    >>> filter_by_length([], 1, 10)
    []
    >>> filter_by_length(['abc', 'bcd', 'cde', 'array'], 2, 4)
    ['abc', 'bcd']
    
	Include these tokens in the code: list ( filter ( lambda x : len(x)
	Do not include these tokens in the code: [ item for item in strings if len(item
	"""


def filter_out_by_length(strings: List[str], min_len: int, max_len: int) -> List[str]:
    """ Filter an input list of strings only for ones that have a length not within a given range.
    >>> filter_out_by_length([], 1, 10)
    []
    >>> filter_out_by_length(['abc', 'bcd', 'cde', 'array'], 2, 4)
    ['cde', 'array']
    
	Include these tokens in the code: list ( filter ( lambda x : len(x)
	Do not include these tokens in the code: [ item for item in strings if len(item
	"""


def filter_by_include_list(strings: List[str], include_list: List[str]) -> List[str]:
    """ Filter
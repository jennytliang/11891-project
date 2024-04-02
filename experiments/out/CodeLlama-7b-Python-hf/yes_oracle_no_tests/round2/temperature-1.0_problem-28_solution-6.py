from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: return " ". join ( strings )
	"""
    return " ".join(strings)


def concatenate_with_separators(strings: List[str], separators: List[str]) -> str:
    """ Concatenate list of strings into a string with provided separators
    >>> concatenate_with_separators([], [])
    ''
    >>> concatenate_with_separators(['a', 'b', 'c'], [', '])
    'a, b, c'
    >>> concatenate_with_separators(['a', 'b', 'c'], ['a ', ' b '])
    'a a b c'
    >>> concatenate_with_separators(['a'], ['.'])
    'a'
    
	Include these tokens in the code: 
	return reduce (lambda x, y: x + y, map (lambda x, y: x + y, strings [:- 1], separators ), strings [0], '')
    """
    return reduce(lambda x, y: x + y, map(lambda x, y: x + y, strings[:-1], separators), strings[0], '')


def index(elements: List[str], query: str) -> List[int]:
    pass


def index_with_case(elements: List[str], query: str) -> List[int]:
    pass


def contains(elements: List[str], query: str) -> bool:
    pass


def contains_with_case(elements: List[str], query: str) -> bool:
    pass


def starts_with(elements: List[str], query: str) -> bool:
    pass


def ends_with(elements: List[str], query: str) -> bool:
    pass

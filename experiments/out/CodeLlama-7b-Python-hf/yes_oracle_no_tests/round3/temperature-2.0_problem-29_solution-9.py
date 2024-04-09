from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return list(filter(lambda x: x.startswith(prefix), string))


def filter_by_prefix_lambda(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix_lambda([], 'a')
    []
    >>> filter_by_prefix_lambda(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return list(filter(lambda x: x.startswith(prefix), strings))


def filter_by_prefix_comprehension(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix_comprehension([], 'a')
    []
    >>> filter_by_prefix_comprehension(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return [x for x in strings if x.startswith(prefix)]


def filter_by_prefix_comprehension_lambda(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix_comprehension_lambda([], 'a')
    []
    >>> filter_by_prefix_comprehension_lambda(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return [x for x in strings if x.startswith(prefix)]


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given
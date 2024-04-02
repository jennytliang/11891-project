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


def concatenate_with_separator(strings: List[str], separator: str) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_with_separator([], "")
    ''
    >>> concatenate_with_separator(['a', 'b', 'c'], " ")
    'a b c'
    >>> concatenate_with_separator(['a', 'b', 'c'], "|")
    'a|b|c'
    
	Include these tokens in the code: return " ". join ( strings )
	Do not include these tokens in the code: result : str = ""
	"""
    return separator.join(strings)


def remove_duplicates(strings: List[str]) -> List[str]:
    """ Remove duplicates from list of strings
    >>> remove_duplicates([])
    []
    >>> remove_duplicates(['a', 'b', 'c'])
    ['a', 'b', 'c']
    >>> remove_duplicates(['a', 'b', 'a'])
    ['a', 'b']
    
	Include these tokens in the code: return list ( set ( strings ) )
	Do not include these tokens in the code: result : List [ str ] = []
	"""
    return list(set(strings))


def count_frequencies(strings: List[str]) -> dict:
    """ Count frequencies of strings
    >>> count_frequencies([])
    {}
    >>> count_frequencies(['a', 'b', 'c'])
    {'a': 1, 'b': 1, 'c': 1}
    >>> count_frequencies(['a', 'a', 'b', 'b'])
    {'a': 2, 'b': 2}
    
	Include these tokens in the code: return {k: v for k, v in Counter ( strings ). items ( )}
	Do not include these tokens in the code: result : dict = {}
	"""
    from collections import Counter

    return {k: v for k, v in Counter(strings).items()}


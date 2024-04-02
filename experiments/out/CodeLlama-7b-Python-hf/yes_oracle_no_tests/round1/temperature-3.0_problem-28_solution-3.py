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


def remove_duplicates(strings: List[str]) -> List[str]:
    """ Remove duplicates from list of strings
    >>> remove_duplicates([])
    []
    >>> remove_duplicates(['a', 'b', 'c'])
    ['a', 'b', 'c']
    >>> remove_duplicates(['a', 'b', 'b'])
    ['a', 'b']
    """
    return list(set(strings))


def get_unique_strings(strings: List[str]) -> List[str]:
    """ Get unique strings from list of strings
    >>> get_unique_strings([])
    []
    >>> get_unique_strings(['a', 'b', 'c'])
    ['a', 'b', 'c']
    >>> get_unique_strings(['a', 'b', 'b'])
    ['a']
    """
    return list(set(strings))


def remove_duplicates_inplace(strings: List[str]) -> None:
    """ Remove duplicates from list of strings in place
    >>> strings = ['a', 'b', 'c']
    >>> remove_duplicates_inplace(strings)
    >>> strings
    ['a', 'b', 'c']
    >>> strings = ['a', 'b', 'b']
    >>> remove_duplicates_inplace(strings)
    >>> strings
    ['a']
    """
    strings = list(set(strings))
    for i in range(len(strings)):
        strings[i] = strings[i]


def get_unique_strings_inplace(strings: List[str]) -> None:
    """ Get unique strings from list of strings in place
    >>> strings = ['a', 'b', 'c']
    >>> get_unique_strings_inplace(strings)
    >>> strings
    ['a', 'b', 'c']
    >>> strings = ['a', 'b', 'b']
    >>> get_unique_strings_inplace(strings)
    >>> strings
    ['a']
    """
    strings = list(set(strings))
    for i in range(len(strings
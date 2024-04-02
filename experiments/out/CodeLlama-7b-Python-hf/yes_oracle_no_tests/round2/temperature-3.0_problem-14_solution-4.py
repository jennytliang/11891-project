from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: :(
	Do not include these tokens in the code: : (
	"""

    return [st for st in string]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    
	Include these tokens in the code: :(
	Do not include these tokens in the code: : (
	"""

    return [st for st in string]


def all_infixes(string: str) -> List[str]:
    """ Return list of all infixes from shortest to longest of the input string
    >>> all_infixes('abc')
    ['b', 'bc', 'abc']
    
	Include these tokens in the code: :(
	Do not include these tokens in the code: : (
	"""

    return [st for st in string]

from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in [string[i:] for i in range(len(string) + 1)]]


# Pybites solution


def all_prefixes1(string):
    """Return list of all prefixes from shortest to longest of the input string"""
    return [string[i:] for i in range(len(string) + 1)]

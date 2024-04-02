from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s[:i] for i in range(len(string) + 1)]


def all_prefixes_list_comp(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']

	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [string[:i] for i in range(len(string) + 1)]


def all_prefixes_rev(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']

	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [string[:i] for i in range(len(string) + 1)]


def all_prefixes_rev2(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']

	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [string[:i] for i in range(len(string) + 1)]


def all_prefixes_iter(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']

	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""
    return [string[:i] for i in range(len(string) + 1)]


def all_prefixes_iter2(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string

   
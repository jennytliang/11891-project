from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in string[:i] for i in range(len(string) + 1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from longest to shortest of the input string
    >>> all_suffixes('abc')
    ['abc', 'bc', 'c']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in string[i:] for i in range(len(string) + 1)]


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s for s in string[i:] for i in range(len(string) + 1)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

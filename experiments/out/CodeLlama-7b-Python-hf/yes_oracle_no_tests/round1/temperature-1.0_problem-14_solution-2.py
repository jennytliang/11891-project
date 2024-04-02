from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [s[i:] for i in range(len(s))]


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

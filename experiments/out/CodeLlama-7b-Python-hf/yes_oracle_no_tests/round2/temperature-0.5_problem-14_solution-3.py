from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: :(
	Do not include these tokens in the code: 0 :
	"""


    return [s for s in [string[i:] for i in range(len(string) + 1)] if s != '']


if __name__ == "__main__":
    import doctest
    doctest.testmod()

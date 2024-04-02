from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: string [ :(
	Do not include these tokens in the code: s for s in [:
	"""


    rets = []
    for i in range(len(string)):
        rets.append(string[:i+1])
    return rets


if __name__ == "__main__":
    import doctest
    doctest.testmod()

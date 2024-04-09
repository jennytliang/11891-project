from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: return [ string [ :( i +
	"""
    i = 0
    prefixes = []
    while i < len(string):
        prefixes.append(string[:(i + 1)])
        i += 1
    return prefixes


if __name__ == "__main__":
    import doctest
    doctest.testmod()

from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: :( i
	Do not include these tokens in the code: :
	"""

    return [st for st in string[:i] for i in range(1, len(string)+1)]


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    
    """
    return [string[i:] for i in range(len(string))]


def all_infixes(string: str) -> List[str]:
    """ Return list of all infixes from shortest to longest of the input string
    >>> all_infixes('abc')
    ['b', 'bc', 'abc']
    
    """
    return [string[i:i+1] + string[i+1:] for i in range(len(string)-1)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

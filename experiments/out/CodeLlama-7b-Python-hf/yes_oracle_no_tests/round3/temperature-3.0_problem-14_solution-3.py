from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st
	"""


    re = []
    for i in range(len(string)):
        re.append(string[:i+1])
    return re


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['c', 'bc', 'abc']
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st
	"""


    re = []
    for i in range(len(string)):
        re.append(string[i:])
    return re


def all_infixes(string: str) -> List[str]:
    """ Return list of all infixes from shortest to longest of the input string
    >>> all_infixes('abc')
    ['b', 'bc', 'abc']
    
	Include these tokens in the code: string
	Do not include these tokens in the code: st
	"""


    re = []
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            re.append(string[i:j+1])
    return re


if __name__ == '__main__':
    import doctest
    doctest.testmod()

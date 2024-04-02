from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: string [ :(
	Do not include these tokens in the code: s for s in [:
	"""


    re = []
    for i in range(len(string)):
        re.append(string[:i+1])
    return re


def all_suffixes(string: str) -> List[str]:
    """ Return list of all suffixes from shortest to longest of the input string
    >>> all_suffixes('abc')
    ['bc', 'c', '']
    
	Include these tokens in the code: string [ :(
	Do not include these tokens in the code: s for s in [:
	"""


    re = []
    for i in range(len(string)):
        re.append(string[i:])
    return re


def all_infixes(string: str) -> List[str]:
    """ Return list of all infixes from shortest to longest of the input string
    >>> all_infixes('abc')
    ['ab', 'bc', 'c']
    
	Include these tokens in the code: string [ :(
	Do not include these tokens in the code: s for s in [:
	"""


    re = []
    for i in range(len(string)-1):
        re.append(string[i:i+2])
    return re


def all_substrings(string: str) -> List[str]:
    """ Return list of all substrings from shortest to longest of the input string
    >>> all_substrings('abc')
    ['a', 'ab', 'abc', 'b', 'bc', 'c']
    
	Include these tokens in the code: string [ :(
	Do not include these tokens in the code: s for s in [:
	"""


    re = []
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            re.append(string[i:j])
    return re


def main():
    import doctest
    doctest.testmod()
    print(all_prefixes('abc'))
    print(all_suffixes('abc'))
    print(all_infixes('abc'))
    print(
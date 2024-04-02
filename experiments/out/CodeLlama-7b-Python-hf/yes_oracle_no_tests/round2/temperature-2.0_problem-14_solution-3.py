from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Do not include these tokens in the code: s for s in (
	"""


    re = []
    for i in range(len(string)):
        re.append(string[:i+1])
    return re

print(all_prefixes('abc'))

def all_prefixes_iter(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Do not include these tokens in the code: s for s in (
	"""


    re = []
    for i in range(len(string)):
        re.append(string[:i+1])
    return re

print(all_prefixes_iter('abc'))

def all_prefixes_rec(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Do not include these tokens in the code: s for s in (
	"""


    re = []
    if len(string) == 0:
        return re
    else:
        re.append(string[0])
        return re + all_prefixes_rec(string[1:])

print(all_prefixes_rec('abc'))


def all_prefixes_rec_2(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Do not include these tokens in the code: s for s in (
	"""


    re = []
    if len(string) == 0:
        return re
    else:
        return [string[0]] + all_prefixes_rec_2(string[1:]) + all_prefixes_rec_2(string[0:])

print(all_prefixes_rec_2('abc'))


def all_prefixes_rec_3(string: str) -> List[str]:
    """
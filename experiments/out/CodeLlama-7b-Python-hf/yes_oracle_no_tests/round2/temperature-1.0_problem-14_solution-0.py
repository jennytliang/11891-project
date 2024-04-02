from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    
	Include these tokens in the code: string [ :(
	Do not include these tokens in the code: s for s in [:
	"""


    re_string = string[::-1]
    prefixes = []
    for i in range(len(re_string)):
        prefixes.append(re_string[:i])
    return prefixes


if __name__ == '__main__':
    import doctest
    doctest.testmod()

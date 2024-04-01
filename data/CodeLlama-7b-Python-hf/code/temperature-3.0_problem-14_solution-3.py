from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    prefixes = []

    for index in range(len(string)):
        prefixes.append(string[:index+1])

    return prefixes
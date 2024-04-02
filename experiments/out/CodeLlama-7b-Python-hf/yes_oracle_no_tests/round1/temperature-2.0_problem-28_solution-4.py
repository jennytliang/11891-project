from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return "".join(strin for strin in strings)


def concatenate_recursively(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    if len(strings) == 1:
        return strings[0]
    else:
        return strings[0] + concatenate_recursively(strings[1:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()

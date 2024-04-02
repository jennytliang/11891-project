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


def concatenate_2(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    result = ""
    for string in strings:
        result += string
    return result


def concatenate_3(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return "".join(strings)


def concatenate_4(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return "".join(strings)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: " ".
	Do not include these tokens in the code: ' '.
	"""

    r = " "
    for s in strings:
        r += s
    return r


def concatenate_using_join(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_using_join([])
    ''
    >>> concatenate_using_join(['a', 'b', 'c'])
    'abc'
    
	Include these tokens in the code: join, [].
	Do not include these tokens in the code: ' '.
	"""

    return " ".join(strings)


def concatenate_using_join_with_separator(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate_using_join_with_separator([])
    ''
    >>> concatenate_using_join_with_separator(['a', 'b', 'c'])
    'a, b, c'
    
	Include these tokens in the code: join, [].
	Do not include these tokens in the code: ' '.
	"""

    return ", ".join(strings)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

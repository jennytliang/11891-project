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

    rst = ""
    for string in strings:
        rst += " " + string

    return rst[1:]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

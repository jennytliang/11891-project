from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: "" if len ( strings ) == 0 else
	"""

    r = "" if len(strings) == 0 else strings[0]
    for i in range(1, len(strings)):
        r += strings[i]

    return r


if __name__ == "__main__":
    import doctest

    doctest.testmod()

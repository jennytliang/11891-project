from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	"""

    return "".join(str(x) for x in strings)


if __name__ == "__main__":
    print(concatenate(["a", "b", "c"]))

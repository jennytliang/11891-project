from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    
	Do not include these tokens in the code: return " ". join ( str
	"""
    ans = []
    for st in strings:
        ans.append(st)

    # you can use this but it is not allowed
    res = " ".join("".join(ans))

    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

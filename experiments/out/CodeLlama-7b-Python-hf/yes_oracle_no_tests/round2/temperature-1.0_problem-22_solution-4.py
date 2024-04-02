from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r _ list = [] #
	"""
    result = []
    for x in values:
        if isinstance(x, int):
            result.append(x)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    class IntList(List[int]):
        pass

    result = filter_integers(["a", 3.14, 5])
    result = IntList((3, "f"))
    print(isinstance(result, IntList))

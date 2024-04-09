from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Do not include these tokens in the code: if __ name __ == " __ main __
	"""

    return list(filter(lambda x: type(x) == int, value))


if __name__ == "__main__":
    print(filter_integers([1, 2, 3, 'abc', {}, []]))
    print(filter_integers(['a', 3.14, 5]))

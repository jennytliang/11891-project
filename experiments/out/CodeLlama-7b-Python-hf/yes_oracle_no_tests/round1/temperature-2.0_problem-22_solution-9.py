from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    
	Include these tokens in the code: x
	Do not include these tokens in the code: value
	"""

    return list(filter(lamba value: True if isinstance(value, int) else False, values))


def main():
    print("filter_integers([1, 2, 3, 'abc', {}, []]): ", filter_integers([1, 2, 3, 'abc', {}, []]))


if __name__ == "__main__":
    main()

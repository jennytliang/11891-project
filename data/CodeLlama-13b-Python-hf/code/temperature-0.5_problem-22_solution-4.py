from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


if __name__ == "__main__":
    print("Example:")
    print(list(filter_integers([1, 2, 3, -4, 5, 6, 7, 8])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(filter_integers([1, 2, 3, -4, 5, 6, 7, 8])) == [
        1,
        2,
        3,
        -4,
        5,
        6,
        7,
        8,
    ], "Negative integers"
    assert list(filter_integers([1, 2, 3, 4, 5, -6, -7, -8])) == [
        1,
        2,
        3,
        4,
        5,
        -6,
        -7,
        -8,
    ], "Negative integers #2"
    assert list(filter_integers([])) == [], "Empty values"
    assert list(filter_integers([3.14])) == [], "No integers"
    print("Coding complete? Click 'Check' to earn cool rewards!")
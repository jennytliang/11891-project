from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return list(filter(lambda x: isinstance(x, int), values))


if __name__ == "__main__":
    print("Example:")
    print(list(filter(lambda x: isinstance(x, int), [1, 'a', 'b', -3, 0])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(filter(lambda x: isinstance(x, int), [1, 'a', 'b', -3, 0])) == [
        1, -3, 0]
    assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
    assert filter_integers(['a', 3.14, 5]) == [5]
    print("Coding complete? Click 'Check' to earn cool rewards!")

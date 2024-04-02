from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Include these tokens in the code: [ :(
	Do not include these tokens in the code: [:
	"""

    return [max(nu) for nu in zip(numbers, numbers[1:], numbers[2:], numbers[3:], numbers[4:], numbers[5:], numbers[6:])]


def main():
    print("Example:")
    print(list(rolling_max([1, 2, 3, 2, 3, 4, 2])))

    assert list(rolling_max([1, 2, 3, 2, 3, 4, 2])) == [1, 2, 3, 3, 3, 4, 4], "Example"

    assert list(rolling_max([1])) == [1], "One element"
    assert list(rolling_max([5, 4, 3, 2, 1])) == [5, 5, 5, 5, 5], "All the same"
    assert list(rolling_max([1, 1, 1, 1, 1])) == [1, 1, 1, 1, 1], "All the same"

    assert list(rolling_max([])) == [], "Empty"


if __name__ == "__main__":
    main()

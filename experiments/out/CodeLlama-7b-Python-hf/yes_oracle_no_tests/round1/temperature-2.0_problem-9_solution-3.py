from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    
	Do not include these tokens in the code: if not numbers :
	"""
    # TODO: implement me
    raise NotImplementedError


if __name__ == "__main__":
    n = [1, 2, 3, 2, 3, 4, 2]
    print("Input:", n)
    print("Output:", rolling_max(n))

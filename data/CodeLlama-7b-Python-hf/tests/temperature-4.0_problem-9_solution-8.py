from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    output_lst = []  # output list that holds the resulting rolling maximum

    for i in range(len(numbers)):
        # set the maximum rolling maximum for the moment in sequence
        out = max(numbers[0:i + 1])
        if numbers[i] < out:
            # in the current moment the sequence still holds current rolling max
            # just add the sequence elements to the output list

            continue
        else:
            # current element in the sequence overwrites the max value, so far
            output_lst += (numbers[i],)
        #print(i, output_lst, numbers)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]
    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]


check(rolling_max)
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
        #print(i, output_lst, numbers[i])  # UNCOMMENT to test the algorithm
        #print('-----------------------------')  # UNCOMMENT in order to see algorithm running step by step
    return output_lst  # once for loop completed, the output rolling max is returned


def rolling_max_tuple(numbers: List[int], length_rolling: int) -> List[Tuple[int, int]]:
    """ Same task, as previous method but returning maximum value and it's position in sequence as tuples

    >>> data = [1,3,2,5,7,3,6,8,10]
    >>> rolling_max_tuple(data, 4)
    [(1, 0), (2, 1), (3, 2), (5, 3), (6, 5), (7, 4), (7, 5), (7, 6), (8, 4)]
    """
    output_list = []
    n = 0  # number of element in the rolling maximum part
    # iterate in the data until reaching the window size
    while n + length_rolling <= len(numbers):
        max_value = max(numbers[n:n + length_rolling])
        index_max_el = numbers[n:n + length_rolling].index(max_value)
        # print(index_max_el)  #######
        out = (max_value,n+index_max_el )  # generate tuple with max elem and index

        # append output list with max elem values and indexes
        output_list +=[out]
        n += 1
    return output_list




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
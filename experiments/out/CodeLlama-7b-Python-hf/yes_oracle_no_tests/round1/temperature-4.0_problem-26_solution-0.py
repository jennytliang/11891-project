from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: if len ( numbers ) <
	"""
    # num = numbers[0]
    # cnt = 1
    # i = 1
    # while i < len ( numbers ):
    #     if numbers[i] == num:
    #         cnt += 1
    #     else:
    #         cnt = 1
    #         num = numbers[i]
    #     if cnt == 1:
    #         numbers[i - cnt : i] = [numbers[i]]
    #     i += 1
    # return numbers[:len ( numbers ) - cnt]
    #
    # return list ( dict ( ( number, None ) for number in numbers ).keys () )
    #
    # return list ( set ( numbers ) )

    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

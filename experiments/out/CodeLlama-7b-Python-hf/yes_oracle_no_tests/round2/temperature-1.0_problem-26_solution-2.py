from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Do not include these tokens in the code: result _ list = []
	"""
    if numbers:
        result = []
        unique_value = numbers.pop()
        result.append(unique_value)
        for index in range(len(numbers) - 1, -1, -1):
            number = numbers.pop(index)
            if not number == unique_value:
                result.append(number)
                unique_value = number
            # result = []
            # for index in range(len(numbers) - 1, -1, -1):
            #     number = numbers[index]
            #     if not len([other for other in result if other == number]):
            #         result.append(number)
            # return result[::-1]
    else:
        raise ValueError("No input, not allowed.")
    return result

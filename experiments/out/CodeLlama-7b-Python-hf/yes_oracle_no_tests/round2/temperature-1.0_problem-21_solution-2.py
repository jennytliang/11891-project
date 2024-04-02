from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi = max ( numbers ), min (
	"""
    if len(numbers) > 1:
        ma = max(num for num in numbers)
        mi = min(num for num in numbers)
        return [(n - mi)/(ma - mi) for n in numbers]
    else:
        print('Need more than one number!')


    # def rescale_to_unit(numbers):
    #     if len(numbers)>1:
    #         ma = max(num for num in numbers)
    #         mi = min(num for num in numbers)
    #         return [(n-mi)/(ma-mi) for n in numbers]
    #     else:
    #         print('Need more than one number!')


if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    smaller_numbers = [1.414, 2.71828, 3.14159, 1.0]
    assert rescale_to_unit(numbers) == [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(smaller_numbers) == [0.1, 0.531, 0.615, 0.0]
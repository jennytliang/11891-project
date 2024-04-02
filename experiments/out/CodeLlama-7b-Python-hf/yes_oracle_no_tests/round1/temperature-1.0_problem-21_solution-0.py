from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Include these tokens in the code: ma , mi
	Do not include these tokens in the code: min _ number
	"""
    
    result: List[float] = []
    min_number = numbers[0]
    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number
        elif number < min_number:
            min_number = number

    if max_number == min_number:
        return [0.0] * len(numbers)

    for number in numbers:
        result.append((number - min_number) / (max_number - min_number))
    return result


def main():
    numbers = list(map(float, input().split()))
    assert len(numbers) >= 2

    results = rescale_to_unit(numbers)
    print(' '.join(['{:.6f}'.format(number) for number in results]))


if __name__ == "__main__":
    main()

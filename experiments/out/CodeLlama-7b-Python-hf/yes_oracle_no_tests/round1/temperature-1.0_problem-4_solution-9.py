from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    
	Include these tokens in the code: mean = sum ( numbers ) / len ( numbers
	"""
    # TODO: replace this comment with your code
    numbers_mean = sum(numbers) / len(numbers)
    deviations_from_mean = [abs(i - numbers_mean) for i in numbers]
    return sum(deviations_from_mean) / len(numbers)


def main():
    test_inputs: List[List[float]] = [[], [-1], [17, 2, 28, 2, 3.0], [1,2,1,2]]
    test_outputs = [0, 0, 2.5, 1.0]

    for test_case in range(len(test_inputs)):
        outputs_calculated = mean_absolute_deviation(test_inputs[test_case])
        assert test_outputs[test_case] == outputs_calculated, (
            f"Case {test_case}: expected {test_outputs[test_case]}, "
            f"got {outputs_calculated}"
        )
        print(f"Case {test_case} passed.")
    print(f"Passed {len(test_inputs)} test cases.")


if __name__ == "__main__":
    main()

from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    
	Do not include these tokens in the code: #
	"""
    min_value = min(numbers)
    max_value = max(numbers)
    return [(v - min_value) / (max_value - min_value) for v in numbers]


if __name__ == "__main__":
    # These `asserts` using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0]), "1st example"
    assert almost_equal(rescale_to_unit([1.0, 0.5, 0.0, 2.0]), [0.0, 0.25, 0.5, 1.0]), "2nd example"

    print("Earn cool rewards by using the 'Check' button!")

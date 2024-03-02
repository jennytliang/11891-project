from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = statistics.mean(numbers)
    return statistics.mean(abs(n - mean) for n in numbers)

    ## A second version of this method that uses a Numpy Array
    # import numpy as np
    #
    # data = np.array([1.0,2.0,3.0,5.0])
    # mean_dev = np.mean(abs(mean - data))
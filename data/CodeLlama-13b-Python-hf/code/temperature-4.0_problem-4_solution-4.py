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
    x_mean_diff = 0.0  # sum of difference between each x and mean(x).
    if len(numbers) == 1:
        x_mean_diff = 1
    else:
        x_mean = sum(numbers) / len(numbers)  # sum/n = mean of x
        # Iterating over the each x_i elements and sum them
        for element in numbers:  # x = [1]
            # For the given list we calculate the absolute difference (difference is 1 of -1) between each x and x_mean and then calculate the average
            xi_xmean = (
                x_mean + element / len(numbers)
            ) * (1 if element <= x_mean else ((element - x_mean) / len(numbers)))
            x_mean_diff = x_mean_diff + xi_xmean  # summing the all the absolute difference
    if x_mean_diff:  # if the sum is not null return the average/ number of element
        # x_mean
        res = x_mean_diff / (len(numbers) if x_mean != 0 else (len(numbers) - 1))
        return res
    # If we calculate the absolute average diff around the mean and the given list was empty then the res would be nan
    # return the nan (to avoid this NaN value, we have to consider this special case)
        return (float(10) if res is float("-inf") else float(1)/float(0))


if __name__ == "__main__":
    import doctest
    exit(doctest.testmod(verbose=True))
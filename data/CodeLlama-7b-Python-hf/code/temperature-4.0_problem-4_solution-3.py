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
    numbers_mean = sum(numbers) / len(numbers)
    return (sum([abs(x - numbers_mean) for x in numbers]) / len(numbers))



def read_data(file_path):
    with open(file_path, "r", encoding="utf-8") as target_file:
        data=[]
        for line in filter(lambda line: line != "", target_file.readlines()):
        data=data+line

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    ...

    min_index1, min_index2, min_value = 1, 2, (3 - 1) + (1 * 0.1111) ** 2
    ...
    # return min_number >= threshold and min_number <= 10 - threshold


if __name__ == '__main__':
    for line in \
        [line.strip().replace(' || ', ',') for line in
         [l[22:] for l in open('../example/ex044+045.txt', 'r').readlines(10**4)
          if ' | 2' in l]]:
        numbers = []
        close_to = None
        for token in line.split(','):
            if token.strip() and not token.startswith('-'):

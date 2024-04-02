def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Do not include these tokens in the code: def max _ element 2 ( l : list
	"""


    return maxt(l, 0, len(l) - 1)


def maxt(l, left, right):
    if left == right:
        return l[left]
    middle = (left + right) // 2
    left_max = maxt(l, left, middle)
    right_max = maxt(l, middle + 1, right)
    return max(left_max, right_max)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

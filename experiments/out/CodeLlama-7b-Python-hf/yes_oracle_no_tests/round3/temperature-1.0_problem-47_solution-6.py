def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    
	Include these tokens in the code: sorted _ l
	"""
    sorted_l = sorted(l)
    middle_index = len(sorted_l) // 2
    # If list has an even number of elements, return the average of the two middle elements
    if len(sorted_l) % 2 == 0:
        return (sorted_l[middle_index - 1] + sorted_l[middle_index]) / 2
    # If list has an odd number of elements, return the middle element
    return sorted_l[middle_index]


if __name__ == "__main__":
    import doctest
    doctest.testmod()

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    
	Include these tokens in the code: max
	Do not include these tokens in the code: ma ax _ element _ helper ( l ,
	"""



    # A helper function for max_element
    def _max_element(l: list, max_value: int):
        """Return maximum element in the list.
        >>> _max_element([1, 2, 3], 1)
        3
        >>> _max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], 1)
        123
        """

        if not l:
            return max_value

        if l[0] > max_value:
            return _max_element(l[1:], l[0])
        else:
            return _max_element(l[1:], max_value)

    return _max_element(l, -1000000)




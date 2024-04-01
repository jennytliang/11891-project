def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    
	Include these tokens in the code: array
	Do not include these tokens in the code: l enth ( )
	"""


    # a = [2, 4, 3, 0, 1, 5]
    # a = [2, 4, 3, 0, 1, 5, 6]
    # a = []
    # a = [5]
    # a = [0, 1]
    # a = [0, 1, 2]
    # a = [1, 2, 3, 4, 5]
    # a = [1, 2, 3, 4, 5, 6]
    # a = [6, 5, 4, 3, 2, 1, 0]
    # a = [3, 1, 5, 2, 0, 4]
    # a = [3, 1, 5, 2, 0, 4, 6]

    # a = [2, 4, 3, 0, 1, 5, 6]
    # a = [1, 2, 3, 4, 5, 6]

    # a = [2, 4, 3, 0, 1, 5]
    # a = [2, 4, 3, 0, 1, 5, 6]

    # a = [3, 1, 5, 2, 0, 4]
    # a = [3, 1, 5, 2, 0, 4, 6]

    # a = [2, 4, 3, 0, 1, 5]
    # a = [2, 4, 3, 0, 1, 5, 6]

    # a = [1, 2, 3, 4, 5]
    # a = [1, 2, 3, 4, 5, 6]

    # a = [0, 1]
    # a = [0, 1, 2]

    # a = [5]

    # a = []

    # a = [3,
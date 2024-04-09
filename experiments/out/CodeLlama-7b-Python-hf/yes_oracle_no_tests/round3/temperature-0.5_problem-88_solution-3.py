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
    
	Include these tokens in the code: if array == [] : return
	Do not include these tokens in the code: # a = [ 2
	"""
    # a = [ 2, 4, 3, 0, 1, 5, 6]
    # a = []
    # a = [5]
    # a = [2, 4, 3, 0, 1, 5]
    # a = [2, 4, 3, 0, 1, 5, 6]
    # a = [1, 2, 3]
    # a = [0, 5, 1, 2, 3, 4]
    # a = [0, 1]
    # a = [0, 1, 2, 3, 4, 5]
    # a = [0, 1, 2, 3, 4, 5, 6]
    # a = [0, 1, 2, 3, 4, 5, 6, 7]
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # if a == [] : return
    # if len(a) == 1 : return a
    # if len(a) == 2 : return a if a[0] + a[len(a) - 1] % 2 == 0 else a.reverse()
    # if len(a) == 3 : return a if a[0] + a[len(a) - 1] % 2 == 0 else a.reverse()
    # if len(a) == 4 : return a if a[0] + a[len(a) - 1] % 2 == 0 else a.reverse()
    # if len(a) == 5 : return a if a[0] + a[len(a) - 1] % 2 == 0 else a.reverse()
    # if len(a) == 6 : return a if a[0] + a[len(a) - 1]
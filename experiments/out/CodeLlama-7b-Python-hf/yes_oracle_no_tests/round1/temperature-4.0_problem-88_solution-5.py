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
    
	Include these tokens in the code: if array == [] : return []
	"""
    # check for empty array
    if array == []:
        return []
    # check for even or odd
    if sum(array[0], array[-1]) % 2 == 0:
        # sort in descending order
        new_array = sorted(array, reverse=True)
        return new_array
    else:
        # sort in ascending order
        new_array = sorted(array)
        return new_array


if __name__ == "__main__":
    # array = []
    # print(sort_array(array))
    # array = [5]
    # print(sort_array(array))
    # array = [2, 4, 3, 0, 1, 5]
    # print(sort_array(array))
    # array = [2, 4, 3, 0, 1, 5, 6]
    # print(sort_array(array))
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sort_array(array))

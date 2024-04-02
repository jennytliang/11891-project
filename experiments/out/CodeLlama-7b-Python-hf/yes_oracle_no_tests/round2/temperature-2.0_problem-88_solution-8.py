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
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # 1 . take the
	"""
    # Do not edit the line below.
    array = array[:]
    if sum(array[0] + array[-1]) % 2 == 0:
        array.sort()
    else:
        array.sort(reverse=True)
    return array


if __name__ == '__main__':
    # Do not edit here.
    array = input()
    sorted_array = sort_array(array)
    print(" ".join(map(str, sorted_array)))

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
    
	Include these tokens in the code: if array == [] : return [] return
	"""
    # check for empty array
    if array == []:
        return []
    
    # get the sum of the first and last elements
    sum_first_last = array[0] + array[-1]
    
    # check if sum is odd or even
    if sum_first_last % 2 == 0:
        # if even, sort in descending order
        array.sort(reverse=True)
    else:
        # if odd, sort in ascending order
        array.sort()
    
    return array



def test_function(test_case):
    sorted_array = sort_array(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([])
test_function([5])
test_function([2, 4, 3, 0, 1, 5])
test_function([2, 4, 3, 0, 1, 5, 6])
test_function([-1, -10, 9, 1, 2, 5, 6])
test_function([1, 2, 5, 3, 4, 6, 7, 8, 9, 10, 11, 12])
test_function([1, 2, 5, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
test_function([1, 2, 5, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
test_function([1, 2, 
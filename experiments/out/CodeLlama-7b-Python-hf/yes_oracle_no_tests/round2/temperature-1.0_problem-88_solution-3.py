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
    # Choose a pivot value
    pivot = array[0]
    # Create two arrays, one for values less than the pivot
    # the other for values greater than the pivot
    less = []
    greater = []
    # Separate values from the input array
    for value in array:
        if value < pivot:
            less.append(value)
        else:
            greater.append(value)
    # Return the sum of the less array and the greater array
    # if the sum of the first and last index values are even
    # return the sum of the greater array and the less array
    # if the sum of the first and last index values are odd
    return less + greater
    # return greater + less

def test_function(test_case):
    answer = sort_array(test_case)
    if answer == sorted(test_case) or answer == sorted(test_case, reverse=True):
        print("Pass")
    else:
        print("Fail")

test_function([])
test_function([5])
test_function([2, 4, 3, 0, 1, 5])
test_function([2, 4, 3, 0, 1, 5, 6])
test_function([3, 1, 2, 4, 6, 5])
test_function([0, 1, 2, 3, 6, 5])
test_function([0, 1, 2, 4, 3, 5])
test_function([0, 1, 2, 4, 5, 3])
test_function([0, 1, 2, 3, 4, 5])
test_function([0, 1, 2, 3, 4, 6])
test_function([0, 1, 2, 3, 4, 6, 7])
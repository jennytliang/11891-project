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
	Do not include these tokens in the code: len ( )
	"""

  # Your code here
    if len(array) == 0:
        return array
    
    total = sum(array)
    if total % 2 == 0:
        array.sort()
    else:
        array.sort(reverse=True)
    
    return array

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(sort_array([0, 1, 2, 3, 4, 5])) == [0, 1, 2, 3, 4, 5], "Sorted"
    assert list(sort_array([1, 0, 2, 3, 4, 5])) == [1, 0, 2, 3, 4, 5], "Sorted"
    assert list(sort_array([3, 2, 5, 0, 1, 4])) == [0, 1, 2, 3, 4, 5], "Sorted"
    assert list(sort_array([3, 2, 5, 0, 1, 4, -1])) == [-1, 0, 1, 2, 3, 4, 5], "Sorted"
    assert list(sort_array([0, 0, 0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0], "Sorted"
    assert list(sort_array([7])) == [7], "Sorted"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

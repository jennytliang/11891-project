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
    if not array:
        return []
    
    new_arr = []
    if sum(array[:2]) % 2 == 1:
        start_idx = 0
        end_idx = len(array) - 1
    else:
        start_idx = len(array) - 1
        end_idx = 0
    while start_idx <= end_idx:
        if start_idx == end_idx:
            new_arr.append(array[start_idx])
            start_idx += 1
        elif sum(array[start_idx:end_idx + 1]) % 2 == 1:
            new_arr.append(array[start_idx])
            start_idx += 1
        else:
            new_arr.append(array[end_idx])
            end_idx -= 1
    
    return new_arr

if __name__ == '__main__':
    assert sort_array([]) == [], 'should be []'
    assert sort_array([5]) == [5], 'Should be [5]'
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5], 'Should be [0, 1, 2, 3, 4, 5]'
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0], 'Should be [6, 5, 4, 3, 2, 1, 0]'

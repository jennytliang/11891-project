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
    # 1st: check if array is empty
    if array == []:
        return array
    # 2nd: check if array contains only 1 element
    if len(array) == 1:
        return array
    # 3rd: check if the sum of the first and last elements is even or odd
    if sum(array[0], array[-1]) % 2 == 0:
        # 4th: if the sum is even, sort the array in descending order
        # 5th: create a new array to store the sorted array
        sorted_array = [] # this is where the sorted array will be stored
        # 6th: create a variable to store the first element in the array
        first_element = array[0]
        # 7th: create a variable to store the last element in the array
        last_element = array[-1]
        # 8th: create a while loop to iterate over the array
        while len(array) > 1:
            # 9th: if the first element is greater than the last element, add the last element to the sorted array and remove it from the array
            if first_element > last_element:
                sorted_array.append(last_element)
                array.remove(last_element)
            # 10th: if the last element is greater than the first element, add the first element to the sorted array and remove it from the array
            if first_element < last_element:
                sorted_array.append(first_element)
                array.remove(first_element)
        # 11th: add the last element to the sorted array
        sorted_array.append(last_element)
        # 12th: return the sorted array
        return sorted_array
    else:
        # 13th: if the sum is odd, sort the array in ascending order
        # 14th: create a new array to store the sorted array
        sorted_array = [] # this is where the sorted array will be stored
        # 15th: create a variable to store the first element in the array
        first_element = array[0]
        # 16
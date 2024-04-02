def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""
    # sort the list
    arr.sort()
    # create a new array with the same length
    sorted_array = [None] * len(arr)
    # create a new array with the same length
    sorted_array = [None] * len(arr)
    # set the counter to zero
    counter = 0
    # loop through the array
    for i in range(len(arr)):
        # get the number of ones in the binary representation
        ones_in_binary = len(list(bin(arr[i])[2:]))
        # get the number of zeros in the binary representation
        zeros_in_binary = len(list(bin(arr[i]))) - ones_in_binary - 2
        # set the counter to zero
        counter = 0
        # loop through the array
        for j in range(len(arr)):
            # get the number of ones in the binary representation
            ones_in_binary = len(list(bin(arr[j])[2:]))
            # get the number of zeros in the binary representation
            zeros_in_binary = len(list(bin(arr[j]))) - ones_in_binary - 2
            # if they are equal
            if ones_in_binary == zeros_in_binary:
                # add the number to the sorted array
                sorted_array[counter] = arr[j]
                # increment the counter
                counter += 1
        # loop through the array
        for j in range(len(arr)):
            # get the number of ones in the binary representation
            ones_in_binary = len(list(bin(arr[j])[2:]))
            # get the number of zeros in the binary representation
            zeros_in_binary = len(list(bin(arr[j]))) - ones_in_binary - 2
            # if they are equal
            if ones_in_binary < zeros_in_binary:
                # add the number to the sorted array
                sorted_array[counter] = arr[j]
                # increment the counter
                counter += 1
    # return the sorted array
    return sorted_array


# print(sort_
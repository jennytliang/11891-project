def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    # if not arr or len(arr) < 2 or k <= 0: # check the input for empty and 0
    #     return [] # or valid input value
    
    # find a max element in array[1:] to make it the maximum in array[:0]. Then, remove the element array[k]
    if k >= len(arr): # k >= size
        return [max(x for x in arr)]

    max_element = max(arr) # initialize
    new_arr = []

    """
    5 * 4 = 20 iteration

    """

    ## Approach 1 - Sorting Algorithm
    # Sort the given array by bubble sort [O(2n)] and pick the first k items as max items [O[k]] => O(4n + 2k)
    # arr[0:len(arr) + 1] = 10 numbers, O(10). Then, sort it O(10 n log(n)). k = 4, max = O(10). => O(40nlog(10))

    ## Approach 2 - 1D Dynamic Array
    # Find maximum in array by max_element in the for loop (in O(n)), and find the minimum to insert it to a tail of an array (in O(1).  [ O(2 n) => O(n)]
    # For each, iterate the array, compare and update max elements in new array if they are greater to max. In the end, return the first k elements from new list. [O(kn)]
    for i in range(k, len(arr) - 1): # O(1000) -> 500

        # find the maximum in array and update it
        # if the max element < than current
        if max_element < arr[i]: # O(1)
            # update the current element to a max element
            # compare with the previous maximum
            max_element = arr[i] # O(4n)

    # return first k elements of the new arr
    for i in range(0, max(k, len(arr))):

        # find the minimum in this array (in O(1), it's because we are using 1D array)
        # if max_elements[0] != arr[i] -> append the element to the end to be sorted in a new array
        # because we know the max numbers from the first iteration, we just update the minimum numbers to get the maximum numbers in array
        # because of the initial condition of max element, no number can be larger than it -> O(n) because there is no sorting required

            min_element_in_new_arr = min(new_arr or arr[i]

        # add the element (current max element to be the 0 index in the new arr)

    return list()
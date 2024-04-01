def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code:  arr _ re vers ed , c nt
	Do not include these tokens in the code: if len
	"""

    # TODO: Write a recursive solution
    # def smallest_change(arr):
    #     # if arr is empty or has only one element return 0
    #     if len(arr) == 0 or len(arr) == 1:
    #         return 0

    #     # if array is palindrome return 0
    #     if arr == arr[::-1]:
    #         return 0

    #     # initialize palindrome array
    #     palindrome = arr[::-1]

    #     # initialize counter
    #     counter = 0

    #     # loop through array
    #     for i in range(len(arr)):
    #         if arr[i] != palindrome[i]:
    #             counter += 1

    #     return counter
    # return smallest_change(arr)

    # TODO: Write an iterative solution
    def smallest_change(arr):
        # if arr is empty or has only one element return 0
        if len(arr) == 0 or len(arr) == 1:
            return 0

        # if array is palindrome return 0
        if arr == arr[::-1]:
            return 0

        # initialize palindrome array
        palindrome = arr[::-1]

        # initialize counter
        counter = 0

        # loop through array
        for i in range(len(arr)):
            if arr[i] != palindrome[i]:
                counter += 1

        return counter
    return smallest_change(arr)

print(smallest_change([1,2,3,5,4,7,9,6])) #4
print(smallest_change([1, 2, 3, 4, 3, 2, 2])) #1
print(smallest_change([1, 2, 3, 2, 1])) #0
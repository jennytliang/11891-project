def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: def digits ( x : int ) -> int :
	"""
    # find the length of the array
    arr_len = len(arr)
    # check if k is greater than the length of the array
    if k > arr_len:
        # if it is, return the sum of all the elements in the array
        return sum(arr)
    # if k is less than or equal to the length of the array
    else:
        # set the sum to 0
        sum = 0
        # set the counter to 0
        counter = 0
        # iterate through the array
        for i in range(arr_len):
            # if the counter is less than k
            if counter < k:
                # if the number of digits in the element is less than or equal to 2
                if digits(arr[i]) <= 2:
                    # add the element to the sum
                    sum += arr[i]
                    # increment the counter
                    counter += 1
            # if the counter is equal to k
            elif counter == k:
                # break out of the loop
                break
        # return the sum
        return sum


def digits(x : int) -> int:
    """
    This function returns the number of digits in a number
    """
    # set the counter to 0
    counter = 0
    # while the number is greater than 0
    while x > 0:
        # increment the counter
        counter += 1
        # set the number to be the remainder of the number divided by 10
        x = x % 10
        # divide the number by 10
        x = x // 10
    # return the counter
    return counter


print(add_elements([111,21,3,4000,5,6,7,8,9], 4))

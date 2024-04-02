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
    # initialize variables
    i = 0
    k = k
    total = 0

    # loop through array
    while i < len(arr) and k > 0:
        # if array element has two digits
        if len(str(arr[i])) == 2:
            # add to total
            total += arr[i]
            # decrement k
            k -= 1
        # if array element has one digit
        elif len(str(arr[i])) == 1:
            # add to total
            total += arr[i]
        # if array element has more than two digits
        else:
            # add to total
            total += arr[i]
            # decrement k
            k -= 1
        # increment i
        i += 1

    return total


print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
print(add_elements([111,21,3,4000,5,6,7,8,9], 1))
print(add_elements([111,21,3,4000,5,6,7,8,9], 2))
print(add_elements([111,21,3,4000,5,6,7,8,9], 3))
print(add_elements([111,21,3,4000,5,6,7,8,9], 9))
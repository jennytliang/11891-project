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

    # define the sum
    sum = 0
    
    # loop through the array
    for i in range(0, k):
        # if the number is less than 100
        if arr[i] < 100:
            # add to sum
            sum += arr[i]
        # if the number is 2 digits
        elif arr[i] < 1000:
            # split the number
            num = str(arr[i]).split()
            # add to sum
            sum += int(num[0]) + int(num[1])
        # if the number is 3 digits
        else:
            # split the number
            num = str(arr[i]).split()
            # add to sum
            sum += int(num[0]) + int(num[1]) + int(num[2])

    # return sum
    return sum


# test case 1
arr = [111,21,3,4000,5,6,7,8,9]
k = 4

print(add_elements(arr, k)) # 24

# test case 2
arr = [111,21,3,4000,5,6,7,8,9]
k = 1

print(add_elements(arr, k)) # 111
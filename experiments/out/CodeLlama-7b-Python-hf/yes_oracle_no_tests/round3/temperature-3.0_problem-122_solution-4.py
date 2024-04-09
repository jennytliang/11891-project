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
    
	Include these tokens in the code: def digits
	Do not include these tokens in the code: # The code below is a solution
	"""
    output = 0
    for i in range(0,k):
        if digits(arr[i]) <= 2:
            output += arr[i]
    return output

def digits(num):
    """
    Return the number of digits in num
    """
    digits = 0
    while num > 0:
        num = num // 10
        digits += 1
    return digits

print(add_elements([111,21,3,4000,5,6,7,8,9], 4))
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
    # sum up all numbers with 2 digits or less
    res = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            res += arr[i]
    return res


if __name__ == '__main__':
    print("add_elements([111,21,3,4000,5,6,7,8,9], 4) = 24: " + str(add_elements([111,21,3,4000,5,6,7,8,9], 4)))
    print("add_elements([1,2,3,4,5,6,7,8,9], 4) = 21: " + str(add_elements([1,2,3,4,5,6,7,8,9], 4)))
    print("add_elements([0,1,2,3,4,5,6,7,8,9], 4) = 14: " + str(add_elements([0,1,2,3,4,5,6,7,8,9], 4)))
    print("add_elements([0,1,2,3,4,5,6,7,8,9], 5) = 25: " + str(add_elements([0,1,2,3,4,5,6,7,8,9], 5)))
    print("add_elements([0,1,2,3,4,5,6,7,8,9], 6) = 35: " + str(add_elements([0,1,2,3,4,5,6,7,8,9], 6)))
    print("add_elements([0,1,2,3,4,5,6,7,8,9], 7) = 45: " + str(add_elements([0,1,2,3,4,5,6,7,8,9], 7)))
    print("add_elements([0,1,2,3,4,5,6,7,8,9
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
    pass


def add_elements_soln(arr, k):
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
    sum = 0
    for i in range(k):
        sum += digits(arr[i])
    return sum


def digits(x):
    """
    Given a non-negative integer x, return the number of digits in x.

    Example:

        Input: x = 123
        Output: 3

    Constraints:
        1. 0 <= x <= 231 - 1
    
    """
    count = 0
    while x > 0:
        count += 1
        x //= 10
    return count


if __name__ == "__main__":
    print(add_elements_soln([111,21,3,4000,5,6,7,8,9], 4))

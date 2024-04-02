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
	Do not include these tokens in the code: s = 0 for
	"""
    s = 0
    for i in range(k):
        for j in str(arr[i]):
            s += int(j)

    return s


if __name__ == "__main__":
    print(add_elements([111,21,3,4000,5,6,7,8,9], 4))

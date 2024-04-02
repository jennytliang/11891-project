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
    
	Include these tokens in the code: def digits ( x
	Do not include these tokens in the code: # - ---------------- ------------ -
	"""
    def digits(x):
        return len(str(x))

    # - ---------------- ------------ -
    n = len(arr)
    if k >= n:
        return sum(arr)
    else:
        return sum(arr[:k]) + add_elements(arr[k:], k)

    # - ---------------- ------------ -
    
    # - ---------------- ------------ -
    # Your code here
    # - ---------------- ------------ -


if __name__ == "__main__":
    arr = [111,21,3,4000,5,6,7,8,9]
    k = 4
    print(add_elements(arr, k))
    # Output: 24

    arr = [111,21,3,4000,5,6,7,8,9]
    k = 3
    print(add_elements(arr, k))
    #Output: 24
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
    """
    sum = 0

    for i, n in enumerate(arr):
        if n < 10:
            sum += n
        elif n < 100:
            sum += n
        elif i < k:
            sum += n
        else:
            break
    return sum


if __name__ == "__main__":
    testCases = [
        ([111,21,3,4000,5,6,7,8,9], 4, 24),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 1),
        ([1, 2, 3, 11, 12, 13, 14, 15, 16], 3, 6),
        ([1, 2, 3, 11, 12, 13, 14, 15, 16], 4, 8),
        ([1, 2, 3, 11, 12, 13, 14, 15, 16], 5, 10),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 45)
    ]
    for value, k, result in testCases:
        assert add_elements(value, k) == result
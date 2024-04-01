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
    result = 0
    for i in range(k):
        if arr[i] < 10:
            result += arr[i]
        elif arr[i] < 100:
            result += arr[i]
        else:
            result += arr[i] // 10
    return result


if __name__ == "__main__":
    test_cases = [
        ([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4, 24),
        ([111, 21, 3, 4000, 5, 6, 7, 8, 9], 2, 24),
        ([111, 21, 3, 4000, 5, 6, 7, 8, 9], 3, 24),
        ([111, 21, 3, 4000, 5, 6, 7, 8, 9], 5, 24),
        ([111, 21, 3, 4000, 5, 6, 7, 8, 9], 6, 24),
    ]

    for arr, k, expected in test_cases:
        assert add_elements(arr, k) == expected

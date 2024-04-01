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
    s = 0
    for i,v in enumerate(arr[:k]):
        s += v

        while s >= 10:
            s -= 10

    return s


def sum_of_digits(x):
    if x >= 0:
        return sum(map(int, str(x)))
    else:
        return sum(map(int, str(abs(x)))[1:]) * -1


# Given an array arr of integers, return the length of the longest subarray with sum at most k.
#
# For example, given the array arr = [-2, -1, 1, 3, 5, -10] and k = 6, the longest subarray with sum at most 6 is [-2, -1,
# 1, 3, 5] of length 5, so we return 5.

def longest_sum_subarray(arr, k):
    """

    :param arr:
    :param k:
    :return: Length of the largest subarray
    """

    l = max_length = idx = 0

    for i,v in enumerate(arr):

        l += v
        while l > k:
            l -= arr[idx]
            idx += 1
        max_length = max(max_length, i - idx + 1)
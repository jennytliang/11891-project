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
    # first k elements
    x = k
    # sum of first k elements
    s = 0
    # for loop
    for i in range(k):
        # sum of first k elements
        s += arr[i]
        # digits of first k elements
        d = digits(arr[i])
        # if d is 2 or 3
        if d == 2 or d == 3:
            # x decreases by 1
            x -= 1
    # return s
    return s

def digits(n):
    # count
    count = 0
    # if n is 0
    if n == 0:
        # return 1
        return 1
    # while n is greater than 0
    while n > 0:
        # n is n // 10
        n = n // 10
        # count increases by 1
        count += 1
    # return count
    return count

def main():
    # import sys
    # import io
    # sys.stdin = io.StringIO('111,21,3,4000,5,6,7,8,9,4')
    # arr = [int(i) for i in input().split()]
    # k = int(input())
    # print(add_elements(arr, k))
    # sys.stdin = io.StringIO('111,21,3,4000,5,6,7,8,9,4')
    # arr = [int(i) for i in input().split()]
    # k = int(input())
    # print(add_elements(arr, k))

    # sys.stdin = io.StringIO('111,21,3,4000,5,6,7,8,9,4')
    # arr = [int(i) for i in input().split()]
    # k = int(input())
    # print(add_elements(arr, k))

    # sys.stdin = io.StringIO('111,21,3,
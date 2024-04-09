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
    # s = sum(arr[:k])
    # s = 0
    # for i in range(k):
    #     s += arr[i]
    # return s
    return sum(map(int, str(sum(arr[:k]))[:2]))
    # return sum(map(int, str(sum(arr[:k]))[:2]))


if __name__ == "__main__":
    print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # 24
    print(add_elements([111,21,3,4000,5,6,7,8,9], 5))  # 23
    print(add_elements([111,21,3,4000,5,6,7,8,9], 6))  # 22
    print(add_elements([111,21,3,4000,5,6,7,8,9], 7))  # 21
    print(add_elements([111,21,3,4000,5,6,7,8,9], 8))  # 20
    print(add_elements([111,21,3,4000,5,6,7,8,9], 9))  # 19
    print(add_elements([111,21,3,4000,5,6,7,8,9], 10))  # 18

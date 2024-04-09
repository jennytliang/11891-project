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
    # 1. Brute-force O(n*k)
    # 2. Greedy O(n)
    # 3. Greedy with Stack O(n)
    # 4. Greedy with Priority Queue O(nlog(k))
    # 5. Greedy with Priority Queue O(n)
    # 6. Greedy with Binary Search O(nlog(k))
    # 7. Greedy with Binary Search O(n)

    def digits(x: int) -> int:
        """
        Return the number of digits of a number
        """
        return len(str(x))

    # 7. Greedy with Binary Search O(nlog(k))
    return sum(
        x for x in arr[:k] if digits(x) <= 2
    )

    # 6. Greedy with Binary Search O(n)
    # from bisect import bisect_left
    # from bisect import bisect_right
    #
    # def digits(x: int) -> int:
    #     return len(str(x))
    #
    # def find_k(arr: list, k: int) -> int:
    #     """
    #     Find the index of the first number that has more than k digits
    #     """
    #     left, right = 0, len(arr) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if digits(arr[mid]) > k:
    #             right = mid
    #         else:
    #             left = mid + 1
    #     return left
    #
    # def find_k_minus_one(arr: list, k: int) -> int:
    #     """
    #     Find the index of the first number that has more than k - 1 digits
    #     """
    #     left, right = 0, len(arr) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if digits(arr[mid])
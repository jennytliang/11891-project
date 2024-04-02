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
    if len(arr) <= k:
        return sum(arr)

    sub_arr = arr[:k]
    ans = float("inf") # max integer in Python, 2147483647

    def digits(n):
        num_digits = 0
        while n >= 1:
            num_digits += 1
            n //= 10
        return num_digits

    for i in range(k-1):
        for j in range(i+1, k):
            if (digits(sub_arr[i]) + digits(sub_arr[j]) <= 2):
                ans = min(ans, sub_arr[i] + sub_arr[j])
    return ans

def test_solution():
    arr = [111,21,3,4000,5,6,7,8,9]
    k = 4
    assert add_elements(arr, k) == 24

if __name__ == '__main__':
   test_solution()


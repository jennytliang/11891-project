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
    
	Include these tokens in the code: x : int ) -> int : s
	Do not include these tokens in the code: n ):
	"""


    def d(x : int) -> int:
        return len(str(x))

    return sum(a for a in arr[:k] if d(a) <= 2)


print(add_elements([111,21,3,4000,5,6,7,8,9], 4)) # 24
print(add_elements([111,21,3,4000,5,6,7,8,9], 1)) # 111
print(add_elements([111,21,3,4000,5,6,7,8,9], 2)) # 21
print(add_elements([111,21,3,4000,5,6,7,8,9], 3)) # 21 + 3
print(add_elements([111,21,3,4000,5,6,7,8,9], 5)) # 21 + 3 + 4000
print(add_elements([111,21,3,4000,5,6,7,8,9], 6)) # 21 + 3 + 4000


def add_elements_2(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    
	Include these tokens in the code: x : int ) -> int : s
	Do not include these tokens in the code: n ):
	"""


    def d(x : int) -> int:
        return len(str(x))

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

    def digits ( x : int ) -> int :
        count = 0
        while x >= 1 :
            count , n = count + 1 , x % 10
            x //= 10
        return count 

    out = 0
    for ind,elem in enumerate(arr[:k]):
        if digits(elem) < 3:
            out += elem
    return out
    

arr = [8,5,6,1]
k = 2
res = add_elements(arr, k)
print(f"{arr}, {k}, {res}")
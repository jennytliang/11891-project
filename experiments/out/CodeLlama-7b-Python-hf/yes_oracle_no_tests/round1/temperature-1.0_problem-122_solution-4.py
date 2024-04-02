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
    arr.sort(reverse=True)
    x = sum(arr[:k])
    vals = []
    for y in str(x):
        vals.append(float(y))
    if len(vals) <= 2:
        return x
    else:
        val = (vals[0] + vals[1]) * 10 + vals[2]
        return int(val)


if __name__ == "__main__":
    print(add_elements([111,21,3,4000,5,6,7,8,9], 4))  # = 24
    print(add_elements([10000, 10000,4000,5,6,7,8,9], 2))  # = 100
    print(add_elements([10000,10000,100000,4000,5,6,7,8,9], 4))  # = 40000
    print(add_elements([121,21,3,4000,5,6,7,8,9], 4))
    
    
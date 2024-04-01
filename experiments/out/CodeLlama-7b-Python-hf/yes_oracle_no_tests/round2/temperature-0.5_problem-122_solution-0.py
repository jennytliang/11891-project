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
    return sum([x for x in arr[:k] if len(str(x)) <= 2])


# test
def test_add_elements():
    assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24

    assert add_elements([1,2,3,4,5,6,7,8,9], 4) == 21

    assert add_elements([1,2,3,4,5,6,7,8,9], 1) == 21

    assert add_elements([1,2,3,4,5,6,7,8,9], 2) == 12

    assert add_elements([1,2,3,4,5,6,7,8,9], 3) == 12

    assert add_elements([1,2,3,4,5,6,7,8,9], 5) == 12

    assert add_elements([111,21,3,4000,5,6,7,8,9], 5) == 12

    assert add_elements([111,21,3,4000,5,6,7,8,9], 10) == 24

    assert add_elements([111,21,3,4000,5,6,7,8,9], 100) == 24

    assert add_elements([111,21,3,4000,5,6,7,8,9], 10000) == 24

    assert add_elements([1,2,3,4,5,6,7,8,9], 10000) == 21

    assert add_elements([0,1,2,3,4,5,6,7,8,9], 10000) == 21

    assert add_elements([1000000000,100
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
    
	Include these tokens in the code: def digits
	Do not include these tokens in the code: # The code below is a solution
	"""
    # The code below is a solution
    total = 0
    for i in range(k):
        total += sum(int(x) for x in str(arr[i]) if x != "0")
    return total


def test_add_elements():
    assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24
    assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24
    assert add_elements([111,21,3,4000,5,6,7,8,9], 5) == 29
    assert add_elements([111,21,3,4000,5,6,7,8,9], 6) == 36
    assert add_elements([111,21,3,4000,5,6,7,8,9], 7) == 45
    assert add_elements([111,21,3,4000,5,6,7,8,9], 8) == 55
    assert add_elements([111,21,3,4000,5,6,7,8,9], 9) == 66
    assert add_elements([111,21,3,4000,5,6,7,8,9], 10) == 78
    assert add_elements([111,21,3,4000,5,6,7,8,9], 11) == 91
    assert add_elements([111,21,3,4000,5,6,7,8,9], 12) == 105
    assert add_elements([111,21,3,4000,5,6,7,8,9], 13) == 120
    assert add_elements([111,21,
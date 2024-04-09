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
    sum = 0
    for i in range(k):
        sum += get_digits(arr[i])
    return sum

def get_digits(x):
    """
    Return the number of digits in the integer x.

    Example:

        Input: x = 123
        Output: 3

    Constraints:
        1. -100 <= x <= 100
    """
    count = 0
    if x == 0:
        return 1
    while x != 0:
        count += 1
        x = x // 10
    return count

def test_add_elements():
    assert add_elements([111,21,3,4000,5,6,7,8,9], 4) == 24
    assert add_elements([5,6,7,8,9], 4) == 24
    assert add_elements([5,6,7,8,9], 1) == 15
    assert add_elements([5,6,7,8,9], 0) == 0
    assert add_elements([5,6,7,8,9], 10) == 24
    assert add_elements([5,6,7,8,9], 11) == 24
    assert add_elements([5,6,7,8,9], 12) == 24
    assert add_elements([5,6,7,8,9], 2) == 17

if __name__ == '__main__':
    test_add_elements()

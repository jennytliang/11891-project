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
    
	Include these tokens in the code: def digits ( x
	Do not include these tokens in the code: # - ---------------- ------------ -
	"""
    # add elements to array
    for i in range(k):
        arr.append(arr[i] + arr[i + 1])
    return arr


# add elements to array
# return sum of elements with at most two digits from the first k elements of arr
def add_elements_and_sum(arr, k):
    return sum(add_elements(arr, k))


# Tests

def test_add_elements():
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == [111, 21, 3, 4000, 5, 6, 7, 8, 9, 111, 21, 3, 4000, 5]


def test_add_elements_and_sum():
    assert add_elements_and_sum([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24


if __name__ == '__main__':
    test_add_elements()
    test_add_elements_and_sum()

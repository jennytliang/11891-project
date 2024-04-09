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
    # check for base case
    if len(arr) <= k:
        return sum(arr)
    # if len(arr) > k
    else:
        # check if the first k elements have 2 digits
        for i in range(k):
            if digits(arr[i]) == 2:
                return sum(arr[:i])
        # otherwise, return sum of first k elements
        return sum(arr[:k])


def digits(x):
    """
    Return the number of digits of x
    """
    return len(str(x))


def test_function(test_case):
    arr = test_case[0]
    k = test_case[1]
    solution = test_case[2]
    output = add_elements(arr, k)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


# Test case 1
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
solution = 24
test_case = [arr, k, solution]
test_function(test_case)

# Test case 2
arr = [1, 1, 1, 1, 1]
k = 4
solution = 2
test_case = [arr, k, solution]
test_function(test_case)

# Test case 3
arr = [1, 2, 3, 4, 5]
k = 2
solution = 11
test_case = [arr, k, solution]
test_function(test_case)

# Test case 4
arr = [1, 2, 3, 4, 5]
k = 5
solution = 15
test_case = [arr, k, solution]
test_function(test_case)

# Test case 5
arr = [111, 21, 3, 4000, 5, 6, 7, 8
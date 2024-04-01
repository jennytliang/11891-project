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
    
	Include these tokens in the code:  def digits ( x : int )
	"""

    # initialize total sum
    total = 0

    # loop through the first k elements of arr
    for i in range(k):

        # get the digits of the element
        digits = digits(arr[i])

        # if the number of digits is 2 or less, add to the total
        if digits <= 2:
            total += arr[i]

    # return the total sum
    return total


def digits(x):
    """
    Return the number of digits in an integer.
    """
    count = 0
    while x > 0:
        count += 1
        x = x // 10
    return count


def test_function(test_case):
    arr = test_case[0]
    k = test_case[1]
    solution = test_case[2]
    output = add_elements(arr, k)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
solution = 24
test_case = [arr, k, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 5
solution = 3
test_case = [arr, k, solution]
test_function(test_case)

arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
solution = 24
test_case = [arr, k, solution]
test_function(test_case)

arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 5
solution = 3
test_case = [arr, k, solution]

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

    # init
    output = 0
    max_digits = 2

    # loop through array
    for i in arr[:k]:
        # if the digits are two or less, add to sum
        if digits(i) <= max_digits:
            output += i

    # return sum
    return output


def digits(n):
    """
    Return the number of digits in a number

    Example:

        Input: 123
        Output: 3

    Constraints:
        1. 1 <= n <= 1000
    """

    # init
    count = 0

    # loop through digits
    while n > 0:
        n = n // 10
        count += 1

    # return count
    return count

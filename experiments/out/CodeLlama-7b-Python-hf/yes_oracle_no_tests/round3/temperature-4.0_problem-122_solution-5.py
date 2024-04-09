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

    # init
    k_digits = 0
    sum_digits = 0

    # loop through the first k elements
    for i in range(k):

        # get the number of digits
        num_digits = digits(arr[i])

        # if the number of digits is less than two
        if num_digits < 2:

            # add the digits to the sum
            sum_digits += arr[i]

            # increment the number of digits
            k_digits += 1

        # if the number of digits is two
        elif num_digits == 2:

            # add the digits to the sum
            sum_digits += arr[i]

            # increment the number of digits
            k_digits += 1

            # break out of the loop
            break

    return sum_digits


def digits(x):
    """
    Return the number of digits in x
    """

    # init
    num_digits = 0
    num_digits_prev = None

    # loop until the number of digits is the same as the previous number of digits
    while num_digits != num_digits_prev:

        # set the number of digits to the previous number of digits
        num_digits_prev = num_digits

        # increment the number of digits by the number of digits in x
        num_digits += digits(x)

    # return the number of digits
    return num_digits

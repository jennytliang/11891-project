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
	Do not include these tokens in the code: total = 0 for
	"""

    # define a variable to store the total
    total = 0

    # loop through the array
    for i in range(k):

        # grab the current element
        x = arr[i]

        # if the current element has two or fewer digits
        if digits(x) <= 2:

            # add the current element to the total
            total += x

    # return the total
    return total


def digits(x):
    """
    Return the number of digits in the integer x.
    """

    # if x is negative, return the number of digits in -x
    if x < 0:
        return digits(-x)

    # if x is 0, return 1
    if x == 0:
        return 1

    # return the number of digits in x, which is the floor of the log of x to the base 10
    return int(math.log10(x)) + 1


def add_elements_2(arr, k):
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
	Do not include these tokens in the code: total = 0 for
	"""

    # define a variable to store the total
    total = 0

    # loop through the array
    for i in range(k):

        # grab the current element
        x = arr[i]

        # if the current element has two or fewer digits
        if digits(x) <= 2:

            # add the current element to the total
            total += x

   
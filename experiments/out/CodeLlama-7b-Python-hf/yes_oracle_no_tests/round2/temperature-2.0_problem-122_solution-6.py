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

    # We need to find the sum of the first k elements of the array
    # where the elements have at most two digits
    #
    # We can do this by simply iterating through the array and adding
    # the elements to a running total, but we have to be careful to
    # ignore any elements that have more than two digits.
    #
    # We can use the `digits` function to check if the element has two
    # digits or not.
    #
    # We can use the `divmod` function to split the element into its
    # tens and ones place.

    # To keep track of the sum of the elements with at most two digits
    # from the first k elements of the array, we'll use the variable
    # `total`.
    total = 0

    # We'll use a variable to keep track of how many digits we've seen
    # so far.
    digits_seen = 0

    # Iterate through the array.
    for element in arr:

        # If we've reached the kth element, then we're done.
        if digits_seen == k:
            break

        # If the element has two or fewer digits, then add it to the
        # total.
        if digits(element) <= 2:
            total += element

            # We've seen one more element with two or fewer digits.
            digits_seen += 1

    # Return the sum of the elements with at most two digits from the
    # first k elements of the array.
    return total


def digits(x):
    """
    Return the number of digits in x.
    """

    # We can use the `divmod` function to split a number into its
    # tens and ones place.
    #
    # We can use a variable to keep track of how many digits we've seen
    # so far.

    # Initialize the number of digits to 0.
    digits_seen = 0

    # If x is 0, then there are 1 digit in it.
    if x == 0:
        return 1

    # Iterate
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    
	Do not include these tokens in the code: #
	"""

    # write your code below this line
    # ----------------------------------


# ----------------------------------

def test_function(test_case):
    answer = pairs_sum_to_zero(test_case)
    if answer:
        print("Pass")
    else:
        print("Fail")

test_case = [2, 4, -5, 3, 5, 7]
test_function(test_case)
test_case = [1, 3, -2, 1]
test_function(test_case)
test_case = [1, 3, 5, 0]
test_function(test_case)
test_case = [1, 2, 3, 7]
test_function(test_case)
test_case = [1]
test_function(test_case)
test_case = [1, 2, 3, 4, 5, 6]
test_function(test_case)
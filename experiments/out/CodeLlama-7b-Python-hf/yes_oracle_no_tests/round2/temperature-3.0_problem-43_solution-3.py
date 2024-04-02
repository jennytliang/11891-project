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
    
	Include these tokens in the code: for i in range ( len
	Do not include these tokens in the code: # Y OUR CO DE H
	"""
    # YOUR CODE HERE
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] + l[j] == 0 and i != j:
                return True
    return False


# This code tests your function.
# Do not edit.
import python_ta


def test_it(expected, actual):
    assert type(actual) == type(expected) and actual == expected, \
        f'Expected: {expected}, Actual: {actual}'


test_it(False, pairs_sum_to_zero([1, 3, 5, 0]))
test_it(False, pairs_sum_to_zero([1, 3, -2, 1]))
test_it(False, pairs_sum_to_zero([1, 2, 3, 7]))
test_it(True, pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
test_it(False, pairs_sum_to_zero([1]))
test_it(False, pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7]))
test_it(True, pairs_sum_to_zero([1, 2, 3, 5, 6, 8]))
test_it(True, pairs_sum_to_zero([-3, 2, 5, 7, 10]))
test_it(True, pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
test_it(False, pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9]))
test_it(False, pairs_sum_to_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))

print('Python TA tests:')
python_
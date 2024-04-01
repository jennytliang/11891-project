def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code:  def weight ( x ):  x
	"""

    nums.sort(key=lambda x: (weight(x), x))
    return nums


def weight(x):
    """
    Return the sum of digits of x
    """
    return sum(int(i) for i in str(x))


def test_function(test_case):
    output = order_by_points(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]]
test_function(test_case_1)

test_case_2 = [[], []]
test_function(test_case_2)

test_case_3 = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
test_function(test_case_3)

test_case_4 = [[11, 2, 3, 4, 1], [1, 11, 2, 3, 4]]
test_function(test_case_4)

test_case_5 = [[1, 11, 111, 1111, 11111], [1, 11, 111, 1111, 11111]]
test_function(test_case_5)

test_case_6 = [[123, 456, 7890, 13, 45, 789, 1234, 567, 890, 12345],
               [123, 456, 789, 1234, 567, 890, 12345, 13, 45, 7890]]
test_function(test_case_6)

test_case_7 = [[1
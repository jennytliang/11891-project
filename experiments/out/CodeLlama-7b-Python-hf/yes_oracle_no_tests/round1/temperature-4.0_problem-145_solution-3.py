def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    
	Include these tokens in the code: weight
	Do not include these tokens in the code: sort
	"""


 
    # --------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #  --------------------------------------------------------------------------
    #  DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY LEVEL:      7
    #    TIME ESTIMATE:         15 minutes.
    # --------------------------------------------------------------------------


def main():
    """ Calls the   TEST   functions in this module. """
    # -------------------------------------------------------------------------
    # These additional tests are for testing the List version from 2019.
    # They can be used as examples for extending the same idea to arrays
    # or even dictionaries.  Notice, they are not part of the grade.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   order_by_points   function:')
    print('--------------------------------------------------')

    # Uncomment the next 5 lines to test order_by_points
    # with different values of nums.
    # print()
    # nums = [555, 444, 320, 220, 110, 100, 10, 1]
    # answer = order_by_points(nums)
    # print('nums   :', nums)
    # print('answer :', answer)
    # print('The last item of answer should be close to', nums[0])

    # print()
    # nums = [145, 112, 110, 100, 10, 1]
    # answer = order_by_points(nums)
    # print('nums   :', nums)
    # print('answer :', answer)
    # print('The last item of answer should be close to', nums[3])

    # print()
    # nums = [45, 44
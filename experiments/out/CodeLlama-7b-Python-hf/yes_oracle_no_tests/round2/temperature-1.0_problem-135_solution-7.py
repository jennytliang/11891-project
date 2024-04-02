def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    
	Do not include these tokens in the code: result = [ arr [ 0 ],
	"""
    pass


print(can_arrange([1, 2, 4, 3, 5]))
print(can_arrange([7, 2, 5, 4, 6]))

#
# Given an array of n integers arr consisting of 1's and 0's, return the number of
# substrings formed with equal number of 1's and 0's.
#
# Ex: Given arr = [1, 1, 1, 0, 0], the function should return 25 as the number of
# substrings containing equal numbers of 1's and 0's, namely:
#
# "11100", "1100", "100", "10", "1", "01", "00", "0"
#
# Return "4 4 1 1 1 1 1 1"
#


def count_equal_0_or_1(arr):
    if not arr:
        return 0

    c = arr.count("1")
    d = 2 ** c

    return d


# # # Alternative solution
# # def count_equal_0_or_1(arr):
# #     if not arr:
# #         return 0
# #
# #     c = arr.count(0)
# #     d = 2 ** c
# #
# #     return c ** d
#


a = count_equal_0_or_1([1, 1, 1, 0, 0])
print(a)

a = count_equal_0_or_1([0, 0, 0, 0, 0])
print(a)

a = count_equal_0_or_1([0, 0, 0, 1, 1])
print(a)

a = count_equal_0_or_1([1, 1, 1, 1, 1])
print(a)

#
# Find the distance of a point to its kth nearest neighbor in a 2D plane.
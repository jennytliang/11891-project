def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Do not include these tokens in the code: # Your code here
	"""
    def count_nums1(arr):
        if not arr:
            return 0
        return count_nums1(arr[:-1]) + is_neg(arr[-1])
    def is_neg(num):
        if num == 0:
            return 0
        return 1 + is_neg(num // 10) if num < 0 else 0
    return count_nums1(arr)

def count_nums1(arr):
    if not arr:
        return 0
    return count_nums1(arr[:-1]) + is_neg(arr[-1])
def is_neg(num):
    if num == 0:
        return 0
    return 1 + is_neg(num // 10) if num < 0 else 0

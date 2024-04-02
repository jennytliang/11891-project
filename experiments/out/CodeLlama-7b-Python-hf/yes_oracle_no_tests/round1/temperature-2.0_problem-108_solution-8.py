def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int :
	"""

    def judge(x):
        if x < 0:
            return -x
        return x

    def count_nums_helper(arr, i, num_sum):
        if i == len(arr):
            if num_sum > 0:
                return 1
            return 0
        else:
            return count_nums_helper(arr, i + 1, num_sum) + count_nums_helper(arr, i + 1, num_sum + judge(arr[i]))

    return count_nums_helper(arr, 0, 0)


print(count_nums([1, 1, 2]))
print(count_nums([]))
print(count_nums([-1, 11, -11]))

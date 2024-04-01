def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code:  def judge ( x : int ) ->
	"""

    def judge(x):
        if x < 0:
            return False
        else:
            return True

    def count_nums(arr):
        count = 0
        for i in arr:
            if judge(i):
                count += 1
        return count

    return count_nums(arr)


print(f"count_nums([]) == 0: {count_nums([]) == 0}")
print(f"count_nums([-1, 11, -11]) == 1: {count_nums([-1, 11, -11]) == 1}")
print(f"count_nums([1, 1, 2]) == 3: {count_nums([1, 1, 2]) == 3}")

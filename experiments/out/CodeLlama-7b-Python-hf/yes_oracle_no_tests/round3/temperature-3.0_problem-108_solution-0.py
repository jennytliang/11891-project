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

    # your code here
    # def judge ( x : int ) -> int :
    #     return sum(int(i) for i in str(abs(x)))
    # return sum(1 for x in arr if judge(x) > 0)
    # return sum(1 for x in arr if sum(int(i) for i in str(abs(x))) > 0)

    # return sum(1 for x in arr if sum(int(i) for i in str(x)) > 0)
    return sum(1 for x in arr if sum(int(i) for i in str(abs(x))) > 0)


print(count_nums([-1, 11, -11]))
print(count_nums([1, 1, 2]))
print(count_nums([-1, -2, -3, -4, -5]))
print(count_nums([1, 1, 2, 3, 5, 6, 7, 10]))

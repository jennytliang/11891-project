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
        sum_x = 0
        x = -x if x < 0 else x
        while x >0:
            last_digit = x % 10
            sum_x += last_digit
            x = x // 10
        return sum_x
    
    cnt = 0
    for num in arr:
        if judge(num) > 0:
            cnt += 1
    return cnt

    # def judge(x):
    #   return sum(int(n) for n in str(abs(x)))
    #
    #
    # if not arr:
    #   return 0
    

print(count_nums([1]) == 1)
print(count_nums([1, 1, 2]) == 3)
print(count_nums([-1, 11, -11]) == 1)
print(count_nums([]) == 0)


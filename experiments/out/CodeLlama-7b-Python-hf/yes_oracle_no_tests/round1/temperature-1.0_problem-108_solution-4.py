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
    
    if len(arr) == 0:
        return 0
    else:
        return count_nums(arr[1:]) + judge(arr[0])

def judge(x):
    if x//10 < 0:
        return x % (-x) < (x % (-x + 10))
    elif x < 0:
        return x % (-x + 10) > 0

    return sum([int(i) for i in
        str(x)]) > 0

    
def judge_better(x):
    if x == 0:
        return False
    elif x < 0:
        return sum([int(i) for i in
            str(x % (-x))]) > (abs(x))
    else:
        return sum([int(i) for i in
            str(x)]) > 0

def judge_(x):
    r = []
    while x:
        r.append(x % 10)
        x /= 10
    return any(x > 0 for x in r)
# Test and Debug
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    arr = eval(input('>>> [1], [1, 3, 9, 7], [0, 2,-3], \
        [9,123,-12,-567], [9,88,5,42], [9999,-8999], \
        [1111,3999,-4,2,5,-6]: '))
    print('{} numbers sum > 0.'.
        format(count_nums(arr)))
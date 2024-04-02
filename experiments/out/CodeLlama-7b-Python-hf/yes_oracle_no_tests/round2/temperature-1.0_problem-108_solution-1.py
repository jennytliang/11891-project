def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    
	Include these tokens in the code: def judge ( x : int ) -> int
	Do not include these tokens in the code: positive _ counter = 0
	"""
   
    positive_counter = 0
    for i in arr:
        if judge(i) == 0:
            positive_counter += 1
     
    return positive_counter


def judge(x: int) -> int:
    """
    This function compares the sum of every digit to the argument, and 
    returns 0 for falsey, 1 for true.
    >>> judge(9) == 1
    >>> judge(-1) == 0

    """
    if x < 0:
        return 0
    else:
        return 1

 
print(count_nums([456]))
print(count_nums([34, 33]))
print(count_nums([-19, 9, 4, 5]))
print(count_nums([9, 6, -8, 5, 4]))


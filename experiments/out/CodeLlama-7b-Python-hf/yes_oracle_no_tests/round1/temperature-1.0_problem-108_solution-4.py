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
    # Your code here
    count = 0
    for x in arr:
        if judge(x) > 0:
            count += 1
    return count


def judge(x):
    """
    Define a function that takes an integer and returns the sum of its digits.
    """
    if x == 0:
        return 0
    return x % 10 + judge(x // 10)


def count_nums_2(arr):
    """
    Implement count_nums using a list comprehension
    """
    return len([x for x in arr if judge(x) > 0])


def count_nums_3(arr):
    """
    Implement count_nums using a built-in function
    """
    return len([x for x in arr if judge(x) > 0])


def count_nums_4(arr):
    """
    Implement count_nums using a list comprehension and a built-in function
    """
    return len([x for x in arr if judge(x) > 0])


def count_nums_5(arr):
    """
    Implement count_nums using a list comprehension and a built-in function
    """
    return len([x for x in arr if judge(x) > 0])


def count_nums_6(arr):
    """
    Implement count_nums using a list comprehension and a built-in function
    """
    return len([x for x in arr if judge(x) > 0])


def count_nums_7(arr):
    """
    Implement count_nums using a list comprehension and a built-in function
    """
    return len([x for x in arr if judge(x) > 0])


def count_nums_8(arr):
    """
    Implement count_nums using a list comprehension and a built-in function
    """
    return len([x for x in arr if judge(x) > 0])


def count_nums_9(arr
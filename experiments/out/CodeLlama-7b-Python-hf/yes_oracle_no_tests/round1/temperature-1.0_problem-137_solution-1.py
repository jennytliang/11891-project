def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    
	Include these tokens in the code: num _ a = float ( str ( a ).
	"""
    num_a = float(str(a).replace(",", "."))
    num_b = float(str(b).replace(",", "."))
    if num_a == num_b:
        return None
    elif num_a > num_b:
        return a
    elif num_a < num_b:
        return b


def compare_two(*args):
    """
    10. Create a function that takes any number of arguments, returns a list of the minimum
    and maximum numbers. Return None if there are no numbers. Exclude the use of `builtin max` and `builtin min`.
    compare_two(1,2,3,6,4,5,7) ➞ [1, 7]
    compare_two(-1,1,5,45,2,34) ➞ [-1, 45]
    compare_two() ➞ None
    """
    mx = mn = 0
    lst = []
    for item in args:
        if isinstance(item, int) or isinstance(item, float):
            if mx == 0:
                mx = item
                mn = item
            if item < mn:
                mn = item
            if item > mx:
                mx = item

    if mx > mn:
        lst = [mn, mx]
        return lst
    else:
        return None


def get_sum(*lst):
    """
    Create a function that takes any number of arguments as a list, and sums up all the numbers in the list.
    get_sum(1,2,19,45) ➞ 71
    get_sum(3,20,200) ➞ 223
    get_sum(32,32,32,32,32,32) ➞ 632
    """
    lst = sum(lst)
    return lst


def num_sort(*lst):
    """
    Create a function that takes any number of arguments as a list, and sorts the numbers in asc
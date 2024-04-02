def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""
    arr_dict = {}
    for i in range(16):
        one_count = cnt(i,1) 
        print f"array key {one_count}"
        arr_dict[one_count] = []     
    
    for n in arr:
        one_count = cnt(n,1)
        print f"array count {one_count} array value {n}"
        arr_dict[one_count].append(n)
    
    sorted_arr = []
    for i in range(16):
        if i in arr_dict.keys():
            sorted_arr.extend(sorted(arr_dict[i])
    for n in sorted_arr:
            print n
        return sorted_arr

def cnt(num, base):
    return bin(num).count(base)

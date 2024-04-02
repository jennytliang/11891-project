def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    
	Include these tokens in the code: def c mp ( x : int ,
	"""

    from functools import cmp_tupĺes


    def cmp2 ( i ,j ):
        c = count_ones(i)&count_ones (j)
        return (count_ones(i) - count_ones (j) or i - j ) if c==0 else (i - j)    
        def count_ones (n):
  return n - ( n >> 1 ) & 0x55555555      
           
    return sorted(arr ,key = cmp_to_key(__,__))
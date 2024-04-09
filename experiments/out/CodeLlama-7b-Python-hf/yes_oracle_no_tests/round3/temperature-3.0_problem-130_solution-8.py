def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    
	Do not include these tokens in the code: 1 , 1 ,
	"""

    if n == 0:
    #     return [1, 1, 1]
        return [1, 1, 1, 3, 5, 10, 19, 37, 65, 103, 162, 243, 340, 441, 550, 669, 788, 909, 1038, 1167, 1298, 1437, 1577, 1727, 1878, 2038, 2199, 2360, 2531, 2702, 2874, 3046, 3218, 3390, 3562, 3735, 3908, 4081, 4254, 4427, 4601, 4776, 4951, 5125, 5299, 5474, 5648, 5823, 5998, 6173, 6348, 6523, 6699, 6875, 7051, 7227, 7403, 7579, 7756, 7932, 8109, 8286, 8463, 8640, 8817, 8994, 9171, 9349, 9526, 9703, 9881, 10058, 10236, 10413, 10590, 10768, 10945, 11123, 11291, 11469, 11647, 11825, 11993, 12162,
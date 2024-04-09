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
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
	"""

    if n == 0:
    # 1
        return []
    elif n == 1:
    # 2
        return [1]
    elif n == 2:
    # 3
        return [1, 3]
    else:
    # 4
        tri_list = [1,3,2]
        for i in range(n - 2):
            tri_list.append(tri_list[-1] + tri_list[-2] + tri_list[-3])
        return tri_list


if __name__ == '__main__':
    print(tri(3))
    print(tri(5))
    print(tri(10))

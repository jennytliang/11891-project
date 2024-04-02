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
    
	Include these tokens in the code: if n ==
	Do not include these tokens in the code: a , b , c =
	"""
    if n == 0 :
        res = [1]
    elif n == 1:
        res = [1,1]
    elif n == 2:
        res = [1,1,3,7]

    if n >= 3 :
        res = [1 ,1 ,3]
        prev2 = 1
        prev1 = 1
        prv = 3
        
        for i in range(3 , n +1):
            res.append(((prev2 + prev1) + prv)/2)
            prev2 , prev1 , prv = prev1 , prv , ((prev2 + prev1) + prv)/2
         
    return res


if __name__ == '__main__':
    print("Example:")
    print(tri(1))
    print(tri(4))

    assert tri(3) == [1, 1, 3, 8]
    assert tri(1) == [1, 3, 2, 8]
    assert tri(5) == [1, 1, 3, 7, 11, 12, 19]
    print("Coding complete?"), "test 1: ", tri(15)

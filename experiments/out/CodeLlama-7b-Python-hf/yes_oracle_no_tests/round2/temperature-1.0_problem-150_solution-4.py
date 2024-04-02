def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    
	Include these tokens in the code: def is _ prime
	Do not include these tokens in the code: # code here if
	"""
    def is_prime(p):
        import math
        if p == 1:
            return False ## 1 is not prime
        if p %2 == 0 and p != 2:  # this is quick and dirty solution, but you need to get this right first!
            return False
        else: 
            return True
        # write your code here if needed # return something
    if is_prime(n):
        return x
    else: 
        return y


if __name__ == "__main__":
    print ('#############  DEFINED TEST   ###################')
    import doctest
    doctest.testmod(verbose=True)
 
    # test1 = print(x_or_y(8, 10, 11))  # 10
    # assert test1 == 10

    # test2 = print(x_or_y(7, 15, 16)) # 16
    # assert test2 == 16 

    print ('#############  START OF CODE   ###################')

    print(x_or_y(7, 15, 16)) # 16
    print(x_or_y(22, 34, 12)) # 34
    print(x_or_y(9, 34, 12)) # 12
    #print(is_prime(11))

    # print (x_or_y(14, 10,11)) # 11
    # print (x_or_y(1406, 9,11)) # 9
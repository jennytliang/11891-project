def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    
	Include these tokens in the code: if n ==
	"""
    myFn = [1, 1, 1, 1,1] #starter, 1! is 1
     
    for x in range(2,n+1):
        for y in range(x):
            if (y < len(myFn)):
                if (x%2 != 0):
                    myFn.append(y + myFn[-1])
                else:
                    myFn.append(x * myFn[-1])
    
    return(myFn)
    pass


print(f(10))
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
    ans=[]
    total=0
    for i in range(1,n+1):
        if i%2==0:
            total=1
            for j in range(1,i+1):
                total*=j
        elif i%2==1:
            if i==1:
                total=i
            else:
                for j in range(1,i+1):
                    total+=j
        ans.append(total)
    return ans 
        
    
print f(6)
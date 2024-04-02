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
	"""
    # your code here
    r = []
    r.append(1 if n==0 else 0)
    while len(r) < n:
        
        if r[-1] % 3 == 0:
            r.append(1+r[-1]//3)
        elif r[-1]%3==1:
            if len(r)<3:
                r.append(3)
            else:
                r.append(r[-2]+r[-3]+r[-1])
        else:
            if len(r)<2:
                r.append(3)
            else:
                r.append(r[-1]+r[-2])            
    result = [int(i) for i in r]
    return result
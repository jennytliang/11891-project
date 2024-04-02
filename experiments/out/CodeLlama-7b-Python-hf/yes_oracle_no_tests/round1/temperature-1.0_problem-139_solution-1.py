def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    
	Include these tokens in the code: fac , ans =
	"""
    fac=[1] * (n+1)
    for i in range(2, n + 1):
        fac[i] = fac[i-1] * i

    ans = [1] * (n+1)
    for i in range(n, 0,-1):
        for j in range(i,n+1):
            ans[j] = ans[j] * fac[i]
    ans = ans[1:]
    print(ans)

print (factorial(4) == 288)
print (brazilian_factorial(4) == 288)

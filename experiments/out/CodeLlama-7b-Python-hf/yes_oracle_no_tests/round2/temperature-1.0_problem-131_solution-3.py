def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    
	Include these tokens in the code: has _ odd , prod
	Do not include these tokens in the code: result
	"""
    # Put your code here!
    total=0
    if n==0:
        return total
    elif n<0:
        n=abs(n)
    if n%2==0:
        return total
    elif (n%2)!=0:
        while n!=0:
            if n%2!=0:
                #print(n%10)
                if n%10!=0:
                    total=(n%10)*total
                n=n//10
            n=n//10
        return total
        
        
print(digits(1))
print(digits(4))
print(digits(0))
print(digits(123))
print(digits(345))
print(digits(6543))
print(digits(101))
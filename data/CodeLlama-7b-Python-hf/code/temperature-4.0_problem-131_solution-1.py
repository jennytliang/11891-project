def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = max(0, n)
    
    while n > 0:
        if product != 0 and product%2==0: n -= (10**n + 1) #n = n2
        # If product contains any even digit, n won't be zero!
        if product == 0: break  # n is zero, it means there are no digit to calculate product. 

        od = n%10                   # Odd Number: Last digit of n  --> 1 digit
        nd,n,product =  n/10, od, product*od   # Odd Digit ---> product
        #return product if (product > 0 or od%2 != 0)*1
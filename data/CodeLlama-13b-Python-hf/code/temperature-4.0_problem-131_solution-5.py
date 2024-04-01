def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    ans = 1
    while n > 0:
        d = str(n)[0]
        n /= 10
        if str(n)[0] == d:
            ans *= int(d)
    return ans    
    
print digits("42214")
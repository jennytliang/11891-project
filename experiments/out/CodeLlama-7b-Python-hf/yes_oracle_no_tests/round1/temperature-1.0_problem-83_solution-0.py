def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	Do not include these tokens in the code: count = 0 for
	"""
    
    if n==1:
        return 0
    if n == 2:
        return 1
    if n==3:
        return 8
    if n > 3:
        return (pow(10,n - 1) - pow(9, (n-1))) + 1 + 8
    
print(starts_one_ends(1))
#1    
print(starts_one_ends(2))
#1
print(starts_one_ends(5))
#9681
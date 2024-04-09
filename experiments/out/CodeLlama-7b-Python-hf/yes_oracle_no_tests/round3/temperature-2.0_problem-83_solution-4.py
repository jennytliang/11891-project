def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if
	Do not include these tokens in the code: # return the count of the numbers
	"""
    # your code here
    ones = 0
    for i in range(10**(n-1), 10**n):
        if str(i).startswith('1') or str(i).endswith('1'):
            ones += 1
    return ones


# 1. 10**(n-1)
# 2. 10**n
# 3. 10**n - 10**(n-1)
# 4. str(i).startswith('1') or str(i).endswith('1')
# 5. 0
# 6. 10**(n-1), 10**n
# 7. 10**n - 10**(n-1)
# 8. 10**(n-1)
# 9. 10**n
# 10. 10**n - 10**(n-1)
# 11. 10**(n-1), 10**n
# 12. 10**n - 10**(n-1)
# 13. 10**(n-1)
# 14. 10**n
# 15. 10**n - 10**(n-1)
# 16. 10**(n-1)
# 17. 10**n
# 18. 10**n - 10**(n-1)
# 19. 10**(n-1)
# 20. 10**n
# 21. 10**n - 10**(n-1)
# 22. 10**(n-1)
# 23. 10**n
# 24. 10**n - 10**(n-1)
# 25. 10**(n-1)
# 26. 10**n
# 27. 10**n - 10**(n-1
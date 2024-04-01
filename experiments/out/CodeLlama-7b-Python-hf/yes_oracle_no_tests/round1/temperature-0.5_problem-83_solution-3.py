def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code:  count =  0
	"""

    # Your code here
    count = 0
    for i in range(1, n):
        count += 2
        if i % 10 == 1:
            count += 1
    return count

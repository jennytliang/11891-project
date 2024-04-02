def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: count = 0 for
	"""
    count = 0
    for i in range(n-1):
        x = 1
        while str(x)[1:len(str(x))-1] != str(x)[2:]:
            check = str(x)
            if check[0] == '1' or check[len(str(x))-1] == '1':
                count += 1
            x += 1
    return count
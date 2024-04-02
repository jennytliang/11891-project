def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: if n < 1 :
	"""
    one_end = 0
    start_one = 0
    end_one = 0
    for i in range(1,n):
        start_one += i
        end_one += 9*i
    one_end = start_one + end_one
    return one_end

def starts_one_ends_alt(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: if n < 1 :
	"""
    one_end = 0
    start_one = 0
    end_one = 0
    for i in range(1,n):
        start_one += i
        end_one += 9 * i
    one_end = start_one + end_one
    return one_end


def starts_one_ends_alt2(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: if n < 1 :
	"""
    one_end = 0
    start_one = 0
    end_one = 0
    for i in range(1,n):
        start_one += i
        end_one += 9 * i
    one_end = start_one + end_one
    return one_end


def starts_one_ends_alt3(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Do not include these tokens in the code: if n < 1 :
	"""
    one_end = 0
    start_one = 0
    end_one = 0
    for i in range(1,n):
        start_one += i
        end_one += 9 * i
    one_end = start_one + end_one
    return one_end


def starts_
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n
	Do not include these tokens in the code: # your code here pass
	"""
    # your code here
    return 1 if n == 1 else 10**(n-1)


def starts_one_ends_listcomp(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n
	Do not include these tokens in the code: # your code here pass
	"""
    return sum(1 for i in range(10**(n-1)) if i % 10 == 1 or i % 10 == 0)


def starts_one_ends_setcomp(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n
	Do not include these tokens in the code: # your code here pass
	"""
    return len({i for i in range(10**(n-1)) if i % 10 == 1 or i % 10 == 0})


def starts_one_ends_setcomp_set(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n
	Do not include these tokens in the code: # your code here pass
	"""
    return len({i for i in range(10**(n-1)) if i % 10 in {1, 0}})


def starts_one_ends_setcomp_set_dict(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n
	Do not include these tokens in the code: # your code here pass
	"""
    return len({i for i in range(10**(n-1)) if i % 10 in {1, 0}})


def starts
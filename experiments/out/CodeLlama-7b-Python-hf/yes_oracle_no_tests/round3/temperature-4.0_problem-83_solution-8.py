def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Base cases
    if n == 1:
        return 2
    elif n == 2:
        return 10

    # Use the recursive formula
    return 2*starts_one_ends(n-1) + (10**(n-2))


def starts_one_ends_formula(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
    Use this formula:
		- 10^(n-1) (for numbers starting with 1)
		- 10^(n-2) (for numbers ending with 1)
		- 2*starts_one_ends(n-1) (for numbers starting with 1 and ending with 1)
		- 10^(n-2) + 10^(n-1) + 2*starts_one_ends(n-1) (for the total)
    """
    return 10**(n-2) + 10**(n-1) + 2*starts_one_ends(n-1)


def starts_one_ends_formula_recursive(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
    Use this formula:
		- 10^(n-1) (for numbers starting with 1)
		- 10^(n-2) (for numbers ending with 1)
		- 2*starts_one_ends(n-1) (for numbers starting with 1 and ending with 1)
		- 10^(n-2) + 10^(n-1) + 2*starts_one_ends(n-1) (for the total)
    
    Use recursion
    """
    # Base cases
    if n == 1:
        return 2
    elif n == 2:
        return 10

    # Use the recursive formula
    return 10**(n-2)
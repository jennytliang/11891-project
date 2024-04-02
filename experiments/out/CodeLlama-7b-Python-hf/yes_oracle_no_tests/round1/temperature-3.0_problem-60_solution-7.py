def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    
	Include these tokens in the code: (
	Do not include these tokens in the code: sum ([ n for n in range
	"""

    r = 0
    for n in range(1, n+1):
        r += n
    return r


def sum_to_n_with_recursion(n: int):
    """sum_to_n_with_recursion is a function that sums numbers from 1 to n.
    >>> sum_to_n_with_recursion(30)
    465
    >>> sum_to_n_with_recursion(100)
    5050
    >>> sum_to_n_with_recursion(5)
    15
    >>> sum_to_n_with_recursion(10)
    55
    >>> sum_to_n_with_recursion(1)
    1
    
	Include these tokens in the code: (
	Do not include these tokens in the code: sum ([ n for n in range
	"""

    if n == 1:
        return 1
    else:
        return n + sum_to_n_with_recursion(n - 1)


def sum_to_n_with_recursion_and_memo(n: int, memo: dict = {}):
    """sum_to_n_with_recursion_and_memo is a function that sums numbers from 1 to n.
    >>> sum_to_n_with_recursion_and_memo(30)
    465
    >>> sum_to_n_with_recursion_and_memo(100)
    5050
    >>> sum_to_n_with_recursion_and_memo(5)
    15
    >>> sum_to_n_with_recursion_and_memo(10)
    55
    >>> sum_to_n_with_recursion_and_memo(1)
    1
    
	Include these tokens in the code: (
	Do not include these tokens in the code: sum ([ n for n in range
	"""

    if n == 1:
       
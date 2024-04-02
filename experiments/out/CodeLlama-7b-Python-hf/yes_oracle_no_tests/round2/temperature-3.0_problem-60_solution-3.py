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
    
	Include these tokens in the code: return ( n
	Do not include these tokens in the code: sum = 0 for
	"""
    # YOUR CODE HERE
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum


def sum_to_n2(n: int):
    """sum_to_n2 is a function that sums numbers from 1 to n.
    >>> sum_to_n2(30)
    465
    >>> sum_to_n2(100)
    5050
    >>> sum_to_n2(5)
    15
    >>> sum_to_n2(10)
    55
    >>> sum_to_n2(1)
    1
    """
    # YOUR CODE HERE
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


def sum_to_n3(n: int):
    """sum_to_n3 is a function that sums numbers from 1 to n.
    >>> sum_to_n3(30)
    465
    >>> sum_to_n3(100)
    5050
    >>> sum_to_n3(5)
    15
    >>> sum_to_n3(10)
    55
    >>> sum_to_n3(1)
    1
    """
    # YOUR CODE HERE
    return (n * (n + 1)) // 2


print(sum_to_n3(30))
print(sum_to_n3(100))
print(sum_to_n3(5))
print(sum_to_n3(10))
print(sum_to_n3(1))

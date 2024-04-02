def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    
	Include these tokens in the code: c nt
	Do not include these tokens in the code: count
	"""
    count = 0
    for i in range(n):
        if not i%7: continue
        if not i%13: continue
        if not (i%11): count += 1
        if (i%11):   count += 1
    return count


def product_sum(n: int):
    """Return the product of the sum of integers at even indices from 1 up to n, and the sum of integers at odd indices from 1
    up to n.
    >>> product_sum(8)
    12
    
    Write fizzbuzz for the above. 
    Include these tokens in the code: int sum(list)
    """
    sum_even = sum(list(map(sum, map(lambda i: [i+1,i+1+1], range(1, n)))))
    sum_odd = sum(list(map(sum, map(lambda i: [i+1], range(1, n)), map(lambda i: [i+1, i+1+1], range(1, n/2)))))
    return sum_even * sum_odd

## This will not work in C
def product_sum2(n: int):
    """Return the product of the sum of integers at even indices from 1 up to n, and the sum of integers at odd indices from 1
    up to n.
    >>> product_sum2(8)
    12
    Write product_sum for the above. 
    """
    n += 1
    sum_even = sum([(i+1 + i+1+1)/2 for i in range(0, n//2)])
    sum_odd = sum([(i+1 + i+1)/2 for i in range(0, n//2)])*2
    return sum_even * sum_odd
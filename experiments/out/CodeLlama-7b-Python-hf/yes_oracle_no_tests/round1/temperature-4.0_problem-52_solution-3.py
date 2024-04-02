def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    
	Include these tokens in the code: return all ( x < t
	"""

    for i in l:
        if i >= t:
            return False
    return True


def sum_multiples(n: int, low: int, high: int):
    """Return the sum of all integers from low to high that are
    multiples of n.
    >>> sum_multiples(3, 2, 5)
    3
    >>> sum_multiples(5, 2, 5)
    0
    >>> sum_multiples(0, 2, 5)
    0
    >>> sum_multiples(3, 2, 4)
    3
    """
    sum = 0
    for i in range(low, high + 1):
        if i % n == 0:
            sum += i
    return sum


def make_pizza(size: int, *toppings: str):
    """Summarize the pizza we are about to make."""
    print("Making a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


def remainders(m: int, *dividends: int):
    """Print the remainders when the dividends are divided by m.
    >>> remainders(10, 7, 9, 5)
    1
    4
    4
    5
    """
    for dividend in dividends:
        print(dividend % m)


def count_cousins(n: int, p: int, *siblings: int):
    """Print the number of siblings of a node that have the same value
    as the node and are one step away.
    >>> count_cousins(3, 1, 2, 1, 1, 3, 1)
    2
    >>> count_cousins(4, 2, 1, 2, 3, 2, 3, 2, 4, 2, 1, 2, 3, 2, 3, 2, 4)
    4
    """
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for elem in l:
        if elem >= t:
            return False
    return True


def odd_numbers(n: int):
    """Return a list of odd numbers from 1 to n."""
    "*** YOUR CODE HERE ***"
    odd_list = []
    for num in range(1, n+1):
        if (num % 2 == 1):
            odd_list.append(num)
    return odd_list
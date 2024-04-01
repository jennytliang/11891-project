def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (0, 0)
    evens = 0
    odds = 0
    while num != 0:
        if num % 10 % 2 == 0:
            evens += 1
        else:
            odds += 1
        num = num // 10
    return evens, odds

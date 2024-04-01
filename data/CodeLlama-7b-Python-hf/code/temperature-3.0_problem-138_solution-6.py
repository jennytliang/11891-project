def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    total = 0
    list_even = []
    for number in range(1,n):
        if number % 2 == 0:
            total = total + number
            list_even.append(number)
    if total == n and len(list_even) == 4:
        return True
    else: 
        return False

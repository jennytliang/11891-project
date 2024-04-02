def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""
    # Start with 10^(n-1)
    # Iterate through 10^n to 9*10^n
    # Add 1 if number % 10 == 1
    # Add 1 if number // 10^n == 1
    # Add 1 if number % 10 == 9
    # Add 1 if number // 10^n == 9
    # Subtract 1 if number % 10 == 0
    # Subtract 1 if number // 10^n == 9
    # Subtract 1 if number % 10 == 8
    # Subtract 1 if number // 10^n == 8
    # Return count
    count = 0
    start = 10 ** (n - 1)
    end = 9 * 10 ** n
    for number in range(start, end + 1):
        if number % 10 == 1:
            count += 1
        if number // 10 ** n == 1:
            count += 1
        if number % 10 == 9:
            count += 1
        if number // 10 ** n == 9:
            count += 1
        if number % 10 == 0:
            count -= 1
        if number // 10 ** n == 9:
            count -= 1
        if number % 10 == 8:
            count -= 1
        if number // 10 ** n == 8:
            count -= 1
    return count


print(starts_one_ends(1))
print(starts_one_ends(2))
print(starts_one_ends(3))
print(starts_one_ends(4))
print(starts_one_ends(5))
print(starts_one_ends(6))

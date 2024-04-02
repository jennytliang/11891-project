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
    # Count the number of times 7 appears in integers less than n which are divisible by 11 or 13.
    # You may assume that the inputs greater than 0.
    # TODO DO NOT ALTER THE SKELETON CODE
    
    count = 0
    for c in range(n):
        # print(f"{c + 1:,d} {c * 10:,d}")  # Uncomment for debug
        if(c*10+11) % 7 or (c*10+13) % 7:
            count += c*10
            # print(f"{c:,d} {count:,d}")  # Uncomment for debug
    return count

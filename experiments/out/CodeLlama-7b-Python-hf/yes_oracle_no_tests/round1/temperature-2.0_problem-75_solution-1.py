def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: >
	"""

    # ====================================
    # Phase 1.
    # Re-arrange the condition
    # ====================================
    # a must be less than 100
    if a > 100:
        return False

    # ====================================
    # Phase 2.
    # Initialize the variables.
    # ====================================
    # Initialize a flag
    flag = False

    # Initialize a counter to keep track of the number of prime factors
    count = 0

    # ====================================
    # Phase 3.
    # Loop
    # ====================================
    # Loop until a is greater than 1
    while a > 1:
        # ====================================
        # Phase 4.
        # Check if a is prime.
        # ====================================
        # Loop through the numbers between 2 and a - 1.
        for i in range(2, a):
            # ====================================
            # Phase 5.
            # If the number is not prime,
            # ====================================
            if a % i == 0:
                # ====================================
                # Phase 6.
                # Set flag to false
                # ====================================
                flag = False

                # ====================================
                # Phase 7.
                # Break the inner loop
                # ====================================
                break

            # ====================================
            # Phase 8.
            # If the number is prime,
            # ====================================
            else:
                # ====================================
                # Phase 9.
                # Set flag to true
                # ====================================
                flag = True

        # ====================================
        # Phase 10.
        # If the flag is true,
        # ====================================
        if flag:
            # ====================================
            # Phase 11.
            # Increment the counter
            # ====================================
            count += 1

        # ====================================
        # Phase 12.
        # Set flag to false

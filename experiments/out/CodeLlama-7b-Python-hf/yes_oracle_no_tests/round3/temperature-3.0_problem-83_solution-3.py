def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    
	Include these tokens in the code: if n ==
	"""

    # Base case
    if n == 1:
        return 2

    # Setup
    count = 0

    # Iterate through all possible first digits
    for first_digit in range(1, 10):

        if first_digit == 1:
            # If the first digit is 1, the number starts with 1
            # so we add 1 to the count
            count += 1
            continue

        # If the first digit is not 1, the number does not start with 1
        # so we subtract 1 from the count
        count -= 1

        # Iterate through all possible second digits
        for second_digit in range(0, 10):
            if second_digit == 0:
                # If the second digit is 0, the number ends with 0
                # so we add 1 to the count
                count += 1
                continue

            # If the second digit is not 0, the number does not end with 0
            # so we subtract 1 from the count
            count -= 1

            # Iterate through all possible third digits
            for third_digit in range(0, 10):
                if third_digit == 0:
                    # If the third digit is 0, the number ends with 0
                    # so we add 1 to the count
                    count += 1
                    continue

                # If the third digit is not 0, the number does not end with 0
                # so we subtract 1 from the count
                count -= 1

                # Iterate through all possible fourth digits
                for fourth_digit in range(0, 10):
                    if fourth_digit == 0:
                        # If the fourth digit is 0, the number ends with 0
                        # so we add 1 to the count
                        count += 1
                        continue

                    # If the fourth digit is not 0, the number does not end with 0
                    # so we subtract 1 from the count
                    count -= 1

                    # Iterate through all possible fifth digits

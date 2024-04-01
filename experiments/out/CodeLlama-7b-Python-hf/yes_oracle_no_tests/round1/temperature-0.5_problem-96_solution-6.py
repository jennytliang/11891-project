def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code:  ans
	Do not include these tokens in the code: pr imes
	"""

    # 1. Set the initial answer
    ans = []

    # 2. Loop through all the integers
    for i in range(2, n):

        # 3. Check if each integer is prime
        prime = True
        for j in range(2, i):

            # 4. If any of the integers divide into the current integer, it is not prime
            if i % j == 0:
                prime = False

        # 5. If the integer is prime, add it to the answer
        if prime:
            ans.append(i)

    # 6. Return the answer
    return ans


def count_up_to_2(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code:  ans
	Do not include these tokens in the code: pr imes
	"""

    # 1. Set the initial answer
    ans = []

    # 2. Loop through all the integers
    for i in range(2, n):

        # 3. Check if each integer is prime
        prime = True
        for j in range(2, i):

            # 4. If any of the integers divide into the current integer, it is not prime
            if i % j == 0:
                prime = False

        # 5. If the integer is prime, add it to the answer
        if prime:
            ans.append(i)

    # 6. Return
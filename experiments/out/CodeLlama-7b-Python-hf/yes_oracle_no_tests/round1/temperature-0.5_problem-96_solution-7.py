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

    # create a list to store the prime numbers
    prime_list = []
    # create a list to store the numbers to check
    check_list = []

    # check if n is a prime number
    if n > 1:
        # add n to the check list
        check_list.append(n)

    # loop through the check list
    for num in check_list:
        # loop through the prime list
        for prime in prime_list:
            # check if the number can be divided by the prime number
            if num % prime == 0:
                # if it can be divided, break out of the loop
                break
        else:
            # if the number cannot be divided, add it to the prime list
            prime_list.append(num)

    # return the first n prime numbers
    return prime_list[:n]


# print(count_up_to(5))
# print(count_up_to(11))
# print(count_up_to(0))
# print(count_up_to(20))
# print(count_up_to(1))
# print(count_up_to(18))


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

    # create a list to store the prime numbers
    prime_list =
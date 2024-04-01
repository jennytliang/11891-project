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
    """
    prime_numbers = []

    for i in range(n):
        for j in range(i + 1):
            if i % j == 0:
                if j <= 1:
                    break
            if j == i:
                prime_numbers.append(j)

    print(prime_numbers)

    return prime_numbers


def count_up_to_with_filter(n):
    """Implement a function that takes an non-negative integer and returns an array of the
    first n integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    return list(filter(is_prime, range(n)))


def is_prime(number):
    """Check if a number is prime"""
    if number <= 1:
        return False
    elif number <= 3:
        return True

    for j in range(2, number):
        if number % j == 0:
            return False
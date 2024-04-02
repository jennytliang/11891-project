def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    
	Include these tokens in the code: return n **
	"""
    return n ** 2


# print(car_race_collision(10))

# def is_prime(n: int):
#     """
#     Given an integer n, return true if n is prime, otherwise return false.
#     """
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# print(is_prime(11))


def is_prime(n: int):
    """
    Given an integer n, return true if n is prime, otherwise return false.
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(11))


def is_prime(n: int):
    """
    Given an integer n, return true if n is prime, otherwise return false.
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(n: int):
    """
    Count the number of prime numbers up to and including n.
    """
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count


print(count_primes(10))


def is_palindrome(s: str):
    """
    Given a string, return true if the string is a palindrome, otherwise return false.
    """
    return s == s[::-1]


print(is_palindrome("racecar"))


def is_palindrome(s: str):
    """
    Given a string, return true if the string is a palindrome, otherwise return false.
    """
    return s == s[::-1]


def count_primes(n: int):
    """
    Count the number of prime numbers up to
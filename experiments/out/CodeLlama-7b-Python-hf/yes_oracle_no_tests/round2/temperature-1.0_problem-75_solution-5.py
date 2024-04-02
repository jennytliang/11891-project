def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: 1
	Do not include these tokens in the code: 0
	"""

    if 3 < a < 100:
        for i in range(2, a):
            if a % i == 0:
                for j in range(2, a):
                    if i % j == 0:
                        for k in range(2, a):
                            if j % k == 0:
                                return True
    return False


def is_multiply_prime_2(a):
    if 3 < a < 100:
        for i in range(2, a):
            for j in range(2, a):
                if i % j == 0:
                    for k in range(2, a):
                        if j % k == 0:
                            if i * j * k == a:
                                return True
    return False


print(is_multiply_prime(30))
print(is_multiply_prime_2(30))


# def is_multiply_prime(a):
#     if a < 3:
#         return False
#     for i in range(2, a):
#         if a % i == 0:
#             for j in range(2, a):
#                 if i % j == 0:
#                     for k in range(2, a):
#                         if j % k == 0:
#                             if i * j * k == a:
#                                 return True
#     return False
#
#
# print(is_multiply_prime(30))
# print(is_multiply_prime_2(30))

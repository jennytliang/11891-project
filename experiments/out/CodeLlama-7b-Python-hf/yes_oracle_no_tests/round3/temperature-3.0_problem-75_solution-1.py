def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: <=
	Do not include these tokens in the code: <
	"""

    # TODO: Write your solution here
    if a <= 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                return True
    return False


def main():
    print(is_multiply_prime(30))  # True
    print(is_multiply_prime(20))  # False
    print(is_multiply_prime(10))  # False
    print(is_multiply_prime(3))  # False
    print(is_multiply_prime(2))  # False
    print(is_multiply_prime(1))  # False


if __name__ == "__main__":
    main()

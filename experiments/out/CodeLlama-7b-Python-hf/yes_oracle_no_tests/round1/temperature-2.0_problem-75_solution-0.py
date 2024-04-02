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

    is_multiple = False
    for i in range(2, 100):
        if is_multiple:
            break
        for j in range(2, 100):
            if is_multiple:
                break
            for k in range(2, 100):
                if i * j * k == a:
                    is_multiple = True
                    break
    return is_multiple


def main():
    #   Test your code with this first
    #   Change the argument to try different values
    a = 30
    print("is_multiply_prime({}) == {}".format(a, is_multiply_prime(a)))

    #   Uncomment these to check your code
    #   Correct values should be true or false. Not 1 or 0
    a = 30
    print("is_multiply_prime({}) == {}".format(a, is_multiply_prime(a)))

    a = 20
    print("is_multiply_prime({}) == {}".format(a, is_multiply_prime(a)))

    a = 100
    print("is_multiply_prime({}) == {}".format(a, is_multiply_prime(a)))

    a = 1
    print("is_multiply_prime({}) == {}".format(a, is_multiply_prime(a)))

    a = 32
    print("is_multiply_prime({}) == {}".format(a, is_multiply_prime(a)))

    a = 35
    print("is_multiply_prime({}) == {}".format(a, is_multiply_prime(a)))


if __name__ == '__main__':
    main()
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        for i in range(2, a):
            if a % i == 0:
                return False
        return True
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_multiply_prime(30))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(15) == False
    assert is_multiply_prime(10) == False
    assert is_multiply_prime(91) == True
    assert is_multiply_prime(100) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

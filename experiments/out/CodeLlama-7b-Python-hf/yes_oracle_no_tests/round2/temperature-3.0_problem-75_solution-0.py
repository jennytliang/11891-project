def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Do not include these tokens in the code: 0 0
	"""

    if a <= 100:
        prime = [2, 3, 5, 7]
        for i in prime:
            if a % i == 0:
                a = a / i
                if a == 1:
                    return True
        return False
    else:
        return False


def test_function():
    assert is_multiply_prime(30) == True, "30 = 2 * 3 * 5"
    assert is_multiply_prime(15) == False, "15 is not multiply prime"
    assert is_multiply_prime(36) == False, "36 is not multiply prime"
    assert is_multiply_prime(45) == False, "45 is not multiply prime"
    assert is_multiply_prime(60) == True, "60 = 2 * 3 * 5"
    assert is_multiply_prime(75) == False, "75 is not multiply prime"
    assert is_multiply_prime(90) == True, "90 = 2 * 3 * 5"
    assert is_multiply_prime(100) == False, "100 is not multiply prime"
    assert is_multiply_prime(300) == False, "300 is not multiply prime"
    assert is_multiply_prime(0) == False, "0 is not multiply prime"
    assert is_multiply_prime(1) == False, "1 is not multiply prime"
    print("Congratulations! All tests passed!")


def main():
    test_function()


if __name__ == '__main__':
    main()

def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        for i in range(2, 100):
            for j in range(2, 100):
                for k in range(2, 100):
                    if i * j * k == a:
                        return True
        return False
    else:
        return False

if __name__ == "__main__":
    print(is_multiply_prime(30))
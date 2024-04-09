def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    
	Include these tokens in the code: if a <=
	"""
    # 1. find the numbers of prime numbers in the prime factorization of a
    # 2. check if the number of prime numbers is equal to 3
    # 3. return the result
    prime_nums = []
    for i in range(2, a):
        if a % i == 0:
            prime_nums.append(i)
    return len(prime_nums) == 3


if __name__ == '__main__':
    print(is_multiply_prime(30))

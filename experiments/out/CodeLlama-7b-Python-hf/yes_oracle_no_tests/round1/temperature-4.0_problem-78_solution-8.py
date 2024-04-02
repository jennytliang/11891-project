def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
    For num = "AB" the output should be 1.
    For num = "1077E" the output should be 2.
    For num = "ABED1A33" the output should be 4.
    For num = "123456789ABCDEF0" the output should be 6.
    For num = "2020" the output should be 2.
    
	Do not include these tokens in the code: hex a = num . upper ()
	"""
    def is_prime(num):
        """Check if given number is a prime number.
        
        Args:
            num: integer
            
        Returns:
            True if number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    if not num:
        return 0

    # convert hexadecimal to decimal
    dec = int(num, 16)

    # count all primes in a given decimal number
    count = 0
    while dec > 0:
        last_digit = dec % 10
        if is_prime(last_digit):
            count += 1
        dec //= 10

    return count

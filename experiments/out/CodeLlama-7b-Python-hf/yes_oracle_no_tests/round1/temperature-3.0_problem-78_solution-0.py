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
    
	Include these tokens in the code: return len ( list ( filter ( lambda x :
	Do not include these tokens in the code: digits =
	"""
    # your code here
    from math import sqrt
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def check_hex(num):
        if not num:
            return 0
        hex_list = list(num)
        count = 0
        for i in hex_list:
            if i in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "B", "D"]:
                if is_prime(int(i, 16)):
                    count += 1
        return count

    return check_hex(num)


print(hex_key("AB"))
print(hex_key("1077E"))
print(hex_key("ABED1A33"))
print(hex_key("123456789ABCDEF0"))
print(hex_key("2020"))

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
	"""
	
	# your code here
    # 1. hex_to_dec (num)
    # 2. prime_check (num)
    # 3. prime_check_list (num)
    # 4. len (prime_check_list (num))
    # 5. return (len (prime_check_list (num)))
    
    # 1. hex_to_dec (num)
    def hex_to_dec(num):
        # 1. Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
        hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        # 2. Create a dictionary
        hex_dict = dict(zip(hex_list, range(0, 16)))
        # 3. Create an empty string
        dec_string = ''
        # 4. For each character in num, append the corresponding decimal value to dec_string
        for i in num:
            dec_string += str(hex_dict[i])
        # 5. Convert dec_string to an integer
        dec_num = int(dec_string)
        return dec_num
    
    # 2. prime_check (num)
    def prime_check(num):
        # 1. Create a list of prime numbers between 0 and 100
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # 2. If num is in prime_list, return True

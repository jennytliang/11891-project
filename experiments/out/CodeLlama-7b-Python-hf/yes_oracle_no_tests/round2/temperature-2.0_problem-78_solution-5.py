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
    
	Include these tokens in the code: return len ( list ( filter ( lambda x
	Do not include these tokens in the code: result = 0 for
	"""
    hexdigits = '0123456789ABCDEF'
    hex_dict = {i: hexdigits.index(i) for i in hexdigits}
    hex_primes = [2, 3, 5, 7, 11, 13]
    hex_primes_dict = {i: hex_primes.index(i) for i in hex_primes}
    num_str = ''.join([str(hex_dict[i]) for i in num])
    num_int = int(num_str, 16)
    num_list = list(str(num_int))
    num_list_int = [int(i) for i in num_list]
    num_list_primes = list(filter(lambda x: hex_primes_dict[x] >= 0, num_list_int))
    return len(num_list_primes)


print(hex_key("AB"))
print(hex_key("1077E"))
print(hex_key("ABED1A33"))
print(hex_key("123456789ABCDEF0"))
print(hex_key("2020"))

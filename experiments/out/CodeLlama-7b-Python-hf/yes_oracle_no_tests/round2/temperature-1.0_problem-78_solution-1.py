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
    
	Do not include these tokens in the code: # 1 ) convert hex ade
	"""
    # #1) convert hexadecimal to decimal
    # number = 0
    # for i in num:
    #     if i == "A":
    #         number += 10
    #     elif i == "B":
    #         number += 11
    #     elif i == "C":
    #         number += 12
    #     elif i == "D":
    #         number += 13
    #     elif i == "E":
    #         number += 14
    #     elif i == "F":
    #         number += 15
    #     else:
    #         number += int(i)
    # print(number)
    # #2) count the number of prime number
    # prime_number = 0
    # for i in range(2, number+1):
    #     for j in range(2, i):
    #         if i % j == 0:
    #             break
    #     else:
    #         prime_number += 1
    # print(prime_number)
    
    # #3) return the number of prime number
    # return prime_number
    
    # #4) return the number of prime number
    # #4)
    # prime_number_hex = 0
    # for i in num:
    #     if i == "A":
    #         prime_number_hex += 1
    #     elif i == "B":
    #         prime_number_hex += 1
    #     elif i == "C":
    #         prime_number_hex += 1
    #     elif i == "D":
    #         prime_number_hex += 1
    #     elif i == "E":
    #         prime_number_hex += 1
    #     elif i == "F":
    #         prime_number_hex += 1
    #     else:
    #         prime_number_hex += int(i)
    # return prime_number_hex
    # #5)
    # prime_number_hex = 0
    # for i in num:
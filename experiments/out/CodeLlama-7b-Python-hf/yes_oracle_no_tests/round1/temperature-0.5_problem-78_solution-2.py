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
    
	Include these tokens in the code:   return len
	Do not include these tokens in the code: hex _ dict = { " 0
	"""

    # a list of all prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    # a list of all hexadecimal digits
    hexdigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    # a dictionary to help us map the hexadecimal digits to the primes
    hex_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 11,
        "B": 13,
        "C": 17,
        "D": 19,
        "E": 23,
        "F": 29
    }

    # a list to store the hexadecimal digits in
    hex_num_list = []

    # loop through the string
    for i in range(len(num)):
        # if the string is in the hexadecimal digits
        if num[i] in hexdigits:
            # add the hexadecimal digit to the list
            hex_num_list.append(num[i])
        # else do nothing
        else:
            pass

    # a list to store the primes in
    primes_list = []

    # loop through the hexadecimal digits
    for i in range(len(hex_num_list)):
        # if the hex
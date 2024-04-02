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
	Do not include these tokens in the code: hex _ dict = {
	"""
    hexadecimals = "0123456789ABCDEF"
    hex_dict = {
        "2":2,#"0",
        "3":3,#"1",
        "5":5,#"2",
        "7":7,#"3",
    }
    hexs = num
    hex_keys = [k for k in hex_dict if k in hexs]
    hex_values = sum(hex_dict.values())

    if not hexadecimals:
        return 1 + len(hex_keys)   
    elif hexadecimals.isdigit():
        return 2 + len(hex_keys)
    return hex_values


def hex_key2(num):
    hexadecimals = {
        "2":2,#"0",
        "3":3,#"1",
        "5":5,#"2",
        "7":7,#"3",
    }
    hexs = num
    #hex_keys = [k for k in hex_dict if k in hexs]


    
    
    if not hexs:
        return 1 + len(hex_keys)   
    elif hexs.isdigit():
        return 2 + len(hex_keys)
    return hex_values


def hex_key3(num):
    hexadecimals = {hex(i):i-1 for i in range(17)}
    hex_keys = [k for k in hexadecimals if k in num]
    return len(hex_keys)



if __name__ == '__main__':
    hex_keys = [2,"2","2","02","02"]
    print(hex_key3(hex_keys))

    hex_keys = ["AB","20", "0","3", "21","22","2","23","2","AA" ]
    print(hex_key3(hex_keys))
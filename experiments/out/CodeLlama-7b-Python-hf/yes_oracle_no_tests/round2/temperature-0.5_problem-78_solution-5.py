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
    # your code goes here
    hex_list = list(num)
    hex_list = [int(i, 16) for i in hex_list]
    hex_list = [i for i in hex_list if i not in [10, 11, 12, 13, 14, 15]]
    hex_list = [i for i in hex_list if i in [2, 3, 5, 7, 11, 13]]
    return len(hex_list)


def hex_key_solution(num):
    """This solution is based on the fact that the hexadecimal digits
    are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    """
    return sum(x in [2, 3, 5, 7, 11, 13] for x in [int(num[i:i + 1], 16) for i in range(len(num)) if num[i:i + 1] in "0123456789ABCDEF"])


if __name__ == '__main__':
    print("Example:")
    print(hex_key('AB'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert hex_key('AB') == 1
    assert hex_key('1077E') == 2
    assert hex_key('ABED1A33') == 4
    assert hex_key('123456789ABCDEF0') == 6
    assert hex_key('2020') == 2
    print("C
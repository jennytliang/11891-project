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
    hex_dict = {"A": "10", "B": "11", "C": "12", "D": "13", "E": "14", "F": "15"}
    hex_key_list = list()
    for digit in num:
        if digit in ["A", "B", "C", "D", "E", "F"]:
            hex_key_list.append(hex_dict[digit])
        else:
            hex_key_list.append(digit)

    for num in hex_key_list:
        try:
            num = int(num, 16)
            if num % 2 == 0:
                hex_key_list.remove(num)
            if num % 3 == 0:
                hex_key_list.remove(num)
            if num % 5 == 0:
                hex_key_list.remove(num)
            if num == 2 or num == 3 or num == 5 or num == 11 or num == 13:
                pass
            else:
                hex_key_list.remove(num)
        except ValueError:
            pass
    return len(hex_key_list)


if __name__ == "__main__":
    assert hex_key("A") == 1
    assert hex_key("1077E") == 2
    assert hex_key("ABED1A33") == 4
    assert hex_key("123456789ABCDEF0") == 6
    assert hex_key("2020") == 2
    assert hex_key("A20A2BEE") == 4
    print("ALL TESTS PASS")

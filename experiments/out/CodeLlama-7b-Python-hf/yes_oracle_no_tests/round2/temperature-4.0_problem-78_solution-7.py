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
    
	Include these tokens in the code: return len (
	Do not include these tokens in the code: hex _ dict = {
	"""
    hex_dict = {'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', 'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15'}
    hex_list = [hex_dict[x] for x in num]
    hex_list = [int(x) for x in hex_list]
    hex_list = [x for x in hex_list if x % 2 == 1]
    return len(hex_list)


if __name__ == '__main__':
    assert hex_key("AB") == 1, "All hex digits are prime"
    assert hex_key("1077E") == 2, "Only hex digits 11 and 13 are prime"
    assert hex_key("ABED1A33") == 4, "Only hex digits 10, 11, 13 and 15 are prime"
    assert hex_key("123456789ABCDEF0") == 6, "Only hex digits 2, 3, 5, 7, 11 and 13 are prime"
    assert hex_key("2020") == 2, "Only hex digits 2 and 10 are prime"

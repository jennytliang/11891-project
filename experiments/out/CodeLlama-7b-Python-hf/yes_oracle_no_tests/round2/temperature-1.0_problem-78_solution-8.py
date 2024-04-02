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
    
	Include these tokens in the code: len ( list ( filter ( lambda x : x
	Do not include these tokens in the code: hex _ dict [ num [ 0 ]] + hex
	"""

    r=[2,3,5,7,'B','D']
    s=num[0:3]
    if s=='B0B' or s=='B1B' or s=='B2B' or s=='B3B' or s=='B4B' or s=='B5B':
        return 2
    elif s=='B6B' or s=='B7B' or s=='B8B' or s=='B9B' or s=='BAA' or s=='BBB':
        return 3
    elif s=='BDBC' or s=='BDEF' or s=='CDEF' or s=='DDEF' or s=='EFFF' or s=='FFFF':
        return 4
    elif s=='1000' or s=='1001' or s=='1010' or s=='1011' or s=='1100' or s=='1111':
        return 5
    elif s=='2020' or s=='3030' or s=='4040' or s=='5050' or s=='6060' or s=='7070':
        return 6
    elif s=='8080' or s=='9090' or s=='A0A0' or s=='B0B0' or s=='C0C0' or s=='D0D0':
        return 7
    else:
        return 8

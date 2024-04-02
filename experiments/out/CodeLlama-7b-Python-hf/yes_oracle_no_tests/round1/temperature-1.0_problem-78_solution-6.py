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

# solution with string comprehension
    return len(
        [c for c in num if c in "AB2357BDEF"]
    )


def hex_key_sol2(num):
    """
        The code below uses filter() and map() to determine if each character
        exists in the hex keys list [2, 3, 5, 7, B (=11), D (=13)].
        The lambda returns False if there is an entry, otherwise True
        Note that it is wrapped in list() which we need because filter()
            returns an iterator that we can't call the len function on
        So we just call list() to force evaluation
    """
    hex_keys = [2, 3, 5, 7, 11, 13]
    return len(
        list(  # needed because filter() returns an iterator
            filter(
                lambda x: x not in hex_keys,
                map(
                    lambda x: int(x, 16),
                    num,
                ),
            )
        )
    )


assert hex_key("AB") == 1, "A and B are primes"
assert hex_key("ABED1A33") == 4, "A, B, E, D are prime"
assert hex_key("1077E") == 2, "10, 77, E are prime"
assert hex_key("2020") == 2, "20, 20 are prime"
assert hex_key("123456789ABCDEF0") == 6, "0, A, B, E, F are prime"

assert hex_key_sol2("AB") == 1, "A and B are primes"
assert hex_key_sol2("ABED1A33") == 4, "A, B, E, D are prime"
assert hex_key_sol2("1077E") == 2, "10, 77, E are prime"
assert hex_key_sol2("2020") == 2, "20, 
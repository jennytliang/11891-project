def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: def is _ prime ( a ):
	"""
    # Prime numbers are divisible by 1 and themselves.
    # If string is divisible by any number other than 1 and itself, it is not prime.
    # If string is not divisible by any number other than 1 and itself, it is prime.
    # 1. Convert string to int
    # 2. Check if string is divisible by 1 and itself
    # 3. If string is divisible by any number other than 1 and itself, return False
    # 4. If string is not divisible by any number other than 1 and itself, return True
    # 5. Return the result

    if isinstance(string, str):
        string = int(string)

    if string == 1:
        return False
    if string == 2:
        return True
    if string % 1 != 0:
        return False
    if string % 2 != 0:
        return False

    for i in range(3, string, 2):
        if string % i == 0:
            return False

    return True


# Tests
def test_prime_length():
    assert prime_length('Hello') == True
    assert prime_length('abcdcba') == True
    assert prime_length('kittens') == True
    assert prime_length('orange') == False
    assert prime_length('2') == True
    assert prime_length('11') == True
    assert prime_length('15') == True
    assert prime_length('21') == False
    assert prime_length('24') == False
    assert prime_length('29') == True
    assert prime_length('32') == False
    assert prime_length('39') == True
    assert prime_length('43') == False
    assert prime_length('51') == True
    assert prime_length('55') == True
    assert prime_length('59') == False
    assert prime_length('64') == False
    assert prime_length('69') == True
    assert prime_length('72') == False
    assert prime_length('
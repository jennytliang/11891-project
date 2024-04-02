def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    
	Include these tokens in the code: a
	Do not include these tokens in the code: num
	"""

    def is_p(number):
        if number == 2:
            return True
        elif number == 3:
            return True
        elif number == 5:
            return True
        elif number == 7:
            return True
        elif number % 2 == 0:
            return False
        elif number % 3 == 0:
            return False
        elif number % 5 == 0:
            return False
        elif number % 7 == 0:
            return False
        else:
            return True

    return is_p(len(string))


def test_prime_length():
    assert prime_length('Hello') == True
    assert prime_length('abcdcba') == True
    assert prime_length('kittens') == True
    assert prime_length('orange') == False


if __name__ == '__main__':
    test_prime_length()

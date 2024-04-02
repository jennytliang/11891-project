def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Include these tokens in the code: return int
	Do not include these tokens in the code: if not any ([ type
	"""
    return (a%10)*(b%10)

def count_letters(string):
    """Complete the function that counts the number of letters 
    (upper or lower case) in a string.
    Assume the input is always valid.
    Examples:
    count_letters("The quick brown fox jumps over the lazy dog.") 
    should return 31.
    count_letters("The time you enjoy wasting is not wasted time.") 
    should return 40.
    count_letters("") should return 0.
    
	Include these tokens in the code: return int
	Do not include these tokens in the code: if not any ([ type
	"""
    return len(string.replace(" ", "").replace("\n", ""))

def sum_digits(number):
    """Complete the function that takes a number as input and 
    returns the sum of the absolute value of each of the number's 
    digits.
    Assume the input is always valid.
    Examples:
    sum_digits(10) should return 1.
    sum_digits(121) should return 4.
    sum_digits(123) should return 6.
    sum_digits(0) should return 0.
    sum_digits(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
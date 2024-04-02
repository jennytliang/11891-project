def words_string(s):
    """
    You will be given a string of words separated by commas or spaces. Your task is
    to split the string into words and return an array of the words.
    
    For example:
    words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    
	Include these tokens in the code: words = ( s
	Do not include these tokens in the code: return
	"""
    words = s.split(", ")
    return words


def sum_all(list_of_num):
    """
    You will be provided with an array of numbers.
    Your task is to sum all the array elements and return the sum.
    
    Examples:
    sum_all([1, 3, 5]) == 9
    sum_all([-1, 0, 4, 5]) == 9
    sum_all([1, 2, 5, 6, 7, 8, 9]) == 45
    sum_all([-1, -2, 0, 1, 9]) == 8
    
	Include these tokens in the code: sum_number = ( list_of_num
	Do not include these tokens in the code: return 
	"""
    sum_number = sum(list_of_num)
    return sum_number
    
def extract_prices(string_of_price):
    """
    You will be given a string with prices for a number of products separated by commas and spaces. 
    Your task is to extract the prices from the string and return the sum of all the price numbers in the array.
    
    Examples:
    extract_prices("apples 2, bananas 4, oranges 3") # returns 9
    extract_prices("apples 3, bananas 5, oranges 4, bats 7") # returns 21
    extract_prices("apples 15, bananas 13") # returns 28
    
	Include these tokens in the code: prices = ( data
	Do not include these tokens in the code: return
	"""
    pr_no = [int(x) for x in string_of_price.split() if x.isdigit()]
    prices = sum(pr_no)
    return prices


def find_odd(lst):
    """
    You will be provided with a list of integers.
    You have to figure out whether is there any odd number or not.
    If there is any, you have to return the first odd number.
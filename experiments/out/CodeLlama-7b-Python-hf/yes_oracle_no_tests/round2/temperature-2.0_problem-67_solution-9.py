def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    
	Include these tokens in the code: words = s . split (" ")
	"""
    words = s.split(" ")
    apples = int(words[0])
    oranges = int(words[2])
    return n - apples - oranges


def sum_numbers(s):
    """
    In this task, you are given a string that represents a number. 
    You should be able to sum up the digits of the number and 
    return them as a string. If the number is less than 10, 
    you must return "0".
    For example:
    sum_numbers("12345") -> "15"
    sum_numbers("9") -> "9"
    sum_numbers("34259") -> "33"
    sum_numbers("10") -> "0"
    sum_numbers("121") -> "3"
    
    """
    if s == "0":
        return "0"
    else:
        return str(sum([int(i) for i in s]))


def string_splosion(s):
    """
    In this task, you will be given a string s. 
    You should return a new string created by merging each 
    character (even s) together. For example:
    string_splosion("Code") -> "CCoCodCode"
    string_splosion("abc") -> "aababc"
    string_splosion("ab") -> "aab"
    
    """
    return "".join([i * len(s) for i in s])


def array_diff(input_array, num):
    """
    In this task, you will be given an array and a single number. 
    You should create a new array that contains each number of the 
    original array except the num. The numbers in the new array 
    should be in the same order as they were in the original array.
    For example:
    array_diff([1,2,2,2,3], 2) #  [1,3]
    array_diff([4,4,4,5,4], 4) #  [5]
    array_diff([
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
    
	Include these tokens in the code:  words = s . split (" ")
	Do not include these tokens in the code: # your code here app les
	"""

    words = s.split(" ")
    apples = int(words[0])
    oranges = int(words[2])
    return n - apples - oranges


def sum_of_numbers(s):
    """
    In this task, you are given a string s that only has either numbers or the plus operator '+'. 
    You have to return the sum of the numbers in the string.
    for examble:
    sum_of_numbers("123+456") -> 123 + 456 = 579
    sum_of_numbers("10000000000") -> 10000000000
    sum_of_numbers("+100") -> 100
    sum_of_numbers("1000+100") -> 1100
    sum_of_numbers("+1000+100+5000") -> 6000
    sum_of_numbers("+101000+100+5000") -> 111100
    """
    return sum([int(i) for i in s.split("+")])


def sum_of_numbers2(s):
    """
    In this task, you are given a string s that only has either numbers or the plus operator '+'. 
    You have to return the sum of the numbers in the string.
    for examble:
    sum_of_numbers2("123+456") -> 123 + 456 = 579
    sum_of_numbers2("10000000000") -> 10000000000
    sum_of_numbers2("+100") -> 100
    sum_of_numbers2("1000+100") -> 1100
    sum_of_numbers2("+1000+100+5000") -> 6000
    sum_of_numbers2("
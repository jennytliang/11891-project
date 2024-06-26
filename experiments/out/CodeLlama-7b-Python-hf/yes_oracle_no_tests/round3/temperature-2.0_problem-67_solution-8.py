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
    
	Do not include these tokens in the code: # code
	"""
    #code
    apples=int(s.split()[0])
    oranges=int(s.split()[2])
    return n-apples-oranges


if __name__ == '__main__':
    print("Example:")
    print(fruit_distribution("5 apples and 6 oranges", 19))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8, "Apples"
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2, "Oranges"
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95, "Both"
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19, "All"
    print("Coding complete? Click 'Check' to earn cool rewards!")
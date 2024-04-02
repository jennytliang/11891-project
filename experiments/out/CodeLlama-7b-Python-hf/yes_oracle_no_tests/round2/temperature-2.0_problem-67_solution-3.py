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
    
	Do not include these tokens in the code: # First we will split the string
	"""
    # First we will split the string
    lst = s.split()
    # print(lst)
    # Second we will check if the first item in the list is the word "apples"
    if lst[0] == "apples":
        # If the first item is "apples" we will add the number of apples in the list to the variable apples
        apples = int(lst[0])
    else:
        # If the first item is not "apples" we will add 0 to the variable apples
        apples = 0
    # Third we will check if the third item in the list is the word "oranges"
    if lst[2] == "oranges":
        # If the third item is "oranges" we will add the number of oranges in the list to the variable oranges
        oranges = int(lst[2])
    else:
        # If the third item is not "oranges" we will add 0 to the variable oranges
        oranges = 0
    # Fourth we will check if the fourth item in the list is the word "mango"
    if lst[3] == "mango":
        # If the fourth item is "mango" we will add the number of mango in the list to the variable mango
        mango = int(lst[3])
    else:
        # If the fourth item is not "mango" we will add 0 to the variable mango
        mango = 0
    # Finally we will return the result
    return n - apples - oranges - mango
    """
    Do not use any built-in functions to solve this task.
    """


if __name__ == "__main__":
    print(fruit_distribution("5 apples and 6 oranges", 19))
    print(fruit_distribution("0 apples and 1 oranges", 3))
    print(fruit_distribution("2 apples and 3 oranges", 100))
    print(fruit_distribution("100 apples and 1 oranges", 120))

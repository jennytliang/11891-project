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
    
	Include these tokens in the code: words
	Do not include these tokens in the code: tokens
	"""
    #take n value
    w = int(n)
        
    #split the sentences by words and calculate the tokens in them
    s = s.split(" ")
    
    #store tokens
    tokens = []
    for t in s:
        if t.isnumeric():
            tokens.append(t)
    print(tokens)
    
    #count fruits
    counter = 0
    for x in tokens:
        counter += int(x)
    print(counter)

    #calculate for mango
    a = w - counter
    print(a)
    
    return a


if __name__ == '__main__':
    s = input("Insert the fruits distribution: ")
    n = input("Insert number of total fruits: ")
    fruit_distribution(s, n)

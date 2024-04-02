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
    
	Include these tokens in the code: c 1 , c 2
	Do not include these tokens in the code: a
	"""

    words = s.split(" ")[0]
    fruits = s.split(" ")
    if ("apples","c","1") in fruits:
        apples_count = int(fruits[1])
        oranges_count = int(fruits[fruits.index("c") + 2])
        
        return n - apples_count - oranges_count

    apples_count = s.split(" ")[0]
    oranges_count = s.split(" ")[s.split(" ").index("and") + 1]
    return int(n) - int(apples_count) - int(oranges_count)

if __name__ == "__main__":
    print(fruit_distribution("5 apples and 6 oranges", 19))
    print(fruit_distribution("6 apples and 7 oranges", 19))
    print(fruit_distribution("1 oranges and 1 apples", 15))
    print(fruit_distribution("2 oranges and 4 apples", 9))
    print(fruit_distribution("4 apples and 3 oranges", 13))
    print(fruit_distribution("6 oranges and 2 apples", 11))
    print(fruit_distribution("1 oranges and 5 apples", 8))
    print(fruit_distribution("3 apples and 9 oranges", 4))
    print(fruit_distribution("3 apples and 6 oranges", 18))
    print(fruit_distribution("none", 0))
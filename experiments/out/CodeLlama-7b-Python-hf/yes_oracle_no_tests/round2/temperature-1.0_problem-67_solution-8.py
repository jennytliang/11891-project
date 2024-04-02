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
	Do not include these tokens in the code: app les , or anges
	"""

def fruit_distribution(s,n):
    s = s.split("and")
    s = [x.strip() for x in s]
    mango = n-sum(int(x[0]) for x in s)
    
                            #if x[0] == 5: return int(x[x.startswith("")])
                            #print(sum((x == 5)))
                            #print(x)
                            #return n - x[0]
    
    return mango

print(fruit_distribution("5 apples and 6 oranges", 19)) 
print(fruit_distribution("0 apples and 1 oranges", 3)) 
print(fruit_distribution("2 apples and 3 oranges", 100)) 
print(fruit_distribution("100 apples and 1 oranges", 120)) 

#-------------------------------------------------------------------------------------------------

    # def fruit_distribution(s,n):
    #     l = s.split()
    #     mangoes = int(l[4]) - (int(l[0]) + int(l[2]))
    #     return mangoes

    # print(fruit_distribution("5 apples and 6 oranges", 19)) 
    # print(fruit_distribution("0 apples and 1 oranges", 3)) 
    # print(fruit_distribution("2 apples and 3 oranges", 100)) 
    # print(fruit_distribution("100 apples and 1 oranges", 120)) 

#-------------------------------------------------------------------------------------------------
    
    # def fruit_distribution(s,n):
    #     l = s.split()
    #     l = [x.strip() for x in l]
    #     return n-(int(l[0])+int(l[2]))

    # print(fruit_distribution("5 apples and 6 oranges", 19)) 
    # print(fruit_distribution("0 apples and 1 oranges", 3)) 
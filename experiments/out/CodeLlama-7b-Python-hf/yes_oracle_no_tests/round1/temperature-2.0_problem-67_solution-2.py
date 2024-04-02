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
	Do not include these tokens in the code: app les
	"""
    # 1st solution
    # apples_count = int(s.split()[0])
    # oranges_count = int(s.split()[2])
    # return n - apples_count - oranges_count

    # 2nd solution
    apples_count, oranges_count = 0, 0
    for i in s.split():
        if i.isdigit():
            if i.endswith('apples'):
                apples_count = int(i)
            elif i.endswith('oranges'):
                oranges_count = int(i)
    return n - apples_count - oranges_count
    
    # 3rd solution
    # apples_count, oranges_count = 0, 0
    # for i in s.split():
    #     if i.isdigit():
    #         if i.endswith('apples'):
    #             apples_count = int(i)
    #         elif i.endswith('oranges'):
    #             oranges_count = int(i)
    # return n - apples_count - oranges_count
    
    # 4th solution
    # apples_count, oranges_count = 0, 0
    # for i in s.split():
    #     if i.isdigit():
    #         if i.endswith('apples'):
    #             apples_count = int(i)
    #         elif i.endswith('oranges'):
    #             oranges_count = int(i)
    # return n - apples_count - oranges_count
    
    # 5th solution
    # apples_count, oranges_count = 0, 0
    # for i in s.split():
    #     if i.isdigit():
    #         if i.endswith('apples'):
    #             apples_count = int(i)
    #         elif i.endswith('oranges'):
    #             oranges_count = int(i)
    # return n - apples_count - oranges_count
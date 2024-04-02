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
	Do not include these tokens in the code: app les
	"""

    words = s.split(" ")[1]
    words = words.split(" and ")
    apples = int(words[0].replace("apples", ""))
    oranges = int(words[1].replace("oranges", ""))
    return n - apples - oranges



def number_of_apples_and_oranges(s, a, b, x, y):
    """
    In this task, you will be given two integers a and b and two arrays of integers apples and oranges. 
    You have to figure out the total number of apples and oranges that land on Treesu.
    The apples and oranges will be scattered in the forest. The apple and orange trees are 
    located at index a and b in the array trees, respectively.
    
    For example:
    number_of_apples_and_oranges(7, 1, [-2, 2, 1], [5,-6,3,4,0], 1, 2) -> 1
    number_of_apples_and_oranges(11, 5, [2, 1, 0, -1, -2, 2, 2, -1], [5, 3, 4, 0, -2, -3, 1, -2], 1, 3) -> 2
    number_of_apples_and_oranges(9, 0, [-1, 2, 1, -3], [5, 3, 4, 0], 1, 2) -> 0
    number_of_apples_and_oranges(10, 0, [-1, -2, 1, 2, 3, -1, 2, -1, 3, 2], [5, 4, 4, 0, -2, -3, 1, -2, 3, -2], 1, 3) -> 4
    number_of_apples_and_oranges(10, 0, [-1, -2, 1, 2, 3, -1, 2, -1, 3, 2], [
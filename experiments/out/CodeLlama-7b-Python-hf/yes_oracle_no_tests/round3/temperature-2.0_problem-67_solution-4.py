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
	Do not include these tokens in the code: # code goes here #
	"""
    #code goes here
    #split string into list of words
    word_list = s.split()
    #find index of word 'apples'
    index_of_apples = word_list.index('apples')
    #find index of word 'oranges'
    index_of_oranges = word_list.index('oranges')
    #find index of word 'and'
    index_of_and = word_list.index('and')
    #find index of word 'mango'
    index_of_mango = word_list.index('mango')
    #find the total number of apples
    apples = int(word_list[index_of_apples-1])
    #find the total number of oranges
    oranges = int(word_list[index_of_oranges-1])
    #find the total number of mango
    mango = int(word_list[index_of_mango-1])
    #find the total number of fruits
    total = apples + oranges + mango
    #find the total number of fruits
    fruits = total - apples - oranges
    return n - total + fruits


if __name__ == '__main__':
    print("Example:")
    print(fruit_distribution("5 apples and 6 oranges", 19))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert fruit_distribution("5 apples and 6 oranges", 19) == 8
    assert fruit_distribution("0 apples and 1 oranges", 3) == 2
    assert fruit_distribution("2 apples and 3 oranges", 100) == 95
    assert fruit_distribution("100 apples and 1 oranges", 120) == 19
    print("Coding complete? Click 'Check' to earn cool rewards!")
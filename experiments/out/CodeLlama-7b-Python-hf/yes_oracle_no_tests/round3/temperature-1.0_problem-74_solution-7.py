def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    
	Include these tokens in the code: c
	Do not include these tokens in the code: # total _ match :: [
	'''
    # 1st solution
    # def total_match(lst1, lst2):
    #     lst1_sum = 0
    #     lst2_sum = 0
    #     for i in lst1:
    #         lst1_sum += len(i)
    #     for i in lst2:
    #         lst2_sum += len(i)
    #     if lst1_sum == lst2_sum:
    #         return lst1
    #     elif lst1_sum < lst2_sum:
    #         return lst1
    #     else:
    #         return lst2
    
    # 2nd solution
    # def total_match(lst1, lst2):
    #     lst1_sum = sum([len(i) for i in lst1])
    #     lst2_sum = sum([len(i) for i in lst2])
    #     if lst1_sum == lst2_sum:
    #         return lst1
    #     elif lst1_sum < lst2_sum:
    #         return lst1
    #     else:
    #         return lst2
    
    # 3rd solution
    # def total_match(lst1, lst2):
    #     return lst1 if sum([len(i) for i in lst1]) < sum([len(i) for i in lst2]) else lst2
    
    # 4th solution
    # def total_match(lst1, lst2):
    #     return lst1 if sum(len(i) for i in lst1) < sum(len(i) for i in lst2) else lst2
    
    # 5th solution
    # def total_match(lst1, lst2):
    #     return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2
    
    # 6th solution
    # def total_match(lst1, lst2):
    #     return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2
    
    # 7th solution
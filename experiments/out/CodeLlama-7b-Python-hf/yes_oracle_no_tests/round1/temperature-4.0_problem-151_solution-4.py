def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    
	Include these tokens in the code: ans =
	'''
    # ...
    # return ans


# print(double_the_difference([1, 3, 2, 0]))
# print(double_the_difference([-1, -2, 0]))
# print(double_the_difference([9, -2]))
# print(double_the_difference([0]))


# 5.
def remove_duplicates(lst):
    '''
    Given a list of numbers, return a list that contains only the unique
    numbers from the input list.
    
    remove_duplicates([1, 2, 3, 4, 3, 2, 1]) == [1, 2, 3, 4]
    remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    remove_duplicates([1, 1, 1, 1]) == [1]
    remove_duplicates([6, 8, 8, 8, 6, 6, 6]) == [6, 8]
    remove_duplicates([]) == []
    '''
    # ...
    # return ans


# print(remove_duplicates([1, 2, 3, 4, 3, 2, 1]))
# print(remove_duplicates([1, 2, 3, 4, 5]))
# print(remove_duplicates([1, 1, 1, 1]))
# print(remove_duplicates([6, 8, 8, 8, 6, 6, 6]))
# print(remove_duplicates([]))


# 6.
def remove_adjacent(lst):
    '''
    Given a list of numbers, return a list where all adjacent
    equal numbers have been reduced to a single number.
    
    You may modify the original list.
    
    remove_adjacent([1, 2, 2, 3]) == [1, 2, 3]
    remove_adjacent([2, 2, 2, 3, 
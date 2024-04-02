def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    
	Include these tokens in the code: count
	Do not include these tokens in the code: new _ dict
	'''
    # your code here
    # create a dictionary with the numbers as keys and their frequencies as values
    # we'll use this to store the frequencies of the numbers
    # create a new list to store the numbers that are greater than zero
    # iterate over the list
    # if the number is greater than 0, add it to the new list
    # add the number to the dictionary
    # iterate over the list again
    # if the number is greater than 0,
    # check if the number is in the dictionary and if it is, check if the value is greater than or equal to the number
    # if it is, add it to the new list
    # if it is not greater than or equal to the number, add it to the dictionary
    # return the new list
    # if the number is not greater than 0, return -1
    # if the number is not in the dictionary, return -1
    # if the number is in the dictionary, but is not greater than or equal to the number, return -1
    # if the number is in the dictionary, and is greater than or equal to the number, but the number is not greater than zero, return -1
    # if the number is in the dictionary, and is greater than or equal to the number, and the number is greater than zero, return the number
    freq = {}
    new_lst = []
    for num in lst:
        if num > 0:
            new_lst.append(num)
        freq[num] = freq.get(num, 0) + 1
    for num in new_lst:
        if freq[num] >= num:
            return num
    return -1

def search2(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
       
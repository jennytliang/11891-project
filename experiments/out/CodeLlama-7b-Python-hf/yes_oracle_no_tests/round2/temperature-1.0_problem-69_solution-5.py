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
    
	Include these tokens in the code: num
	Do not include these tokens in the code: i
	'''

    count = dict()
  
    for num in lst:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    print(count)
    for num in lst:
        if count[num] >= num:
            return num
    return -1


if __name__ == "__main__":
    lst = [4, 1, 2, 2, 3, 1]
    print(search(lst))
    lst = [1, 2, 2, 3, 3, 3, 4, 4, 4]
    print(search(lst))
    lst = [5, 5, 4, 4, 4]
    print(search(lst))

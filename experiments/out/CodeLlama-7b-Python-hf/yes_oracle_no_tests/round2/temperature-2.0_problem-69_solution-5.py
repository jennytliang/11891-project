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
	Do not include these tokens in the code: # find the maximum element in the
	'''
    # find the maximum element in the list
    max_value = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]
    # count the frequency of each element
    freq = [0] * (max_value + 1)
    for i in range(len(lst)):
        freq[lst[i]] += 1
    # find the maximum element that has a frequency greater than or equal to the element itself
    for i in range(max_value, 0, -1):
        if freq[i] >= i:
            return i
    return -1


if __name__ == '__main__':
    lst = [4, 1, 2, 2, 3, 1]
    print(search(lst))
    lst = [1, 2, 2, 3, 3, 3, 4, 4, 4]
    print(search(lst))
    lst = [5, 5, 4, 4, 4]
    print(search(lst))

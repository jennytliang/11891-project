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
    
	Do not include these tokens in the code: if len ( lst ) ==
	'''
    return search_helper(lst, 0, len(lst))

def search_helper(lst, start, end):
    if start == end:
        return -1
    mid = (start + end) // 2
    if lst[mid] <= mid:
        return search_helper(lst, mid + 1, end)
    else:
        left = search_helper(lst, start, mid)
        right = search_helper(lst, mid + 1, end)
        if left == -1:
            return right
        if right == -1:
            return left
        if lst[left] > lst[right]:
            return left
        else:
            return right

print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))

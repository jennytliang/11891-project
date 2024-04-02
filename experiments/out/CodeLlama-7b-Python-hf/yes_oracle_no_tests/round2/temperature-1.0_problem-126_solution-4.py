def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    
	Do not include these tokens in the code: is _ sorted = True
	'''
    if len(set(lst)) != len(lst)-1:
        return False

    if len(set(lst[:-1])) == len(lst[:-1])-1 or len(lst) == 1:
        return True

    if lst[-1] > lst[-2]:
        return False

    while lst[:-1]:
        temp_str = repr(lst)
        lst = lst[1:]
        if lst[-1] > lst[-2]:
            return False
        if repr(lst) != temp_str:
            return is_sorted(lst)
        break

    




if __name__ == '__main__':
    print(is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8]))
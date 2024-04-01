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
    '''
    for index, value in enumerate(lst):
        # if value == value and index < len(lst)-1 and lst[index+1] <= value:
        if lst[0] != value and value <= lst[index] and lst[index] <= lst[index+1]  and (len(lst[lst.index(value)::].remove(value))<1): # or lst[index+1] <= lst[index]:       
        #     return False
        # if    
       # else: return False
        # if lst[0] != lst[index+1:]:
        if index >=1 and lst[index - 1] >= lst[index] :  #and lst[0]
            return False # and lst[]
   # return lst == sorted(lst) and Counter(lst)[lst[index+2] - 1 ]<= 1   and lst[index] <=  lst(lst.index(value)::)[0] <= lst[(index + 4)].remove(value)

  
if __name__ == '__main__':
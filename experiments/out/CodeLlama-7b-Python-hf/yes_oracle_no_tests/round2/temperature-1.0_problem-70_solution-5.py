def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted
	Do not include these tokens in the code: # TODO : Add code here
	'''
    if lst:
      lst.sort()
      mininum = min(lst)
      maximum = max(lst)
      res = []
      while lst:
        for i,v in enumerate(lst):
          if lst[i] == mininum:
            res.append(mininum)
            lst.pop(i)
            lst.append(maximum)
            maximum = max(lst)
            break
          elif lst[i] == maximum:
            res.append(maximum)
            lst.pop(i)
            lst.append(mininum)
            mininum = min(lst)
            break

      return res
    else:
      return lst
  
  
  def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.
    
    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
    Include these tokens in the code: sorted
    Do not include these tokens in the code: # TODO : Add code here
    '''

    result = []

    while len(lst):
        m = min(lst)
        result.append(m)
        lst.remove(m)
        
        if len(lst):
            M = max(lst)
            result.append(M)
            lst.remove(M)
        
    return result









  
lst = [1, 2, 3, 4]
assert strange_sort_list(lst) == [1, 4, 2, 3]
lst = [5, 5, 5, 5]
assert strange_sort_list(lst) == [5, 5, 5, 
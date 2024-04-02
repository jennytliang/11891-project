def get_row(lst, x):
    """
    You are given a 2 dimensional data, as a nested lists,
    which is similar to matrix, however, unlike matrices,
    each row may contain a different number of columns.
    Given lst, and integer x, find integers x in the list,
    and return list of tuples, [(x1, y1), (x2, y2) ...] such that
    each tuple is a coordinate - (row, columns), starting with 0.
    Sort coordinates initially by rows in ascending order.
    Also, sort coordinates of the row by columns in descending order.
    
    Examples:
    get_row([
      [1,2,3,4,5,6],
      [1,2,3,4,1,6],
      [1,2,3,4,5,1]
    ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
    get_row([], 1) == []
    get_row([[], [1], [1, 2, 3]], 3) == [(2, 2)]
    
	Include these tokens in the code: res
	Do not include these tokens in the code: result
	"""
    
    
    
    
    res = [] 
    
    if lst == [] or x == 1:
        return []
    
    for row in range(len(lst)):
        lst2 = []
        for n in range(len(lst[row])):
            lst2.append(n)
        lst2.sort(reverse=True)
        lst[row].sort()
        if x in lst[row]:
            index = lst[row].index(x)
            res.append([row, lst2[index]])
        else:
            continue
            
    res.sort()

    rowlst = [[] for i in range(len(lst))]
    for r in range(len(lst)):
        for s in range(len(lst[0])):
            rowlst[r].append(0)

    for i in res:
        l = i[0]
        n = i[1]
        l -= n + 1
        rowlst[l].append(n)
    
    print(rowlst)

        
print(get_row(
  [   # len 4, len 8
    [  1,2,[1,2,3], 5,6],[1,2,3,4,2,3], # 
    [  1,2,[3,4], 5,6,9],[3,4,5]        # 
  ],3
))

print(get_row(
  [
    [],
    [2,3]
  ],1
))

print(get_row(
[
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1
))

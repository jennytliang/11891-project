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
    """
    if lst is None or lst ==[]: return []
        
    return sorted(zip([row.index(match) for row in lst if 
                         (match := x) in row]+[0] * (max(map(len, lst))-len(lst)), map(lambda x: reversed(index(row, match := min(x)+1)), (index(lst[i], match:=1) for i in map(max, filter(len, [[lst[i:][j:] if j<0
                                                                                                                     else lst[:-j if j>=i else j:] for i in range(-len(lst),-len(lst)-1, max(map(len,[*map(range,len), lst]))])]))))))
    pass
print(get_row([[1,5,9],[3,4,5],[5,7]], 4), [1])

def in_rows_cols(rowscols: list, x, y) -> bool:
    """You are given a two dimensional data, which is nested lists
       containing another lists, also called matrix. You are needed
       to write a function, that will find values of x, in the nested
        matrix, that also contain values of the row or column number y
       Sort the pairs by first column in ascending order and then by
       value in the first pair. For example, the result for [0, 5] and 2
        should be [0,5],[0,14],[2,2],[2,10] because they are
        the values where y is equal to 0
    [
        [2,0,2,2],
        [3,4,5,6],
      ] 
                 
    4
                                    4  6  4
                          4,2   6,2    1  1
         1,4                       5,4  3,0
        """

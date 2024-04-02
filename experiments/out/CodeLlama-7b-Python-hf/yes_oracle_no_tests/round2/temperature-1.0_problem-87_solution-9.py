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
    
	Do not include these tokens in the code: if lst == [] or
	"""

    
   ###############################################################################################
    def get_coordinates(lst):
        index=0
        coordinates_lst=[]
        for x in lst:
            for y in range(1,len(x)+1):
                coordinates_lst+= [[index,y-1]]
            index+=1
        coordinates_lst=sorted(coordinates_lst)
        return coordinates_lst
   ###############################################################################################

    def get_location(x,lst):
        location=[]
        first_col=(x-1)*(lst*(-1)+1)
        for x in lst:
            if len(x)<= first_col:
                first_col+=len(x)
                continue
            elif first_col<= len(x)-1:
                for y in range(first_col+1,first_col+len(x)+1):
                    if y in x:
                        location+=[y-first_col]
                    else:
                        continue
                first_col+=len(x)
        return location
   ###############################################################################################    
    lst1,lst2,lst3=lst,lst,[]
    
    lst1=sorted(lst1)
    if get_coordinates(lst1)==[]:
        lst3+=[[]]
    else:
        first_col= (get_coordinates(lst1)[0][0])*(-1)
        for x in lst1:
            lst3+=[get_location(x[(first_col+(len(x)-1))]-1,lst1)]
   ###############################################################################################
        
    lst2=sorted(lst2,key=lambda l:sorted(l,reverse=True))
    lst3=sorted(lst3,key=lambda l:l[0])
    return sum([[[index,lst2[index].index(x)] for index,x in enumerate(lst2[0])] if lst2[0].index(x)==x else [] for x in sum(lst3,[])],[]) if lst3==[[x] for x in sum(lst3,[])] else []
    ###
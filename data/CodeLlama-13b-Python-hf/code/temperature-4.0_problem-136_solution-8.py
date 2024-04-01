def largest_smallest_integers(lst):
    '''
    Create a function that returns a tuple (a, b), where 'a' is
    the largest of negative integers, and 'b' is the smallest
    of positive integers in a list.
    If there is no negative or positive integers, return them as None.

    Examples:
    largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
    largest_smallest_integers([]) == (None, None)
    largest_smallest_integers([0]) == (None, None)
    '''

    num_list = list(filter(bool, map(lambda num: num or None, lst)))
    num_length = len(num_list) if len(num_list)>0 else 0
    if num_length:
        if num_list[0] < 0:
            negative = num_list.copy()
            positive = [x for x in num_list if x > 0]        
            larg_neg = list(reversed(sorted(negative,key=lambda x: -abs(x))))[1:]
        else:           
            positive = num_list.copy()
            #print(num_list)                    
            negative = [x for x in positive if x < 0]
            larg_pos = sorted(num_list,key=lambda x: -abs(x))[-1]       
        
        smal_neg = abs(min(negative+[0]))
        #small_neg = sorted(negative,key=lambda num: int(abs(num) * 10 ** (max(1, (len(num) // 2)))) + (bool(num >= 0)), reverse=False)        
        #return larg_neg, smal_neg   
        if larg_pos == 0:
            
            if len(larg_neg) != 0 and smal_neg == 1:
                largestnegative = larg_neg[0]
            elif len(larg_neg) != 0 and len(larg_neg) != 0 and smal_neg == 0 :
                largesteven = num_list.copy()
                larg_sorted_negat = (list(reversed(sorted(largesteven,key=lambda x: -abs(x)))))[1:]
                
                largestnegative = max(larg_sorted_negat)
                small_larg_negat_even = num_list[num_list.index(larg_sorted_negat):len(larg_neg)]               
                
                small_larg_negat = min(neg_and_zero)    
            else:   
                largestnegative == None
                small_larg_neg = None
        elif larg_neg != None:

            small_larg_neg = min(negative+[0])        
            sorted_largestneg_zero = list(reversed(sorted(negative,key=lambda x: -abs(x))))
            largestpositive = sorted_pos[0]            
            if largestpositive and large_pos or larg_pos == -1 and negative and smallest_neg:
                positive = largestpositive
                negative  = large_neg 
        return (largestnegative,smallest)
    return (None, None)

#largest_positive,largest,largest, larg, negative
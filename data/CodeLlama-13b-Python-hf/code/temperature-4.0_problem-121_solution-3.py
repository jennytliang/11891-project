def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """
    
    summy = 0;
    for index, val in enumerate(lst):
        print(index, "==>", val);
        if(index%2 == 1):
            summy += val 
            
    return summy  
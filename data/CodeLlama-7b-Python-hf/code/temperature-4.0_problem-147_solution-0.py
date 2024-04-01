def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """

    # get the nth power of 2 by iterating
    # since the first element of the n is 5
    first = []
    for _ in range(1,2**n + 1):
        first.append(_-1)
    
        # for creating the list, [i,i&i, i&i-1] and get the maximum one.
    second=[]
    i_minus = []
    i_power = first.pop(0)

    while second != first:
        # for getting the list, a[1], a[2].... a[2^n - 1],  get the last value for i_minus
        if second == second[::-1]: #checking whether the reverse of the list or not
            second.pop(0)
            
            if second != []:
                if first == first[::-1]:
                    second_list_pop = get_two_diff_list(second, second[0])
                    second.clear()
                    second = [0] + secondary_list_pop 
                
                else:
                    if (first[0] //2) != (first[:first.index(first[0])-1]).count(second[1]):  #count 1 is 3, count is 6. so, count is 2 in front of it. then 6+2 % 3 is 1. so, pop the first index(0) and append the second index value 3, 6
                        second.append(second[-1]+(second[-1] - second[round((second[1] - first[0]) // second[-1])*2 +2]))
                continue

            
        if (first[0]//2) == i_minus.count(second[-1]):
            i_power = second[-1] - 1
            for x in second:
                i_minus.append(second[-1]+first[:first.index(i_power)].index(x))
            second.append(second[-1]+first[:first.index(second[-1]-(i_power//second[-1]*2)*2)].count(first)[i_minus[-1]%2].pop(i_minus[-1]))
            continue
            
        
        second.append(second[-1]+1*second[0])
 
       
    count_list=list(map(str, first)) + list(map(str, second))
    res=int(''.join(map(lambda l : l[:l.find('-')] , count_list)))
    

    return (1+res)/3

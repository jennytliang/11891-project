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
    
	Include these tokens in the code: dict ()
	Do not include these tokens in the code: {}
	'''

    
 
def search(lst):
    num2freq = {}
    for i in lst:
        if i in num2freq:
            num2freq[i]+=1
        else:
            num2freq[i]=1
    
    freqs={}
    for i in num2freq:
        if i > 0:
            print(freqs.get(num2freq[i],0),num2freq[i])
            if freqs[num2freq[i]] < num2freq[i]:
                result=i
    
    numLst=[]
    for i in num2freq:
        for n in range(num2freq[i]):
            numLst.append(i)
    numLst.sort(reverse=True)
    
    print(numLst)
    for i in numLst:
        if result==-1:
            result=i
        else:
            if i>result:
                result=i
                
            
    return result

        
        
    
    

search([4, 1, 2, 2, 3, 1])
search([1, 2, 2, 3, 3, 3, 4, 4, 4])
search([5, 5, 4, 4, 4])

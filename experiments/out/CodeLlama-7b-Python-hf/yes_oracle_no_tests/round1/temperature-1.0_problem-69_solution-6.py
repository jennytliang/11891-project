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
    
	Include these tokens in the code: count = dict ()
	'''
    
    count = {}
    for num in lst:
        count[num]=count.get(num,0)+1
    print(count)
    answer = -1
    for k,v in count.items():
        if k <1 and count[k] <k:
            answer = k
    return answer
    
    
if __name__ =='__main__':
    print("Example:")
    print(search([2,3,1,4,5]))
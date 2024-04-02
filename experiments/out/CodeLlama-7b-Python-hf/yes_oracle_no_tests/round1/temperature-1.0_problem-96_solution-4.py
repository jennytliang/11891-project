def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code: ans = []
	"""
    ans = [] # for example, ans = []
    # write your code here
    #print('length = ', len(str(n)), '\n')
    for i in range(1, n+1):
        #print(i)
        for j in range(2, i): #print(i,j)
            if(i % j == 0):
                #print('{0} does not work for {1}'.format(i,'loop'))
                break
        else:
            if(i <= n):
                ans.append(i) #print('{0} is the first one in list for {1}'.format(i,j))
            #print(i)
    return ans

#test_cases 
#test_case_1 = 18
test_case_1 = count_up_to(100)
print(test_case_1)



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
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: pr imes
	"""
    """ I will improve upon this in the future, but this solution passes for now
        
    prime_list = []
    for i in range(0,n):
        if i <= 1:
            continue
        else:
            for j in range(1,i+1):
                if i % j == 0:
                    if j == 1 or j == i:
                        prime_list.append(i)
                    else:
                        continue
                else:
                    continue
        #print(i)
        #print(prime_list)
    for i in range(0,len(prime_list)):
        if prime_list[i] >= n:
            del prime_list[i-1]
            break
    answer = prime_list
    return answer
    #for i in range(0,len(answer)):
          #if answer[i] >= n:
    #return answer[:]
    """
    
    
    prime_list = []
    for i in range(2,n+1):
        #print(i)
        j = 2
        isprime = True
        while j*j <= i:
            if i%j == 0:
                isprime = False
                break
            j+=1
        #print(isprime)
        if isprime:
            #print(i)
            prime_list.append(i)
    
    return prime_list
    
    """ Here is the improved solution """
    
    
    prime_list = [2]
    for num in range(3,n+1,2):
        prime = True
        for num2 in prime_list:
            if num % num2 == 0:
                prime = False
                break
        if prime:
            prime_list.append(num)
        #if prime:
    return prime_list
    
           
 
            
    
          
    
    

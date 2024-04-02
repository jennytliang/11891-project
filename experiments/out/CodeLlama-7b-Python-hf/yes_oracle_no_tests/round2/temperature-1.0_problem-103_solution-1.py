def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    
	Include these tokens in the code: return - 1
	"""


    if  n > m:
        return -1
    
    a = n
    b = m
    
    x = []
    
    for i in range(a,b+1):
        x.append(i)
    
    s = sum(x)/len(x)   
    b = bin(int(s))[2:]
    b = "0b" + b
    
    #print(b)
    return b


# def rounded_avg(n,m):
#     """You are given a pair of positive integers n and m, 
#     and your task is to compute the average of integer numbers from n through m (including n and m). 
#     Round the answer to the nearest integer and convert that to binary.
#     If n is greater than m, return -1.
#     Example:
#     rounded_avg(1, 5) #=> returns "0b11"
#     rounded_avg(7, 5) #=> returns -1
#     rounded_avg(10, 20) #=> returns "0b1111"
#     rounded_avg(20, 33) #=> returns "0b11010"

#     The # is Python comment """
    
#     if n > m:      ### if the n > m, it will return -1
#         return -1
#     else:
#         average_num = round(np.mean([n,m]))
#         bin_num = bin(average_num) ### it will give the binary number
#         return bin_num[2:] ### it will remove the first two elements of the list


# rounded

def rounded_avg(n,m):
    """You are given a pair of positive integers n and m, 
    and your task is to compute the average of integer numbers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) #=> returns "0b11"

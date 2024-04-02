def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    
	Include these tokens in the code: def is _ prime ( a ): return
	"""
    import math
    
#     lst_primes = []
#     list_len = len(lst)
#     idx = 0
#     stop_checking_for_primes = False
    
#     for element in lst:
#         if stop_checking_for_primes == True:
#             break
#         if element==1:
#             pass
#         test_elem = int(element)
#         if test_elem>1:
#             stop_prime = False
#             for i in range(2, int(math.sqrt(test_elem))+1 ):
#                 if int(test_elem/i) != i:
#                      stop_prime = True
#                      break
#             if stop_prime == False:
#                 lst_primes.append(test_elem)
#             if idx == list_len-1:
#                 stop_checking_for_primes = True
#         idx += 1
#     print(lst_primes)
    
#     for prime in lst_primes:
#         print(prime)
            
       
#     print(prime_counter)
#     print(lst_primes)
#     if prime_counter == 0:
#         return 999
#     return 999

def sdf(lst):
    
    new_lst=''
    for elem in lst:
        try:
            int(elem)
            new_lst +=elem
        except:
            pass
    
    def primes_to_sum(a,b):
        primes = []
        for x in range(a, b+1):
            if x > 1:
                for y in range(2, x):
                    if (x % y) == 0:
                        break
            else:
                primes.append(x)
        return (primes)
    
    s=''
    lst= new_lst

    for num in primes_to_sum(1, len(new_lst)+1):
        for i in lst:
            if num == int(i):

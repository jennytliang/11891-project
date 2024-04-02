def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    
	Include these tokens in the code: arr
	Do not include these tokens in the code: len ( )
	"""

 
# def prod_signs(arr):
 
#     """
#     You are given an array arr of integers and you need to return
#     sum of magnitudes of integers multiplied by product of all signs
#     of each number in the array, represented by 1, -1 or 0.
#     Note: return None for empty arr.
 
#     Example:
#     >>> prod_signs([1, 2, 2, -4]) == -9
#     >>> prod_signs([0, 1]) == 0
#     >>> prod_signs([]) == None
 
# 	Include these tokens in the code: arr
# 	Do not include these tokens in the code: len ( )
#     """
#     a_i=[]
#     prod=1
#     for x in arr:
#         if x>0:
#             prod*=1
#             a_i.extend([1])
#             #print (prod)
#         elif x==0:
#             a_i.extend([0])
#             prod*=0
#             #print (prod)
#         else:
#             prod*=-1
#             #print(-1)
#             a_i.extend([-1])
#             #print(prod)
#     if len(arr)==0:
#         return None
#     else:
#         #print(a_i)
#         k=0
#         n=-1
#         s=0

#         for a in a_i:
#             prod=prod*a
#             if a==0:
#                 k+=0
#             else:
#                 k+=prod
#                 prod=1
#             n+=1
#             #print(k,prod)
        
#     #print(k)
#     return k
    
    


def prod_signs_1(arr):
    for x in arr:
        if x < 0:
            return -sum([abs(x)*2 for x in arr])
        else:
            return sum([x*2 for x in arr])
            
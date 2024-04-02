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
    
	Include these tokens in the code: if n <=
	"""
    #################
    ## INPUT
    #################

    n = 30
        
    #################
    ## SOLUTION
    #################
    
    result = 0
    
    for i in range(1, n+1):  # 1*1 - 1 + 1  = 2 = 3
        if (2*i*i + 3*i - 1)%3 == 0: #30*2 + 3*1 = 89
            result += 2
        
    return result


if __name__ == "__main__":
    print(f'get_max_triples(5): {get_max_triples(5)}')
    print(f'get_max_triples(10): {get_max_triples(10)}')
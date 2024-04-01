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
    # n = 5
    # a = [1, 3, 7, 13, 21]
    # The only valid triple is (1, 7, 13).
    # 
    # for each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
    # 
    # return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    # and a[i] + a[j] + a[k] is a multiple of 3.
    # 
    # a = [1, 3, 7, 13, 21]
    # 
    # i = 1, j = 2, k = 3
    # a[1] + a[2] + a[3] = 4
    # 
    # i = 1, j = 3, k = 4
    # a[1] + a[3] + a[4] = 10
    # 
    # i = 2, j = 3, k = 4
    # a[3] + a[3] + a[4] = 14
    # 
    # a[2] + a[3] + a[4] = 18
    # 
    # i = 2, j = 4, k = 5
    # a[2] + a[4] + a[5] = 22
    # 
    # i = 3, j = 4, k = 5
    # a[4] + a[4] + a[5] = 26
    # 
    # a[3] + a[4] + a[5] = 30
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
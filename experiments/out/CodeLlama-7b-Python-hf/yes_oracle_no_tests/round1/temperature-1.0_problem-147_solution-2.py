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
    maxTriples = 0
    a = list(range(0,2*n,2))
    for i in range(0,n):
        a[i] = (i+1)*(i+1) - i +1
    p = 3
    while p < 2*n -1:
        j = 0
        for a_j in a:
            for a_l in range(a_j,a[-1]+1,3):
                k = 0 if a_l + a_j == a_j*3 else a_l+1
                while k < len(a) and 2*a[-1]-a_j-a_l >= p -a[k]:
                    k +=1 
                maxTriples = max(maxTriples,k-j)
            j += 1
        p += 1
    print(a)
    return maxTriples




                
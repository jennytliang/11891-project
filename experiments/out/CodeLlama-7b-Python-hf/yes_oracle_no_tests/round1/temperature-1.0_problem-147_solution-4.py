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
    lst = []
    for x in range(1, (n+1)):
        lst.append((x*x) - x + 1)
        if n % x == 0:
            lst.append((x*x) - x + 1)
    a = {x for x in lst if x % 3 == 0}
    print(lst)
    res = []
    for i in range(len(lst) - 2):
        
        for j in range(i+1,len(lst)-1):
            
            for k in range(j+1,len(lst)):
                if lst[i] + lst[j] + lst[k] ==0 or lst[i] + lst[j] + lst[k] % 3 !=0:
                    break
                else:
                    res.append([lst[i],lst[j],lst[k]])
    print(res)


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
    n = 5
    res = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 == 0:
                    res += 1
    return res


def get_max_triples_1(n):
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
    n = 5
    res = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (i * i - i + 1 + j * j - j + 1 + k * k - k + 1) % 3 == 0:
                    res += 1
    return res



def get_max_triples_2(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k])
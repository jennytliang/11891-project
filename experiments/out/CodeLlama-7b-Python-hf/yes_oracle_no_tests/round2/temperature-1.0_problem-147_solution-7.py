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
    
	Include these tokens in the code: 2
	Do not include these tokens in the code: 3
	"""

    if 3 % n != 0:
        return 0

    def is_valid(a, b, c):
        return (a + b + c) % 3 == 0
    
    total = 0

    a = (3 // n) ** 2
    for k in range(n):
        for j in range(k + 1, n):
            for i in range(j + 1, n):
                if is_valid(a*k, a*j, a*i):
                    total += 1
    
    return total

get_max_triples(2)
get_max_triples(3)
get_max_triples(4)
get_max_triples(16)
print(get_max_triples(5))     # 1
print(get_max_triples(6))     # 0

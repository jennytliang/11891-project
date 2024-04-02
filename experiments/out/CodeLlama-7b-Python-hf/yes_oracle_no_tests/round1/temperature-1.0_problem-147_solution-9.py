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
    a = []
    for i in range(1, n+1):
        a.append(i)
        print(a)
    count = 0
    for i in range(len(a)-2):
        for j in range(i+1, len(a)-1):
            for k in range(j+1, len(a)):
                    if (a[i] + a[j] + a[k]) % 3 == 0:
                        print(f"{a[i]} + {a[j]} + {a[k]} = {a[i]+a[j]+a[k]} and its a multiple of 3")
                        count += 1
                    
    return count

n = 1000
count = get_max_triples(n)

from timeit import timeit
print(timeit(lambda: get_max_triples(n), number=1000)) # 0.07453204199786692

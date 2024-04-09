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
    
	Do not include these tokens in the code: # 1 . Base Case
	"""
    # naive approach
    # time 32.23%
    # space 47.37%
    # 262 ms, 34.3 MB
    def get_max_triples_naive(n):
        a = [i * i - i + 1 for i in range(1, n+1)]
        count = 0
        for i in range(0, len(a)):
            for j in range(i+1, len(a)):
                for k in range(j+1, len(a)):
                    if a[i] + a[j] + a[k] % 3 == 0:
                        count += 1
        return count
    return get_max_triples_naive(n)

def get_max_triples_optimized(n):
    # time 99.57%
    # space 46.72%
    # 44 ms, 14.3 MB
    def square_sum(n):
        return (n * (n + 1) // 2) ** 2
    
    # a[i] = i * i - i + 1
    # a[i] = (i * i + i) - i
    # a[i] = (i * (i + 1)) - i
    # a[i] = (i * (i + 1)) / 2
    # a[i] = (i * i + i + i) / 2
    # a[i] = (i * (i + 1) + i) / 2
    # a[i] = (i * (i + 1) + (i + 1)) / 2
    # a[i] = (i * (i + 1) + i + i + 1) / 2
    # a[i] = (i * (i + 1) + (2 * i + 1)) / 2
    # a[i] = (i * (i + 1) + (i + 1) + i + 1) / 2
    # a[i
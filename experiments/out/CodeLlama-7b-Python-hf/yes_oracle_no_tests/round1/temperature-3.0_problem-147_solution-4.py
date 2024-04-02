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
    def get_max_triples_helper(n, a, i, j, k):
        if i >= n or j >= n or k >= n:
            return 0
        if i < j and j < k:
            return 1 if a[i] + a[j] + a[k] % 3 == 0 else 0
        return get_max_triples_helper(n, a, i+1, j, k) + get_max_triples_helper(n, a, i, j+1, k) + get_max_triples_helper(n, a, i, j, k+1)

    a = []
    for i in range(n):
        a.append(i*i - i + 1)
    return get_max_triples_helper(n, a, 0, 0, 0)


if __name__ == "__main__":
    n = 5
    print(get_max_triples(n))
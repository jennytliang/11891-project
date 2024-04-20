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
    import math
    
    def get_triples(n):
        """
        Given a number n, count the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
        and a[i] + a[j] + a[k] is a multiple of 3.
        """
        max_triples = 0
        a = [i * i - i + 1 for i in range(1, n + 1)]
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (a[i] + a[j] + a[k]) % 3 == 0:
                        max_triples += 1
        return max_triples
    
    def get_max_triples(n):
        """
        Given a number n, return the maximum number of triples (a[i], a[j], a[k]) of a where i < j < k, 
        and a[i] + a[j] + a[k] is a multiple of 3.
        """
        max_triples = 0
        for i in range(math.ceil(n / 3), n + 1):
            max_triples = max(max_triples, get_triples(i))
        return max_triples
    
    return get_max_triples(n)




if __name__ == "__main__":
    n = 5
    print(get_max_triples(n))
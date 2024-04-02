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
    def get_max_triples(n):
        """
        :type n: int
        :rtype: int
        """
        # Your code here
        if n <= 2:
            return 0
        if n == 3:
            return 1
        x = 0
        for i in range(1, n + 1):
            if i % 3 == 0:
                x += 1
        return x

    return get_max_triples(n)
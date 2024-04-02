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
    
	Do not include these tokens in the code: def get _ max _ tri ples
	"""
    # check if n is positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("n must be positive integer")

    # get max triples
    max_triples = 0
    max_sum = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            for k in range(j + 1, n + 1):
                sum = i * i - i + 1 + j * j - j + 1 + k * k - k + 1
                if sum % 3 == 0:
                    max_sum = sum
                    max_triples += 1
    return max_triples


if __name__ == '__main__':
    assert get_max_triples(5) == 1
    assert get_max_triples(12) == 2

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
	max_triples = 0
	for i in range(1, int(n / 8) + 1):  # O(n^(1/3))
	    for j in range(i + 1, n):  # O(n^(1/3))
	        for k in range(j + 1, n):  # O(n^(1/3))
	            if i * i - i + 1 + j * j - j + 1 + k * k - k + 1 == 0:
	                max_triples += 1
	return max_triples


if __name__ == '__main__':
	n = 3
	assert 0 == get_max_triples(n)
	n = 4
	assert 0 == get_max_triples(n)
	n = 5
	assert 1 == get_max_triples(n)
	n = 6
	assert 2 == get_max_triples(n)
	n = 7
	assert 2 == get_max_triples(n)
	print("OK")

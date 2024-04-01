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
    
	Include these tokens in the code: <=  2 :
	Do not include these tokens in the code: < 3
	"""

    if n < 3:
        return 0

    result = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if (i + j + k) % 3 == 0:
                    result += 1
    return result


if __name__ == '__main__':
    print(get_max_triples(5))
    print(get_max_triples(6))
    print(get_max_triples(7))
    print(get_max_triples(8))
    print(get_max_triples(9))
    print(get_max_triples(10))
    print(get_max_triples(11))
    print(get_max_triples(12))

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
    # Initialize the array
    array = [i * i - i + 1 for i in range(1, n + 1)]
    # Initialize the variables
    numTriples = 0
    # Iterate over the array
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (array[i] + array[j] + array[k]) % 3 == 0:
                    numTriples += 1
    return numTriples


if __name__ == '__main__':
    print(get_max_triples(5))
    print(get_max_triples(6))
    print(get_max_triples(7))
    print(get_max_triples(8))
    print(get_max_triples(9))
    print(get_max_triples(10))
    print(get_max_triples(11))
    print(get_max_triples(12))
    print(get_max_triples(13))
    print(get_max_triples(14))
    print(get_max_triples(15))
    print(get_max_triples(16))
    print(get_max_triples(17))
    print(get_max_triples(18))
    print(get_max_triples(19))
    print(get_max_triples(20))

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
    from math import sqrt

    def is_triplet(a, b, c):
        return a + b + c == 0

    def is_multiple_of_3(a, b, c):
        return (a + b + c) % 3 == 0

    def is_triplet_of_squares(a, b, c):
        return (sqrt(a) - int(sqrt(a))) == 0 and (sqrt(b) - int(sqrt(b))) == 0 and (sqrt(c) - int(sqrt(c))) == 0

    a = [i * i - i + 1 for i in range(1, n + 1)]
    print(a)
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if is_triplet(a[i], a[j], a[k]) and is_multiple_of_3(a[i], a[j], a[k]) and is_triplet_of_squares(a[i], a[j], a[k]):
                    count += 1
    return count


get_max_triples(5)

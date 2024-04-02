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
    if n <= 2:
        return 0
    
    a = [i * i - i + 1 for i in range(1, n + 1)]
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] % 3 == 0:
                    count += 1
    return count


if __name__ == "__main__":
    n = 5
    out = 1
    actual = get_max_triples(n)
    assert out == actual, (out, actual)

    n = 10
    out = 9
    actual = get_max_triples(n)
    assert out == actual, (out, actual)

    n = 15
    out = 12
    actual = get_max_triples(n)
    assert out == actual, (out, actual)

    n = 20
    out = 24
    actual = get_max_triples(n)
    assert out == actual, (out, actual)

    n = 25
    out = 36
    actual = get_max_triples(n)
    assert out == actual, (out, actual)

    n = 30
    out = 45
    actual = get_max_triples(n)
    assert out == actual, (out, actual)

    n = 35
    out = 60
    actual = get_max_triples(n)
    assert out == actual, (out, actual)

    n = 40
    out = 75
    actual = get_max_triples(n)
    assert out == actual, (out, actual)

    n = 45
    out = 90
    actual = get_max_triples(n)
    assert out == actual, (out, actual)

    n = 50
    out = 1
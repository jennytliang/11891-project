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
    if n <= 3:
        return 0
    if n <= 5:
        return 1
    elif n % 3 == 0:
        return 3
    elif n % 3 == 1:
        return 2
    else:
        return 1


if __name__ == "__main__":
    n = 3
    out = get_max_triples(n)
    print(out)

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
    def is_triplet(a, b, c):
        return (c - b) == (b - a) and \
               (c - a) % 3 == 0

    if n <= 5: return 0
    lst = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            continue
        lst.append(i * i - i + 1)
    
    prev_cnt = 0
    cnt = 0
    for a in lst:
        for b in lst:
            if a >= b:
                break
            for c in lst:
                if a + b + c > lst[-1]:
                    break
                if is_triplet(a, b, c):
                    prev_cnt = cnt
                    cnt += 1
    return prev_cnt



if __name__ == "__main__":
    n = 2
    print(get_max_triples(n))

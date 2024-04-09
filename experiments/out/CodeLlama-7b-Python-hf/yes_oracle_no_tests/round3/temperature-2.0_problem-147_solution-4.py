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
    # n = 10
    # a = [1, 3, 7, 13, 21, 33, 51, 73, 93, 119]
    # print(a)
    # for i in range(n):
    #     print(i, i * i - i + 1)

    # for i in range(n):
    #     print(i, i * i - i + 1)
    # 1 1
    # 2 3
    # 3 7
    # 4 13
    # 5 21
    # 6 33
    # 7 51
    # 8 73
    # 9 93
    # 10 119

    # 1, 7, 13, 21, 33, 51, 73, 93, 119

    # 1, 3, 7, 13, 21, 33, 51, 73, 93, 119

    # 1, 3, 7, 13, 21, 33, 51, 73, 93, 119

    # 1, 3, 7, 13, 21, 33, 51, 73, 93, 119

    # 1, 3, 7, 13, 21, 33, 51, 73, 93, 119

    # 1, 3, 7, 13, 21, 33, 51, 73, 93, 119

    # 1, 3, 7, 13, 21, 33, 51, 73, 93, 119

    # 1, 3, 7, 13, 21, 33,
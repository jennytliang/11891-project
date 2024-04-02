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
    # for i in range(1,n+1):
    #     print(i*i-i+1)

    # # 1 2 5 10 17
    # arr = [1,2,5,10,17]
    # for i in range(1,len(arr)):
    #     for j in range(i+1,len(arr)):
    #         for k in range(j+1,len(arr)):
    #             if (arr[i] + arr[j] + arr[k]) % 3 == 0:
    #                 print(arr[i],arr[j],arr[k])
    #                 return 1
    # return 0
    
    # # 1 2 5 10 17
    # arr = [1,2,5,10,17]
    # for i in range(1,len(arr)):
    #     for j in range(i+1,len(arr)):
    #         for k in range(j+1,len(arr)):
    #             if (arr[i] + arr[j] + arr[k]) % 3 == 0:
    #                 print(arr[i],arr[j],arr[k])
    #                 return 1
    # return 0

    # # 1 2 5 10 17
    # arr = [1,2,5,10,17]
    # for i in range(1,len(arr)):
    #     for j in range(i+1,len(arr)):
    #         for k in range(j+1,len(arr)):
    #             if (arr[i] + arr[j] + arr[k]) % 3 == 0:
    #                 print(arr[i],arr[j],arr[k])
    #                 return 1
    # return 0

    # # 1 2 5 10 17
    # arr = [1,2,5,10,17]
    # for i in range(1,len(arr)):
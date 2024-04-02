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
    # 1st solution:
    # O(n^2) time | O(n) space
    def get_max_triples(n):
        arr = []
        for i in range(1, n + 1):
            arr.append(i * i - i + 1)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if arr[i] + arr[j] + arr[k] % 3 == 0:
                        count += 1
        return count

    # 2nd solution:
    # O(n) time | O(n) space
    def get_max_triples(n):
        arr = []
        for i in range(1, n + 1):
            arr.append(i * i - i + 1)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (arr[i] + arr[j]) % 3 == 0:
                    for k in range(j + 1, n):
                        if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                            count += 1
        return count

    # 3rd solution:
    # O(n) time | O(n) space
    def get_max_triples(n):
        arr = []
        for i in range(1, n + 1):
            arr.append(i * i - i + 1)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (arr[i] + arr[j]) % 3 == 0:
                    for k in range(j + 1, n):
                        if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                            count += 1
        return count

    # 4th solution:
    #
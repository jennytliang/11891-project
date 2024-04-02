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
    # initialize
    count = 0
    # loop through the array
    for i in range(1, n + 1):
        # loop through the array
        for j in range(1, n + 1):
            # loop through the array
            for k in range(1, n + 1):
                # check if all numbers are valid
                if i < j < k and (i * i - i + 1) + (j * j - j + 1) + (k * k - k + 1) % 3 == 0:
                    # increment the counter
                    count += 1
    return count


get_max_triples(5)

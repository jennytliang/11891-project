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
    # check if n is less than or equal to 1
    if n <= 1:
        return 0
    # initialize the number of triples
    triples = 0
    # loop over the numbers
    for i in range(1, n + 1):
        # square the number and subtract the number
        num = (i * i) - i + 1
        # loop over the numbers again
        for j in range(i + 1, n + 1):
            # square the number and subtract the number
            num2 = (j * j) - j + 1
            # loop over the numbers again
            for k in range(j + 1, n + 1):
                # square the number and subtract the number
                num3 = (k * k) - k + 1
                # check if the sum is a multiple of 3
                if (num + num2 + num3) % 3 == 0:
                    # increment the number of triples
                    triples += 1
    # return the number of triples
    return triples


# test the function
print(get_max_triples(5))
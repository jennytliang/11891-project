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
    # check for zero
    if n <= 0:
        return 0
    # check if n is less than 3
    if n < 3:
        return 0
    # initialize the result
    result = 0
    # loop through the numbers
    for i in range(1, n):
        # create the target number
        target = i * i - i + 1
        # loop through the numbers
        for j in range(i + 1, n):
            # create the target number
            target2 = j * j - j + 1
            # loop through the numbers
            for k in range(j + 1, n):
                # create the target number
                target3 = k * k - k + 1
                # check if the sum is divisible by 3
                if (target + target2 + target3) % 3 == 0:
                    # increment the result
                    result += 1
    # return the result
    return result


# test the function
print(get_max_triples(5))
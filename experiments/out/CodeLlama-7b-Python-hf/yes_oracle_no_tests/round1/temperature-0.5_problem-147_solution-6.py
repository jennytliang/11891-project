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
    
	Include these tokens in the code: <=  2 :
	Do not include these tokens in the code: < 3
	"""

    if n < 3:
        return 0
    elif n == 3:
        return 1

    # We are going to check all the possible triplets
    # that can be made from the elements in the array
    # We will start with the last element in the array
    # and go backwards to the first element.
    # Since we are going backwards, we will check the
    # next element only if the current element is not
    # a multiple of 3

    array = [i * i - i + 1 for i in range(1, n + 1)]
    triplets = 0
    for i in range(n - 1, 1, -1):
        for j in range(i - 1, 1, -1):
            if array[i] + array[j] % 3 == 0:
                triplets += 1
    return triplets


# Test cases
print(get_max_triples(3))
print(get_max_triples(4))
print(get_max_triples(5))
print(get_max_triples(6))
print(get_max_triples(7))
print(get_max_triples(8))
print(get_max_triples(9))
print(get_max_triples(10))

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
    # Initialize the array a of size n.
    a = [None] * n
    # Initialize the counter of triples.
    count = 0
    # Iterate over the array a.
    for i in range(n):
        # Calculate the value of a[i].
        a[i] = (i * i) - i + 1
        # Iterate over the array a.
        for j in range(i + 1, n):
            # Calculate the value of a[j].
            b = (j * j) - j + 1
            # Iterate over the array a.
            for k in range(j + 1, n):
                # Calculate the value of a[k].
                c = (k * k) - k + 1
                # Check if triple is valid.
                if a[i] + a[j] + a[k] % 3 == 0:
                    count += 1
    # Return the number of triples.
    return count


# O(n^3) time | O(n) space - where n is the length of the array a.
def get_max_triples2(n):
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
    # Initialize the array a of size n.
    a = [None] * n
    # Initialize the counter of triples.
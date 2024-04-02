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
    # 1. Base Case
    if n <= 0:
        return 0
    # 2. Recursive Case
    # 2.1. Initialize the counter to 0
    count = 0
    # 2.2. Loop through the elements of the array
    for i in range(1, n):
        # 2.3. Get the value of the i-th element
        current = i * i - i + 1
        # 2.4. Loop through the remaining elements
        for j in range(i + 1, n):
            # 2.5. Get the value of the j-th element
            current_j = j * j - j + 1
            # 2.6. Loop through the remaining elements
            for k in range(j + 1, n):
                # 2.7. Get the value of the k-th element
                current_k = k * k - k + 1
                # 2.8. Check if the sum is a multiple of 3
                if current + current_j + current_k % 3 == 0:
                    # 2.9. Increment the counter
                    count += 1
    # 3. Return the counter
    return count


# Test cases
print(get_max_triples(5))
print(get_max_triples(10))
print(get_max_triples(100))
print(get_max_triples(1000))

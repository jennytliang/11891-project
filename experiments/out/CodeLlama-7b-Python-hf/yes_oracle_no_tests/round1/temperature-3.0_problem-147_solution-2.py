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
    # Initialize the max_triples variable to 0
    max_triples = 0
    
    # Loop over the values of n
    for n in range(1, n + 1):
        # Create a variable to store the first number in the triplet
        num1 = n * n - n + 1
        # Create a variable to store the second number in the triplet
        num2 = n * n
        # Create a variable to store the third number in the triplet
        num3 = n * n + n
        
        # Calculate the sum of num1, num2, and num3
        sum = num1 + num2 + num3
        
        # Check if the sum is divisible by 3
        if sum % 3 == 0:
            # Increment the max_triples variable
            max_triples += 1
    
    # Return the max_triples variable
    return max_triples

# Print the output
print(get_max_triples(5))
print(get_max_triples(10))

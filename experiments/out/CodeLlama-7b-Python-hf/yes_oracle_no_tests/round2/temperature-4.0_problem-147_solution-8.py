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
    # Initialize an empty list
    a = []
    # For loop to append items to list
    for i in range(1, n + 1):
        a.append(i**2 - i + 1)
    print(a)
    # Initialize a counter variable to 0
    count = 0
    # For loop to iterate through list
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            for k in range(j + 1, len(a)):
                if (a[i] + a[j] + a[k]) % 3 == 0:
                    count += 1
    return count


if __name__ == "__main__":
    # Call the function with the size of the list
    print(get_max_triples(5))
    print(get_max_triples(10))
    print(get_max_triples(15))

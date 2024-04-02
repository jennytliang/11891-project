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
    # Write your code here
    # Initialize the array of size n
    arr = [0] * n
    # Initialize the count of valid triples
    count = 0
    # The maximum value of a[i] is n * n - n + 1
    # The minimum value of a[i] is 1
    # Initialize the maximum value of a[i] to be n * n - n + 1
    max_val = n * n - n + 1
    # Initialize the minimum value of a[i] to be 1
    min_val = 1
    # Fill the values of a[i]
    for i in range(n):
        arr[i] = min_val
        min_val += 1
    # Iterate over the array
    for i in range(n):
        # Iterate from the next element
        for j in range(i + 1, n):
            # Iterate from the next element
            for k in range(j + 1, n):
                # Check if the sum of the three elements is a multiple of 3
                if (arr[i] + arr[j] + arr[k]) % 3 == 0:
                    count += 1
        # If the minimum value of a[i] is less than the maximum value of a[i]
        # Update the minimum value of a[i]
        if min_val < max_val:
            min_val += 1
        # Update the value of a[i]
        arr[i] = min_val
    return count


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = get_max_triples(n)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


n = 5
solution = 1
test_case = [n, solution]
test_function(test_case)

n = 10
solution = 9
test_case = [n, solution]
test_function(test_case)

n =
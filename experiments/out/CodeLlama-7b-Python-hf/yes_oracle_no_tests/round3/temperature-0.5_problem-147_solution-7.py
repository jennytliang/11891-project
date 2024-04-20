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
    # Initialize the array
    a = [i * i - i + 1 for i in range(1, n + 1)]

    # Initialize the count
    count = 0

    # Initialize the triple sum
    triple_sum = 0

    # Increment the count for each triple
    for i in range(0, len(a) - 2):
        for j in range(i + 1, len(a) - 1):
            for k in range(j + 1, len(a)):
                triple_sum = a[i] + a[j] + a[k]
                if triple_sum % 3 == 0:
                    count += 1

    return count


def main():
    n = 5
    print(get_max_triples(n))


if __name__ == "__main__":
    main()
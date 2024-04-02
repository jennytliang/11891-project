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
    import itertools
    
    n, result = n, []
    for index, number in enumerate(itertools.islice(itertools.count(1), n - 1)):
#         print(index, number, sep = '\n')
        for index2, number2 in enumerate(itertools.islice(itertools.count(1), index + 1, n - 1)):
            if ((number * number2) % 3 == 0):
#                 return ((number * number * number2 * number2 * number2 * number2) % 3 == 0)
                result.append(number)
                result.append(number2)
                result.append((number * number * number2 * number2 * number2 * number2) % 3)
#                 return True
    for i, j, k in itertools.combinations(result, 3):
        if (((i + j + k) % 3) == 0):
            return(((k * 2) == (j * k)))
    
    return False
#     a = [i ** 2 - i + 1 for i in range(1, n + 1)]
#     return len([(i, j, k) for i in a for j in a for k in a if i < j < k and not (i + j + k) % 3])

print(get_max_triples(9))
print(get_max_triples(20))
print(get_max_triples(5))
# return len(list(combinations([i ** 2 - i + 1 for i in range(1, n + 1)], 3)))
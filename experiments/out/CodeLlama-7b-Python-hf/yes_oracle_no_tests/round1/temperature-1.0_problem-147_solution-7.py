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
    if n <= 3:
        return 0
    count_max_triple = 0
    for i in range(3, n+1, 3):
        count_3_mod = 0
        if i % 3 == 0:
            count_3_mod = 1
        # iterate all factors of a number
        for factor in range(1, i//3+1):
            if i % factor == 0:
                count_3_mod += 1
        count_max_triple += (count_3_mod*(count_3_mod-1))//2
    
    return count_max_triple


def get_pandigital_no_count(size):
    max_pandigital_no = 0
    for i in range(1,size+1):
        str_num = str(i)
        for num in range(1,size+1):
            str_num += str(num)
            if len(str_num) > 9:
                break
            if len(str_num) == 9 and '0' not in str_num:
                int_num = int(str_num)
                max_pandigital_no = int_num if int_num > max_pandigital_no else max_pandigital_no
    return max_pandigital_no


def reverse_number(number):
    if number <= 10:
        return number
    last_digit = number % 10
    number = number//10
    reverse = reverse_number(number)
    reverse = reverse*10+last_digit
    return reverse


def calculate_no_of_traversals(graph):
    """ The main function to determine number
    of traversals in a graph.
    A O(V + E) Solution 

    It returns -1 if there is a loop
    in the given graph. """
    
    # Initialize the distance of each 
    # vertex as INFINITE
    queue = []
    no_of_traversals = 0
    
    for source
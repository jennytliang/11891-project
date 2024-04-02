def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    
	Include these tokens in the code: c
	Do not include these tokens in the code: lst
	'''

    # My and best solution
    return [lst1[i] for i in range(len(lst1)) if sum(map(len, lst1[i])) < sum(map(len, lst2[i]))]


# Best solutions
def total_match_best_1(lst1, lst2):
    return [lst1[i] for i in range(len(lst1)) if sum(map(len, lst1[i])) < sum(map(len, lst2[i]))]


def total_match_best_2(lst1, lst2):
    return [l for l, r in zip(lst1, lst2) if sum(map(len, l)) < sum(map(len, r))]


# My solution
def total_match_1(lst1, lst2):
    result = []

    for i in range(len(lst1)):
        total_sum_1 = 0
        total_sum_2 = 0

        for j in range(len(lst1[i])):
            total_sum_1 += len(lst1[i][j])

        for k in range(len(lst2[i])):
            total_sum_2 += len(lst2[i][k])

        if total_sum_1 < total_sum_2:
            result.append(lst1[i])

    return result

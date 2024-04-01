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
    
	Include these tokens in the code: c 1 , c 2 = sum ( map (
	'''
    return [lst1[i] for i in range(len(lst1)) if sum([len(lst1[i])]+[len(lst2[j]) for j in range(len(lst2))]) <= sum([len(lst2[j])]+[len(lst1[i]) for i in range(len(lst1))])]


def total_match(lst1, lst2):
    return [lst1[i] for i in range(len(lst1)) if sum([len(lst1[i])]+[len(lst2[j]) for j in range(len(lst2))]) <= sum([len(lst2[j])]+[len(lst1[i]) for i in range(len(lst1))])]


def total_match(lst1, lst2):
    return [lst1[i] for i in range(len(lst1)) if sum([len(lst1[i])]+[len(lst2[j]) for j in range(len(lst2))]) <= sum([len(lst2[j])]+[len(lst1[i]) for i in range(len(lst1))])]


def total_match(lst1, lst2):
    return [lst1[i] for i in range(len(lst1)) if sum([len(lst1[i])]+[len(lst2[j]) for j in range(len(lst2))]) <= sum([len(lst2[j])]+[len(lst1[i]) for i in range(len(lst1))])]


def total_match(lst1, lst2):
    return [lst1[i] for i in range(len(lst1)) if sum([len(lst1[i])]+[len(lst2[j]) for j in range(len(lst2))]) <= sum([len(lst2[j])]+[len(lst1[i]) for i in range(len(lst1))])]


def total_match(lst1, lst2):
    return [lst1[i] for i in range(len(lst1)) if sum([len(lst1[i])]+[
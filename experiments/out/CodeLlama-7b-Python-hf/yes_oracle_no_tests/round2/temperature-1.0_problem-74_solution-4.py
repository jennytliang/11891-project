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
    return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2
    
def total_match2(lst1, lst2):
    return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2


def total_match3(lst1, lst2):
    return lst1 if sum(len(s) for s in lst1) < sum(len(s) for s in lst2) else lst2


def total_match4(lst1, lst2):
    return lst1 if sum(len(lst1)) < sum(len(lst2)) else lst2


def total_match5(lst1, lst2):
    return lst1 if sum(map(lambda x: len(x), lst1)) < sum(map(lambda x: len(x), lst2)) else lst2


def total_match6(lst1, lst2):
    return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2


def total_match7(lst1, lst2):
    return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2


def total_match8(lst1, lst2):
    return lst1 if sum(map(lambda x: len(x), lst1)) < sum(map(lambda x: len(x), lst2)) else lst2


def total_match9(lst1, lst2):
    return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2


def total_match10(lst1, lst2):
    return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2


def total_match11(lst1, lst2):
    return lst1 if sum(map(len, lst1)) < sum(map(len, lst2)) else lst2


def total_match12(lst1, lst2):
    return
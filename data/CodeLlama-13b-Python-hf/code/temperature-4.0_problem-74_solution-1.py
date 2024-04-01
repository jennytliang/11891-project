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
    '''
    sum_1 = sum([len(str(x)) for x in lst1])
    x1 = [len(str(x)) for x in lst1]
    sum_2 = sum([len(x) for x in lst2])
    if sum_2 <= sum_1:
        return lst1
    for num in x1:
        # print(len([a for a in lst2 if x1 == a]))
        if num >= len([str(a) for a in lst2 if len(str(a))<= num]):
            return []
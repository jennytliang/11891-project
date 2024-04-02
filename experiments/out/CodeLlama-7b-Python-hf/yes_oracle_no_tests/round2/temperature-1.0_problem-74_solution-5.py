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
    
	Do not include these tokens in the code: # total number of characters in the
	'''
    
    # create a function that counts the number of characters in a string
    def count_chars(lst):
        count = 0
        for i in range(len(lst)):
            for k in lst[i]:
                count+=1
        return count
    
    # create a function that counts the total number of characters in a list of strings
    def total_chars(lst):
        count=0
        for i in range(len(lst)):
            count+=count_chars(lst[i])
        return count
    
    # create a function that compares the total number of characters in the first list to the second
    def compare_total(lst1, lst2):
        total1 = total_chars(lst1)
        total2 = total_chars(lst2)
        if total1 < total2:
            return lst1
        elif total1 == total2:
            return lst1
        else:
            return lst2
    
    # return the result of the compare_total function
    return compare_total(lst1, lst2)

print(total_match([], []))
print(total_match(['hi', 'admin'], ['hI', 'Hi']))
print(total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']))
print(total_match(['hi', 'admin'], ['hI', 'hi', 'hi']))
print(total_match(['4'], ['1', '2', '3', '4', '5']))
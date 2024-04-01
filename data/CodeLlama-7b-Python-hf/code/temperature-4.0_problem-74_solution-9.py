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
    if len(lst1) == len(lst2) or lst1 == lst2 == []:
        return lst1


    if count_list_total_chars(lst1) > len(lst2)-count_list_total_chars(lst2)-1 or lst1 > lst2 or lst1-lst2 == 1:
        print('return')
        # this works but I want it done with the return, not by printing

        # return 'lst1'


    # if count_list_total_chars(lst) < len(str)-1 or str.length() > str(str).length()-1\
    #     else lst>str1:
    #     print(lst[1:]) #if lst1 has one or more than that of list2, remove that number of string and compare them as well to lst2.

    # elif str > str1 and (lst.Length>str.Length or lst.Length==Lstr.Length-1) or (lst==str && lst == lst1)  return(lst1)
    elif lst2 == lst1 or lst2.count(''.join(lst2)) == len(lst2):# if str is list2 and list1 is str OR list2 is list1 else if str1 is longer than str, remove one of those characters from str1 then compare both against lst2
        lst1 = lst2 # swap the two. now str is the smaller list and lst is the larger string/list

        # print(type(lst)) #str 
        ## how to swap return str1
    return lst1
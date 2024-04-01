def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    odd = []
    index = -2
    while index < len(lst)-1:  # checking for duplicates
        if lst[index] in lst[index+1::]:
            for item in lst[index+1:]:
                i = lst[::-1].index(item)
                if item == lst[index]:
                    print("Duplicates found!")
                del(lst[index])
                lst.insert(i, lst.pop(-1))
        index += -1
    for item in lst:   # checks if item has odd num of letters in its string
        if item.isalpha():    # checks whether each string is numeric
            val1 = len(item)
            if val1 == 1:
                continue
            temp = val1 % 2     # check mod
            val2=int(temp)     # convert mod result into int, if its zero, its even num
            val3=int(val1+1) + int(val2)   # val3 is odd num
            if val3 == 1 and val1 > 1:
                print("Odd num word found")
                continue    # skips to for loop if found
        if val3 >= 1:
            continue    # passes to next item in the list
        val = val1.isalpha()    # check if any string is not numerical
    for i in lst:  # appending odd strings into the array odd
        if val:
            if i == lst[lst.index(i)-1]:
                continue
            else:
                print("In odd list")
                print(val)
                val = 0
                odd.append(i)
    lst_copy = lst
    odd.append(odd.pop(-1))  # pops first element, then adds it, so it preserves last element
    for n in lst:    # add odd strings from array lst to lst
        flag = n + ''     # checks whether lst is numeric
        lst_flag = str(lst).isalpha() # checks whether string in the lst is numeric or alphabet
        if flag.isnumeric() and lst_flag != None:    # checking if lst is str and if not, append lst
            lst.append(n+'')    # if list doesn't have string elem, append empty strings then append odd string from array lst to list
        print("List string is", lst)
        if val != None:  # adding strings from odd array to end
            print(val)
    print(lst[0:lst.index(odd[0])])  # printing lst up until the first element of odd arr
    if len(lst) == 1:
        print("List len is one")     # prints lst beginning from second element
        value = lst[1::].clear()     # deletes lst
    for j in lst[lst.index(len(odd[0])):]:  # checking and printing odd lst
        if j == odd[len(odd)]:
            print("lst item at index len", j)
        print(j)
    print(odd)
    return sorted(lst)  # returning sorted list



    lst = ["ccaaa",  "abca",   "dcdcdadcd", "dabc", "a",  "dd"]    # test list

    for n in lst:    # printing test lst
        j = str(lst).isalpha()    # checking whether string is alphanumeric
        if j != None:
            print("TestList string is ", n)
    new_lst_length = len(lst) - 1    # new list with odd items is shorter
    odd_string = []     # odd str arr

    while lst != []: # while lst is still not empty
        if n == lst[new_lst_length]:
            print("lst item ", new_lst_length)  # checking to see if n is at end of list lst
        n = lst.pop(0)      # poping out first item of lst and add it to n
        print(n.pop())      # checking n has been removed from lst then print n which is now lst, should print empty list, as lst.pop was used on whole list

    value = len(lst)-1   # checking for duplicate, using lst.pop removes the whole list, so the length is subtracted by lst.pop and lst is converted to 1
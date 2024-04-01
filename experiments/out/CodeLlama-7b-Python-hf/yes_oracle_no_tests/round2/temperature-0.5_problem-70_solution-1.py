def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list = sorted ( lst )
	'''

    # 🚨 Don't change the code below 👇
    print(sorted(lst))
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇
    # lst = sorted(lst)
    # return lst
    lst = sorted(lst)
    i = 0
    while i < len(lst):
        lst = lst[:i] + [lst[i]] + lst[i+1:]
        lst = lst[:len(lst) - i] + [lst[len(lst) - i]] + lst[len(lst) - i:]
        i += 1
    return lst


# 🚨 Don't change the code below 👇
# test_list = input("Enter list to sort in strange order: ")
test_list = [1, 2, 3, 4]
print("Original list: ", test_list)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

print("Sorted list: ", strange_sort_list(test_list))


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
    
	Include these tokens in the code: from fun ct ools import c mp _ to _
	"""

    lst=list(set(lst))
    def odd_sum(lst):
        for i in range(len(lst)):
            if len(lst[i])%2==1: lst[i]=''
        return lst
    
    odd_lst=odd_sum(lst)
    odd_len=[]
    for i in range(len(odd_lst)):
        if odd_lst[i]=='':
            odd_len.append(len(odd_lst[i]))
    lst.remove('')

    def len_even_sum(lst):
        length=[]
        for i in range(len((lst))):
            length.append(len(lst[i]))
        length.sort()
        temp=[]
        for i in range(len(odd_len)):
            if length.count(odd_len[i])>1:
                while length.count(odd_len[i])>0:
                    temp.append(odd_len[i])
                    length.remove(odd_len[i])

        length+=temp
        return length

    length=len_even_sum(odd_lst)
    odd_lst[odd_lst.index('')]=int('inf') ;delodd=[0] ;lenod=[]
    for i in range(len(odd_lst)):
        if len(odd_lst[i])!=len(odd_lst[len(odd_lst)-1]):
            od=1
    if od==1:
        temp=odd_lst[1]
        for i in range(len(odd_lst)):
            if len(odd_lst[i])<len(temp): odd_lst.insert(i,'')
            elif len(odd_lst[i])>len(temp): odd_lst.insert(i,temp)
    sortedlist=[]
    for i in range(len(length)):
        for j in range(len(odd_lst)):
            if (len(odd_lst[j])==length[i])and(len(odd_lst)%2==0):
                sortedlist.append(odd_lst[j])
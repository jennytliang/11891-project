def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    # your code here
    #return sum([int(y)** 2 for x in lst if -1>-x>9>=0]) if len(lst)>0
    new_list = []

    for a in list(lst)[::]:
        if int(a)%2 != 0 and a>=0:
            for x in range(a):
                a += x ** 2
            return a
        elif a == 0:
            if a == list(set(list(lst)))[0]:
                continue

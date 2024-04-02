def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    
	Include these tokens in the code: s =
	"""
    s = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    return sum(s)




def main():
    print('--------------------Test--------------------')
    print('Add even elements that are at odd indices')
    print('--------------------------------------------')
    s = [4, 2, 6, 7]
    ans = add(s)
    print('s =', s)
    print('ans =', ans)

    print('--------------------------------------------')
    print('Add even elements that are at odd indices')
    print('--------------------------------------------')
    s = [5, 2, 6, 7]
    ans = add(s)
    print('s =', s)
    print('ans =', ans)

    print('--------------------------------------------')
    print('Add even elements that are at odd indices')
    print('--------------------------------------------')
    s = [5, 2, 6, 7, 10]
    ans = add(s)
    print('s =', s)
    print('ans =', ans)

    print('--------------------------------------------')
    print('Add even elements that are at odd indices')
    print('--------------------------------------------')
    s = [5, 2, 6, 7, 10, 12]
    ans = add(s)
    print('s =', s)
    print('ans =', ans)

if __name__ == '__main__':
    main()
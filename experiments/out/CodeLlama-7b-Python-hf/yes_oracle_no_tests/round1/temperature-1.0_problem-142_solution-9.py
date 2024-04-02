def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    
	Include these tokens in the code: ans
	Do not include these tokens in the code: This function will take a list of
	"""

    lst_sqr = []
    lst_cube = []
    i = 1

    for x in lst:
		# print(x)
		if x % i == 0:                 # if an index is a multiple of 3...
			# lst_sqr.append(math.pow(x,2))
			lst_sqr.append(x*x)        # ...square the integer
			# lst_sqr.append(x**2)      #square the integer 
			
		elif x % (i+1) == 0:           # if an index is a multiple of 4...
			lst_cube.append(x**3)      # ...cube the integer
			
		else:
			# lst_sqr.append(x)         
			i += 2                     
 
    print("lst,", lst)
    print(lst_sqr)
    print(lst_cube)
	

    i = 0                              # declare an interger to use as indice
	# for each entry at position i in the list:
    for x in lst_sqr:                  # the function shall square the integer entry if your index is a multiple of 3..
		lst[i] = x
		i = i + 1                      # Add 1 to your indice value, to find the next entry
	
    i = 0
    for x in lst_cube:                 # function will cube the integer entry if its index is a multiple of 4..
		lst[i] = x
		i = i + 1
	
    print("lst_cube:", lst_cube)
    
    print("lst_sqr:", lst_sqr)
    
    print(sum(lst))                    # the function will finally sum all entries.

	# Answer code
    # return sum(lst)
    
sum_squares([1, 2, 3])
    
    
       
    
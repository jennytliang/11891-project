def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Include these tokens in the code: return int ( str ( a )[ - 1 ])
	"""
	# return int ( str ( a )[ - 1 ]) * int ( str ( b )[ - 1 ])
	# return (a%10)*(b%10)
	
	a_dict = {}
	for i in str(a):
		key=int(i)
		if(a_dict.get(key)):
			a_dict[key]+=1    
			#print(a_dict)
		else:
			a_dict[key] = 1
			#print("adding key")
        
    b_dict = {}
	for i in str(b):
		key=int(i)
		if(b_dict.get(key)):
			b_dict[key]+=1    
			#print(b_dict)
		else:
			b_dict[key] = 1
			#print("adding key")

	print(a_dict)
	print(b_dict)
	sum=0
	for i in a_dict.keys():
		for j in b_dict.keys():
			if(i==j):
				sum+=a_dict[i]*b_dict[j]
				print(sum)
	return sum

print(multiply(54,88))

	




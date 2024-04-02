def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    
	Include these tokens in the code: array
	Do not include these tokens in the code: len ( )
	"""

 	if array==[]:                
  		return array      
 	    
 	middleind=len(array)//2
 	if len(array)%2==0:
  		front=sort_array(array[:middleind])
  		back=sort_array(array[middleind:])
  		final = merge(front,back,True)
  		print("The original is ", final, "and the final is ", final)
  		return final 
 		
 		
 		
 	else:
  		front=sort_array(array[:middleind])
  		back=sort_array(array[middleind:])
  		final = merge(front,back,False)
  		return final
  		
def merge(a,b,inorder):
	listt=[]
	i=0
	j=0
	lengtha=len(a)
	lengthb=len(b)
	while i<lengtha and j<lengthb:
		if inorder:
			#print("i= ",i," j= ",j)
			if a[i]<=a[j]:
				#print("i= ",i," j= ",j," a[i] ",a[i]," a[j] ",a[j], "a ", a)
				listt.append(a[i])
				i+=1
			else:
				#print("i= ",i," j= ",j," a[i] ",a[i]," a[j] ",a[j], "a ", a)
				listt.append(b[j])
				j+=1
		else:
			
			if a[i]>=a[j]:
				listt.append(a[i])
				i+=1
			else:
				listt.append(b[j])
				j+=1
				

	while i
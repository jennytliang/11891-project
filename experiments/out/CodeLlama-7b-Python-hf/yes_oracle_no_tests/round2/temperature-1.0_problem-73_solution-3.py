def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    
	Include these tokens in the code: arr _ re vers ed ,
	"""

def compare(A,B):
    if sorted(A)==sorted(B):
        return True
    
    return False

def is_equal(arr1,arr2,i,j):
    len1=len(arr1)
    len2=len(arr2)
    return arr1[i] == arr2[j]





def smallest_change(list):
    result = ''
    for i in range(len(list[:4])):
        print('i: '+ str(i))
        if(list[i]==list[len(list) -i-1]):
            result = result+ ('%(03d)' % {'num':list[i]})
            continue
        
        while (is_equal(list[:4],list,i,len(list) -i-1)):
            print('equal')
            print('result: '+result)
            result = result+ ('%(03d)' % {'num':list[i]})
            #print('result: '+result)
            break

    return ('%03s' % {'num': result})

print(smallest_change([1,2,3,5,4,7,9,6]))    #4
print(smallest_change([1, 2, 3, 4, 3,2, 2]))  #1
print(smallest_change([1, 2, 3, 2, 1]))       #0


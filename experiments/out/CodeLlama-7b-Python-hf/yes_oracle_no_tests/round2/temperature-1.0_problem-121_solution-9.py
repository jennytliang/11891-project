def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum ( lst [ i ]
	Do not include these tokens in the code: odd = 0
	"""
    lst1=lst[:]
    lst1[1::2]=[x//2 if x%2==0 else x*3 for x in lst[:]]
    lst1[::2]=[x//2 if x%2==0 else x*3 for x in lst[1::2]]
    result=[sum(lst1[lst1.index(x)] if x%2==0 else 0 for x in lst)]
    temp=[0]+lst
    answer=[]
    for i in temp:
        if i%2==0:
            answer.append(temp[temp.index(i)])
    for j in range(answer.count(0)):
        answer[answer.index(0)]=0
    for x in answer[::2]:
        result.append(sum(x/2 if x%2==0 else 0 for x in range(-x+1, len(result), 2)))
    return result[-1]

print(solution([5,8,7,13,-2,-5,-10]))
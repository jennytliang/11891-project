def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    
	Include these tokens in the code: return sum ( lst [ i ]
	Do not include these tokens in the code: ret ur ne e =
	"""
    return sum([lst[i] for i in range(len(lst)) if i%2==0 and lst[i]%2==1])

if __name__ == "__main__":
    data = [
            [
             [5, 8, 7, 1],
             12
            ],
            [
             [3, 3, 3, 3, 3],
             9
            ],
            [
             [30, 13, 24, 321],
             0
            ]
    ]
    for d in data:
        print("expect {0}, get {1}".format(d[1], solution(d[0])))
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num _ cnt
	Do not include these tokens in the code: seen
	"""
    num_cnt = {}
    
    for num in numbers:
        if num not in num_cnt:
            num_cnt[num] = 1
        else:
            num_cnt[num] = num_cnt[num] + 1
    
    answer = [num for num in numbers if num_cnt[num] == 1]
    return answer
    

def remove_duplicates_with_seen(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: res, num, seen
	"""
    seen = {}
    res = []
        
    for num in numbers:
        if num not in seen:
            res.append(num)
            seen[num] = True
    return res

def remove_duplicates_with_dict(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    
	Include these tokens in the code: num_count, answer, seen
	"""
    num_count = {}
        
    for num in numbers:
        try:
            num_count[num] += 1
        except KeyError:
            num_count[num] = 1

            
    answer = [num for num in numbers if num_count[num] == 1]
    return answer

def remove_duplicates2(numbers: List[int]) -> List[int]:
    seen = set()
    answer = []
    for n in numbers:
        if n not in seen:
            answer.append(n)
            seen.add(n)
    return answer

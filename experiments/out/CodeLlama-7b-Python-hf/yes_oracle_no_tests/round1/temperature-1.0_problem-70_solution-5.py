def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    
	Include these tokens in the code: sorted _ list = sorted ( lst )
	'''
    # TODO: Add code here
    pass


# 풀이 과정
# def strange_sort_list(lst):
#   if not lst:
#     return lst
#   result = []
#   smallest_value = min(lst)
#   largest_value = max(lst)
#   # print(smallest_value)
#   if smallest_value < largest_value:
#     print(smallest_value)
#     for i in range(len(lst)):
#       if smallest_value == lst[i]:
#         lst.pop(i)
#         result.append(smallest_value)
#     # print(result)
#     # print(largest_value)
#     result = result + [largest_value] + strange_sort_list(lst)
#     return result    
#   else:
#     return result + [smallest_value] + strange_sort_list(lst)

	# 참고: 이 문제는 인터프리터(파이썬 인터프리터)상에서의 strorey의 구조에 의존하는 것을 피하고자 한다.
	# 즉, 거의 모든 list는 []를 이용해서 생성이 가능하며, 이는 sys.getsizeof()가 매우 간단하다.
	# 그리고, 해당 함수를 수행한 결과를 출력한다. 이는 파이썬 인터프리터가 언제나 옳은 자료구조를 가질 때만 가능하다.
	# 따라서 다른 언어로 작성하면 큰 문제가 �
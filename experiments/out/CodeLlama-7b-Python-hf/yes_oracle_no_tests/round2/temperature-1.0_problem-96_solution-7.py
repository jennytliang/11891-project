def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    
	Include these tokens in the code: ans = []
	"""
    
    if n < 1:
        return ans
    ans = []
    tmp = True
    count = 2
    while count <= n:
        if tmp:
            ans.append(count)
            tmp = False
        for num in ans:
            if count % num == 0:
                tmp = True
        count += 1
    print(ans)
    return ans

print(f"[2,3] = {count_up_to(5)}")
print(f"[2,3,5,7] = {count_up_to(11)}")
print(f"[] = {count_up_to(0)}")
print(f"[2,3,5,7,11,13,17,19] = {count_up_to(20)}")
print(f"[] = {count_up_to(1)}")
print(f"[2,3,5,7,11,13,17] = {count_up_to(18)}")

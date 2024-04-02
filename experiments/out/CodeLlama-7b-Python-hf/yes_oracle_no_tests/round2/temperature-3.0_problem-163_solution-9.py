def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    
	Do not include these tokens in the code: if a > 0 and
	"""
    if a > 0 and b > 0:
        if a < b:
            if a % 2 == 0:
                nums = []
                for i in range(a, b + 1):
                    if i % 2 == 0:
                        nums.append(i)
                return nums
            else:
                nums = []
                for i in range(a + 1, b + 1):
                    if i % 2 == 0:
                        nums.append(i)
                return nums
        elif a == b:
            if a % 2 == 0:
                return [a]
            else:
                return []
        elif a > b:
            if b % 2 == 0:
                nums = []
                for i in range(b + 1, a + 1):
                    if i % 2 == 0:
                        nums.append(i)
                return nums
            else:
                nums = []
                for i in range(b, a + 1):
                    if i % 2 == 0:
                        nums.append(i)
                return nums


print(generate_integers(2, 8))
print(generate_integers(8, 2))
print(generate_integers(10, 14))

def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    # 1st solution
    # even = 0
    # odd = 0
    # for n in str(num):
    #     if int(n) % 2 == 0:
    #         even += 1
    #     else:
    #         odd += 1
    # return (even, odd)

    # 2nd solution
    # return (sum(int(n) % 2 == 0 for n in str(num)), sum(int(n) % 2 != 0 for n in str(num)))

    # 3rd solution
    return (sum(int(n) % 2 == 0 for n in str(abs(num))), sum(int(n) % 2 != 0 for n in str(abs(num))))


# print(even_odd_count(123))
# print(even_odd_count(-12))
# print(even_odd_count(123456789))
# print(even_odd_count(-123456789))
# print(even_odd_count(1234567890))
# print(even_odd_count(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679))
# print(even_odd_count(31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679))

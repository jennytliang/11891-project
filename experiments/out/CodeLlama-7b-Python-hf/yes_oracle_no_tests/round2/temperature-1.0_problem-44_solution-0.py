def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    
	Include these tokens in the code: "
	Do not include these tokens in the code: '
	"""


    if x == 0:
        return '0'
    else:
        return change_base(x // base, base) + str(x % base)








print(change_base(3, 2))
print(change_base(8, 3))
print(change_base(8, 2))
print(change_base(7, 2))

# print(change_base(100, 2))
# print(change_base(100, 3))
# print(change_base(100, 4))
# print(change_base(100, 5))
# print(change_base(100, 6))
# print(change_base(100, 7))
# print(change_base(100, 8))
# print(change_base(100, 9))
# print(change_base(100, 10))
# print(change_base(100, 11))
# print(change_base(100, 12))
# print(change_base(100, 13))
# print(change_base(100, 14))
# print(change_base(100, 15))
# print(change_base(100, 16))
# print(change_base(100, 17))
# print(change_base(100, 18))
# print(change_base(100, 19))
# print(change_base(100, 20))
# print(change_base(100, 21))
# print(change_base(100, 22))
# print(change_base(100, 23))
# print(change_base(100, 24))
# print(change_base(100, 25))
# print(change_base(100, 26))
# print(change_base(100, 27))
# print(change_
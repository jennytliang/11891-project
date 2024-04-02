def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    
	Include these tokens in the code: num _ a = float ( str
	Do not include these tokens in the code: if is instance
	"""
    
    try:
        tmp = float()
        tmp = float(str(a).strip().replace(",", "."))
    except:
        pass
    
    try:
        tmp = float(b)
    except:
        pass

    test = tmp > float(a)
    test += tmp > float(b)
    ret_val = tmp if test else None

    return ret_val


if __name__ == '__main__':
	#Example Test Case of Question
	print("Example:")
	#>>>>> Test Case, Expected Outcome
	print(compare_one(1,2)) #>>>>> 2
	print(compare_one(2,1)) #>>>>> 2
	print(compare_one(1,1)) #>>>>> None
	print(compare_one(1.1, 1.2)) #>>>>> 1.2
	print(compare_one("123", "23")) #>>>>> "123"
	print(compare_one("1.2","1,2")) #>>>>> "1.2"
	print(compare_one("1", b=1)) #>>>>> None

	print(compare_one(b=1, a=1)) #>>>>> None
	
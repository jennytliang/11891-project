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
    
	Do not include these tokens in the code: try : return
	"""
    A,B=str(a),str(b)
    if (A.count(".") > 0) or (B.count(".") > 0):
      A = A.replace(".", "")
      B = B.replace(".", "")
    if (B.count(",") > 0) or (A.count(",") > 0):
      B = B.replace(",", "")
      A = A.replace(",", "")

    if int(A) > int(B): return A
    elif int(A) == int(B): return None
    else: return B
      
#compare_one(1, 2.5) #➞ 2.5
#compare_one(1, "2,3") #➞ "2,3"
#compare_one("5,1", "6") #➞ "6"
#compare_one("1", 1) #➞ None
#compare_one(6, "9,5") ➞ "9,5"
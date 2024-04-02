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
    
	Include these tokens in the code: num _ a = float ( str ( a ).
	"""
    a,b=str(a),str(b)
    if a==b:
        return
    if float(a)>float(b):
        return a
    else:
        return b
    
def compare_one_soln(a,b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    
	Include these tokens in the code: num _ a = float ( str ( a ).
	"""
    a,b = str(a),str(b)
    if a==b:
        return
    if a.replace(".", "").replace(",", ".").isdigit() and b.replace(".", "").replace(",", ".").isdigit():
        if float(a)>float(b):
            return a
        else:
            return b
    else:
        if a.replace(",", ".").isdigit() and b.replace(",", ".").isdigit():
            if float(a)>float(b):
                return a
            else:
                return b
        else:
            return
            
def compare_one_soln_2(a,b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,
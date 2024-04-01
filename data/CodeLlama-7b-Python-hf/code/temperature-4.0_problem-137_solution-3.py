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
    """
    

    # If a and b are int
    a_int = False
    b_int = False
    if isinstance(a, int):
        a_int = True
        a = str(a).replace(",","")
    
    if isinstance(b, int):
        b_int = True
        b = str(b).replace(",","")


    f = True

    # If numbers are not a real numbers
    # print(f"a {type(a)} , a_int {type(float(a))} {bool(a_real)} a {bool(float('',))}")
    if a.find('.') == -1 and b.find('.') == -1 :
        if any([a=="0", a=="1"]):
            print(a)
            print(f"a_int2 {a_int}, b  {b} ")
            print(isinstance(int(a), type(float(b))))
            if any([b.find("0"), b == "1"]):
        #        print("c")
                if a_int or b_int:
                    if a == str(int(b)).replace(".", ""):
                        return b
                else:

                    if a.split("/")[0][a.find(".", )] != str((int(b)))[a.split("/", a.count("/"))[a.last_i_ndex("/")]])

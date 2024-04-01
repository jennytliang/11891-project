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
    # Convert both numbers to floats. If the second value is a string and cannot be converted,
    # it will return NaN, which will cause the original comparison to return false, as the
    # original value is obviously greater.

    # If the first value is less than the second, convert the first value to the data type
    # that is in the second (string, int, or float)

    # If the second values less that the first, return first
    # If the values are equal, return NaN

    if type(a) == int:
        type1 = int
    elif type(a) == float and type(a) == float or not type(a) == float and '.' in str(b) and "," in str(b): # If b contains a decimal point but not a comma, a string (b) was given. If a contains one and b has a comma and b is an int (but not decimal), return an int. If they have decimals/commas in common, convert to string (and return string, as a string will return as NaN if b is equal or greater)
        b = float(b.replace(",", ".")) #Convert to floats so that the comparisons in the except clause will work, but will still return the correct type for the values
        if str(b).count(",") >= 1:
            type1 = lambda bval: bval.replace(".", ",") #Convert value to original type (given)
        elif str(b).count(",") == 0:
            type1 = float
        elif isinstance(b, float):
            typeb = float #Return a float, as the numbers were originally floats.
        else: #If both numbers were ints but with commas separating the digits, return a string with the comma decimal points
            type1 = lambda abval: str(abval).replace(".", ",")

    elif isinstance(a, float):
        type1 = float

    if a > b or a == b :
        return NaN
    else:
        return type1(max(b, a)) #max returns the number with the biggest number, while also keeping the data type. If the first number in the arguments is returned, the returned val will have b's type, else will keep a's type



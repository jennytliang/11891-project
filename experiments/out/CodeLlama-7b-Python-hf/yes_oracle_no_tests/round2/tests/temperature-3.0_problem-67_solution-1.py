def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    
	Do not include these tokens in the code: # your code goes here
	"""
    # Your code goes here
    a = s.split()
    a = [int(i) for i in a]
    return n - a[0] - a[1]


fruit_distribution("5 apples and 6 oranges", 19)




import numpy as np

def is_floats(x) -> bool:
    # check if it is float; List[float]; Tuple[float]
    if isinstance(x, float):
        return True
    if isinstance(x, (list, tuple)):
        return all(isinstance(i, float) for i in x)
    if isinstance(x, np.ndarray):
        return x.dtype == np.float64 or x.dtype == np.float32
    return False


def assertion(out, exp, atol):
    exact_match = out == exp

    if atol == 0 and is_floats(exp):
        atol = 1e-6
    if not exact_match and atol != 0:
        np.testing.assert_allclose(out, exp, atol=atol)
    else:
        assert exact_match


def check(candidate):
    inputs = [['5 apples and 6 oranges', 19], ['5 apples and 6 oranges', 21], ['0 apples and 1 oranges', 3], ['1 apples and 0 oranges', 3], ['2 apples and 3 oranges', 100], ['2 apples and 3 oranges', 5], ['1 apples and 100 oranges', 120], ['10 apples and 20 oranges', 50], ['3 apples and 4 oranges', 9], ['7 apples and 8 oranges', 30], ['2 apples and 0 oranges', 5], ['0 apples and 0 oranges', 10], ['0 apples and 1 oranges', 1], ['10 apples and 0 oranges', 15], ['3 apples and 5 oranges', 12], ['5 apples and 5 oranges', 12], ['8 apples and 2 oranges', 15], ['2 apples and 0 oranges', 12], ['2 apples and 0 oranges', 30], ['0 apples and 0 oranges', 9], ['0 apples and 1 oranges', 50], ['0 apples and 1 oranges', 15], ['0 apples and 1 oranges', 14], ['0 apples and 0 oranges', 30], ['0 apples and 1 oranges', 10], ['0 apples and 1 oranges', 12], ['10 apples and 20 oranges', 30], ['2 apples and 0 oranges', 13], ['3 apples and 4 oranges', 30], ['8 apples and 2 oranges', 10], ['0 apples and 1 oranges', 2], ['10 apples and 20 oranges', 51], ['3 apples and 5 oranges', 10], ['5 apples and 5 oranges', 15], ['0 apples and 1 oranges', 9], ['0 apples and 1 oranges', 8], ['0 apples and 1 oranges', 13], ['0 apples and 0 oranges', 1], ['7 apples and 8 oranges', 15], ['3 apples and 5 oranges', 51], ['3 apples and 4 oranges', 8], ['3 apples and 5 oranges', 13], ['0 apples and 1 oranges', 51], ['2 apples and 0 oranges', 11], ['10 apples and 0 oranges', 30], ['2 apples and 0 oranges', 14], ['0 apples and 0 oranges', 29], ['10 apples and 20 oranges', 52], ['0 apples and 1 oranges', 4], ['2 apples and 0 oranges', 50], ['2 apples and 0 oranges', 51], ['0 apples and 1 oranges', 11], ['5 apples and 5 oranges', 11], ['2 apples and 0 oranges', 52], ['3 apples and 4 oranges', 12], ['3 apples and 4 oranges', 10], ['10 apples and 0 oranges', 29], ['2 apples and 0 oranges', 3], ['2 apples and 0 oranges', 6], ['3 apples and 5 oranges', 9], ['2 apples and 0 oranges', 29], ['2 apples and 0 oranges', 8], ['0 apples and 0 oranges', 12], ['2 apples and 0 oranges', 10], ['3 apples and 5 oranges', 14], ['2 apples and 0 oranges', 9], ['5 apples and 5 oranges', 13], ['0 apples and 0 oranges', 15], ['3 apples and 4 oranges', 13], ['0 apples and 0 oranges', 14], ['0 apples and 0 oranges', 0], ['3 apples and 4 oranges', 50], ['2 apples and 0 oranges', 15], ['10 apples and 5 oranges', 20], ['3 apples and 7 oranges', 15], ['15 apples and 8 oranges', 30], ['24 apples and 18 oranges', 50], ['50 apples and 50 oranges', 100], ['100 apples and 100 oranges', 200], ['1 apples and 99 oranges', 105], ['99 apples and 1 oranges', 105], ['20 apples and 0 oranges', 25], ['1 apples and 99 oranges', 100], ['99 apples and 1 oranges', 104], ['20 apples and 0 oranges', 199], ['50 apples and 50 oranges', 199], ['1 apples and 99 oranges', 199], ['50 apples and 50 oranges', 200], ['20 apples and 0 oranges', 198], ['24 apples and 18 oranges', 105], ['24 apples and 18 oranges', 100], ['99 apples and 1 oranges', 106], ['3 apples and 7 oranges', 20], ['3 apples and 7 oranges', 25], ['1 apples and 99 oranges', 104], ['97 apples and 1 oranges', 198], ['97 apples and 1 oranges', 105], ['20 apples and 0 oranges', 26], ['3 apples and 7 oranges', 198], ['50 apples and 50 oranges', 105], ['20 apples and 0 oranges', 197], ['50 apples and 50 oranges', 106], ['50 apples and 50 oranges', 104], ['15 apples and 8 oranges', 198], ['0 apples and 0 oranges', 11], ['24 apples and 18 oranges', 106], ['1 apples and 99 oranges', 103], ['99 apples and 1 oranges', 103], ['1 apples and 99 oranges', 197], ['99 apples and 1 oranges', 198], ['97 apples and 1 oranges', 200], ['50 apples and 50 oranges', 103], ['0 apples and 0 oranges', 199], ['15 apples and 8 oranges', 26], ['24 apples and 18 oranges', 49], ['15 apples and 8 oranges', 106], ['20 apples and 0 oranges', 99], ['99 apples and 1 oranges', 197], ['3 apples and 7 oranges', 21], ['3 apples and 7 oranges', 103], ['3 apples and 7 oranges', 101], ['24 apples and 18 oranges', 51], ['100 apples and 100 oranges', 201], ['20 apples and 0 oranges', 50], ['99 apples and 1 oranges', 199], ['20 apples and 0 oranges', 200], ['0 apples and 0 oranges', 106], ['97 apples and 1 oranges', 199], ['3 apples and 7 oranges', 16], ['20 apples and 0 oranges', 27], ['50 apples and 50 oranges', 101], ['97 apples and 1 oranges', 100], ['1 apples and 99 oranges', 106], ['0 apples and 0 oranges', 197], ['20 apples and 0 oranges', 107], ['10 apples and 5 oranges', 21], ['1 apples and 99 oranges', 196], ['24 apples and 18 oranges', 104], ['99 apples and 1 oranges', 102], ['20 apples and 0 oranges', 30], ['1 apples and 99 oranges', 101], ['97 apples and 1 oranges', 107], ['50 apples and 50 oranges', 102], ['24 apples and 18 oranges', 99], ['15 apples and 8 oranges', 197], ['97 apples and 1 oranges', 201], ['15 apples and 8 oranges', 105], ['15 apples and 8 oranges', 100], ['15 apples and 8 oranges', 28], ['0 apples and 0 oranges', 198], ['0 apples and 0 oranges', 50], ['24 apples and 118 oranges', 198], ['97 apples and 1 oranges', 103], ['10 apples and 5 oranges', 51], ['20 apples and 0 oranges', 104], ['24 apples and 118 oranges', 199], ['20 apples and 0 oranges', 31], ['15 apples and 8 oranges', 107], ['10 apples and 5 oranges', 30], ['3 apples and 7 oranges', 106], ['20 apples and 0 oranges', 106], ['24 apples and 18 oranges', 48], ['20 apples and 0 oranges', 48], ['1 apples and 99 oranges', 107], ['20 apples and 0 oranges', 101], ['0 apples and 0 oranges', 200], ['15 apples and 8 oranges', 49], ['1 apples and 99 oranges', 198], ['50 apples and 50 oranges', 197], ['10 apples and 5 oranges', 199], ['3 apples and 7 oranges', 197], ['20 apples and 0 oranges', 196], ['3 apples and 7 oranges', 12], ['3 apples and 7 oranges', 26], ['0 apples and 0 oranges', 25], ['3 apples and 7 oranges', 10], ['15 apples and 8 oranges', 199], ['99 apples and 1 oranges', 101], ['10 apples and 5 oranges', 15], ['15 apples and 8 oranges', 196], ['3 apples and 7 oranges', 22], ['97 apples and 1 oranges', 104], ['24 apples and 118 oranges', 196], ['1 apples and 99 oranges', 102], ['97 apples and 1 oranges', 196], ['24 apples and 18 oranges', 98], ['20 apples and 0 oranges', 105], ['20 apples and 0 oranges', 102], ['99 apples and 1 oranges', 200], ['24 apples and 11 oranges', 49], ['97 apples and 1 oranges', 197], ['24 apples and 118 oranges', 197], ['20 apples and 0 oranges', 28], ['0 apples and 0 oranges', 49], ['0 apples and 0 oranges', 99], ['20 apples and 0 oranges', 201], ['3 apples and 7 oranges', 105], ['10 apples and 5 oranges', 28], ['3 apples and 7 oranges', 27], ['3 apples and 7 oranges', 28], ['15 apples and 8 oranges', 104], ['24 apples and 18 oranges', 199], ['15 apples and 8 oranges', 48], ['0 apples and 0 oranges', 20], ['24 apples and 18 oranges', 196], ['24 apples and 18 oranges', 195], ['24 apples and 18 oranges', 103], ['15 apples and 8 oranges', 99], ['3 apples and 7 oranges', 104], ['10 apples and 5 oranges', 27], ['24 apples and 18 oranges', 97], ['99 apples and 1 oranges', 196], ['10 apples and 5 oranges', 101], ['15 apples and 8 oranges', 103], ['24 apples and 11 oranges', 107], ['15 apples and 8 oranges', 108], ['50 apples and 50 oranges', 201], ['10 apples and 5 oranges', 29], ['0 apples and 0 oranges', 105], ['0 apples and 0 oranges', 104], ['10 apples and 5 oranges', 105], ['3 apples and 7 oranges', 17], ['3 apples and 7 oranges', 14], ['10 apples and 5 oranges', 104], ['3 apples and 7 oranges', 29], ['1 apples and 9 oranges', 105], ['15 apples and 8 oranges', 31], ['1 apples and 9 oranges', 31], ['0 apples and 0 oranges', 100], ['3 apples and 7 oranges', 99], ['15 apples and 8 oranges', 32], ['1 apples and 9 oranges', 104], ['1 apples and 9 oranges', 28], ['1 apples and 9 oranges', 49], ['10 apples and 5 oranges', 106], ['3 apples and 7 oranges', 31], ['0 apples and 0 oranges', 31], ['1 apples and 9 oranges', 29], ['0 apples and 0 oranges', 28], ['10 apples and 5 oranges', 19], ['1 apples and 9 oranges', 50], ['99 apples and 1 oranges', 201], ['10 apples and 5 oranges', 22], ['3 apples and 7 oranges', 18], ['1 apples and 9 oranges', 27], ['20 apples and 0 oranges', 100], ['0 apples and 0 oranges', 17], ['0 apples and 0 oranges', 101], ['1 apples and 9 oranges', 14], ['1 apples and 9 oranges', 11], ['0 apples and 0 oranges', 22], ['1 apples and 9 oranges', 101], ['91 apples and 9 oranges', 105], ['10 apples and 5 oranges', 25], ['0 apples and 0 oranges', 16], ['1 apples and 9 oranges', 103], ['3 apples and 7 oranges', 19], ['03 apples and 7 oranges', 19], ['1 apples and 9 oranges', 20], ['10 apples and 5 oranges', 31], ['10 apples and 5 oranges', 16], ['3 apples and 7 oranges', 30], ['0 apples and 0 oranges', 18], ['1 apples and 9 oranges', 26], ['0 apples and 0 oranges', 103], ['1 apples and 9 oranges', 21], ['0 apples and 018 oranges', 103], ['50 apples and 50 oranges', 202], ['10 apples and 5 oranges', 48], ['1 apples and 9 oranges', 10], ['1 apples and 9 oranges', 22], ['10 apples and 5 oranges', 50], ['0 apples and 018 oranges', 105], ['0 apples and 0 oranges', 107], ['0 apples and 018 oranges', 201], ['1 apples and 9 oranges', 19], ['15 apples and 8 oranges', 27], ['1 apples and 9 oranges', 25], ['10 apples and 5 oranges', 18], ['03 apples and 7 oranges', 21], ['10 apples and 5 oranges', 202], ['0 apples and 0 oranges', 13], ['1 apples and 9 oranges', 15], ['0 apples and 0 oranges', 21], ['20 apples and 0 oranges', 29], ['0 apples and 018 oranges', 200], ['0 apples and 018 oranges', 49], ['1 apples and 9 oranges', 201], ['0 apples and 0 oranges', 102], ['0 apples and 018 oranges', 99], ['91 apples and 9 oranges', 103], ['0 apples and 018 oranges', 100], ['99 apples and 1 oranges', 107], ['03 apples and 7 oranges', 20], ['1 apples and 9 oranges', 32], ['0 apples and 018 oranges', 106], ['1 apples and 9 oranges', 13], ['3 apples and 7 oranges', 107], ['15 apples and 8 oranges', 29], ['0 apples and 0 oranges', 48], ['10 apples and 5 oranges', 99], ['03 apples and 7 oranges', 100], ['99 apples and 1 oranges', 108], ['10 apples and 5 oranges', 26], ['91 apples and 9 oranges', 106], ['3 apples and 7 oranges', 202], ['03 apples and 7 oranges', 51], ['0 apples and 018 oranges', 104], ['03 apples and 7 oranges', 18], ['50 apples and 50 oranges', 107], ['10 apples and 5 oranges', 200], ['1 apples and 9 oranges', 12], ['0 apples and 0 oranges', 19], ['1 apples and 9 oranges', 200], ['1 apples and 9 oranges', 18], ['03 apples and 7 oranges', 99], ['1 apples and 9 oranges', 100], ['1 apples and 9 oranges', 48], ['10 apples and 5 oranges', 100], ['91 apples and 9 oranges', 100], ['03 apples and 7 oranges', 98], ['3 apples and 78 oranges', 202], ['03 apples and 7 oranges', 28], ['03 apples and 7 oranges', 52], ['10 apples and 5 oranges', 49], ['03 apples and 7 oranges', 97], ['3 apples and 7 oranges', 51], ['99 apples and 1 oranges', 202], ['0 apples and 0 oranges', 52], ['3 apples and 78 oranges', 99], ['10 apples and 5 oranges', 103], ['15 apples and 8 oranges', 202], ['0 apples and 018 oranges', 20], ['1 apples and 9 oranges', 17], ['020 apples and 018 oranges', 49], ['1 apples and 9 oranges', 99], ['10 apples and 5 oranges', 52], ['03 apples and 7 oranges', 103], ['10 apples and 5 oranges', 17], ['3 apples and 7 oranges', 108], ['3 apples and 7 oranges', 49], ['1 apples and 9 oranges', 16], ['03 apples and 7 oranges', 201], ['1 apples and 9 oranges', 199], ['1 apples and 9 oranges', 30], ['1 apples and 9 oranges', 202], ['100 apples and 100 oranges', 202]]
    results = [8, 10, 2, 2, 95, 0, 19, 20, 2, 15, 3, 10, 0, 5, 4, 2, 5, 10, 28, 9, 49, 14, 13, 30, 9, 11, 0, 11, 23, 0, 1, 21, 2, 5, 8, 7, 12, 1, 0, 43, 1, 5, 50, 9, 20, 12, 29, 22, 3, 48, 49, 10, 1, 50, 5, 3, 19, 1, 4, 1, 27, 6, 12, 8, 6, 7, 3, 15, 6, 14, 0, 43, 13, 5, 5, 7, 8, 0, 0, 5, 5, 5, 0, 4, 179, 99, 99, 100, 178, 63, 58, 6, 10, 15, 4, 100, 7, 6, 188, 5, 177, 6, 4, 175, 11, 64, 3, 3, 97, 98, 102, 3, 199, 3, 7, 83, 79, 97, 11, 93, 91, 9, 1, 30, 99, 180, 106, 101, 6, 7, 1, 2, 6, 197, 87, 6, 96, 62, 2, 10, 1, 9, 2, 57, 174, 103, 82, 77, 5, 198, 50, 56, 5, 36, 84, 57, 11, 84, 15, 96, 86, 6, 28, 7, 81, 200, 26, 98, 97, 184, 187, 176, 2, 16, 25, 0, 176, 1, 0, 173, 12, 6, 54, 2, 98, 56, 85, 82, 100, 14, 99, 55, 8, 49, 99, 181, 95, 13, 17, 18, 81, 157, 25, 20, 154, 153, 61, 76, 94, 12, 55, 96, 86, 80, 72, 85, 101, 14, 105, 104, 90, 7, 4, 89, 19, 95, 8, 21, 100, 89, 9, 94, 18, 39, 91, 21, 31, 19, 28, 4, 40, 101, 7, 8, 17, 80, 17, 101, 4, 1, 22, 91, 5, 10, 16, 93, 9, 9, 10, 16, 1, 20, 18, 16, 103, 11, 85, 102, 33, 0, 12, 35, 87, 107, 183, 9, 4, 15, 3, 11, 187, 13, 5, 21, 9, 182, 31, 191, 102, 81, 3, 82, 7, 10, 22, 88, 3, 97, 6, 48, 84, 90, 8, 11, 6, 192, 41, 86, 8, 7, 185, 2, 19, 190, 8, 89, 90, 38, 85, 0, 88, 121, 18, 42, 34, 87, 41, 102, 52, 18, 88, 179, 2, 7, 11, 89, 37, 93, 2, 98, 39, 6, 191, 189, 20, 192, 2]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(fruit_distribution)
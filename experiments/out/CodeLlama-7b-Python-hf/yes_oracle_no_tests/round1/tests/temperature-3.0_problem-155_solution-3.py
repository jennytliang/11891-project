def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    
    if num < 0:
        num = -num
    
    while num > 0:
        if num % 10 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10
    
    return (even, odd)


#Pybites solution

def even_odd_count1(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    
	Include these tokens in the code: even , odd =
	"""
    even = 0
    odd = 0
    num = abs(num)
    while num > 0:
        if num % 10:
            odd += 1
        else:
            even += 1
        num = num // 10
    return even, odd




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
    inputs = [[7], [-78], [3452], [346211], [-345821], [-2], [-45347], [0], [2368], [-111], [-2468031], [1010101], [-123456789], [-590], [125890], [444444444], [-1111111], [-222222222], [-591], [444444443], [444444445], [-222222221], [-1111110], [-592], [-222222224], [-222222223], [-7], [2369], [-2468032], [-112], [125889], [-589], [-588], [-123456790], [-593], [-2468033], [-222222225], [-222222226], [2367], [-110], [-113], [444444442], [1010100], [-114], [-67], [-586], [-1111112], [1010099], [1010098], [-222222227], [-2468034], [-123456791], [2366], [-9], [-123456792], [-587], [-1111113], [-2468035], [444444446], [11], [-222222220], [444444447], [-109], [-6], [-585], [125891], [-93], [-10], [12], [125888], [-115], [125892], [13], [-48], [37], [-97], [-94], [-92], [-98], [-11], [-1], [36], [2370], [14], [-1111109], [15], [-222222228], [-123456793], [34], [-16], [35], [10], [-68], [444444441], [-1111114], [-69], [-222222229], [444444440], [-15], [444444439], [33], [-5], [-2468036], [-1111115], [-53], [-358947934856], [54837398243239], [-78653034582], [-1021021021021021021021021021021021021021021021021], [-923456789], [9876543210], [246813579], [-1234567890987654321], [11111], [-2222], [54837398243240], [-923456790], [11112], [-358947934857], [-1234567890987654320], [-923456792], [-2221], [-1021021021021021021021021021021021021021021021020], [-2219], [54837398243238], [-70], [-71], [11110], [-2223], [-1021021021021021021021021021021021021021021021019], [-18], [-358947934858], [-2220], [-1021021021021021021021021021021021021021021021018], [-923456788], [3], [-1234567890987654322], [-17], [-78653034583], [54837398243241], [246813578], [-1021021021021021021021021021021021021021021021022], [-85], [-923456793], [-78653034584], [11109], [-8], [-59], [-19], [-66], [-923456794], [-923456787], [-58], [-923456785], [-2218], [9876543211], [-80], [46], [-358947934855], [-60], [-81], [4], [-1234567890987654323], [246813577], [-12], [-923456786], [-1021021021021021021021021021021021021021021021017], [-358947934854], [11107], [19], [5], [9876543212], [-1021021021021021021021021021021021021021021021016], [54837398243242], [-61], [-14], [18], [-1021021021021021021021021021021021021021021021015], [11106], [-13], [20], [-56], [-923456795], [11108], [-1021021021021021021021021021021021021021021021023], [17], [2], [-923456784], [-65], [1], [54837398243243], [89], [-64], [-82], [-63], [64], [11105], [90], [-358947934859], [99], [65], [11104], [11113], [-83], [6], [-62], [9876543213], [53], [-84], [-2224], [66], [11103], [-358947934853], [-86], [67], [-35], [-1021021021021021021021021021021021021021021021013], [-2217], [-2216], [9876543215], [-923456783], [-3], [-57], [-77777777777777777777], [22222222222], [-33], [13579], [-2468], [2147483647], [11111111111111111111], [-11111111111111111111], [-2147483648], [9876543209], [9876543208], [246813580], [246813581], [-1234567890987654319], [16], [78], [77], [76], [-78653034581], [-1234567890987654318], [75], [-2225], [58], [-78653034585], [246813576], [39], [246813583], [-1234567890987654324], [38], [48], [-21], [40]]
    results = [(0, 1), (1, 1), (2, 2), (3, 3), (3, 3), (1, 0), (2, 3), (1, 0), (3, 1), (0, 3), (5, 2), (3, 4), (4, 5), (1, 2), (3, 3), (9, 0), (0, 7), (9, 0), (0, 3), (8, 1), (8, 1), (8, 1), (1, 6), (1, 2), (9, 0), (8, 1), (0, 1), (2, 2), (6, 1), (1, 2), (3, 3), (1, 2), (2, 1), (4, 5), (0, 3), (5, 2), (8, 1), (9, 0), (2, 2), (1, 2), (0, 3), (9, 0), (4, 3), (1, 2), (1, 1), (2, 1), (1, 6), (3, 4), (4, 3), (8, 1), (6, 1), (3, 6), (3, 1), (0, 1), (4, 5), (1, 2), (0, 7), (5, 2), (9, 0), (0, 2), (9, 0), (8, 1), (1, 2), (1, 0), (1, 2), (2, 4), (0, 2), (1, 1), (1, 1), (4, 2), (0, 3), (3, 3), (0, 2), (2, 0), (0, 2), (0, 2), (1, 1), (1, 1), (1, 1), (0, 2), (0, 1), (1, 1), (2, 2), (1, 1), (1, 6), (0, 2), (9, 0), (3, 6), (1, 1), (1, 1), (0, 2), (1, 1), (2, 0), (8, 1), (1, 6), (1, 1), (8, 1), (9, 0), (0, 2), (7, 2), (0, 2), (0, 1), (6, 1), (0, 7), (0, 2), (5, 7), (6, 8), (6, 5), (32, 17), (4, 5), (5, 5), (4, 5), (9, 10), (0, 5), (4, 0), (8, 6), (4, 5), (1, 4), (4, 8), (10, 9), (4, 5), (3, 1), (33, 16), (2, 2), (7, 7), (1, 1), (0, 2), (1, 4), (3, 1), (31, 18), (1, 1), (5, 7), (4, 0), (32, 17), (5, 4), (0, 1), (10, 9), (0, 2), (5, 6), (7, 7), (5, 4), (33, 16), (1, 1), (3, 6), (6, 5), (1, 4), (1, 0), (0, 2), (0, 2), (2, 0), (4, 5), (4, 5), (1, 1), (4, 5), (3, 1), (4, 6), (2, 0), (2, 0), (4, 8), (2, 0), (1, 1), (1, 0), (9, 10), (4, 5), (1, 1), (5, 4), (31, 18), (5, 7), (1, 4), (0, 2), (0, 1), (5, 5), (32, 17), (8, 6), (1, 1), (1, 1), (1, 1), (31, 18), (2, 3), (0, 2), (2, 0), (1, 1), (3, 6), (2, 3), (32, 17), (0, 2), (1, 0), (5, 4), (1, 1), (0, 1), (7, 7), (1, 1), (2, 0), (2, 0), (1, 1), (2, 0), (1, 4), (1, 1), (4, 8), (0, 2), (1, 1), (2, 3), (0, 5), (1, 1), (1, 0), (2, 0), (4, 6), (0, 2), (2, 0), (4, 0), (2, 0), (1, 4), (4, 8), (2, 0), (1, 1), (0, 2), (31, 18), (2, 2), (3, 1), (4, 6), (4, 5), (0, 1), (0, 2), (0, 20), (11, 0), (0, 2), (0, 5), (4, 0), (6, 4), (0, 20), (0, 20), (7, 3), (5, 5), (6, 4), (6, 3), (5, 4), (8, 11), (1, 1), (1, 1), (0, 2), (1, 1), (5, 6), (9, 10), (0, 2), (3, 1), (1, 1), (5, 6), (5, 4), (0, 2), (5, 4), (10, 9), (1, 1), (2, 0), (1, 1), (2, 0)]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(even_odd_count)
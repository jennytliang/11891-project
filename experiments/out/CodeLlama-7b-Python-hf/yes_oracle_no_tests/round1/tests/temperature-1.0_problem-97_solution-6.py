def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    
	Include these tokens in the code: return int ( str ( a )[ - 1 ])
	"""
    return int(str(a)[-1]) * int(str(b)[-1])



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
    inputs = [[148, 412], [19, 28], [2020, 1851], [14, -15], [76, 67], [17, 27], [0, 1], [0, 0], [-6, -9], [-87, 5], [39, 25], [1, 100], [-15, -12], [-5, 9], [-12, -16], [0, 8], [8, 0], [123, 321], [-6, -5], [-9, 0], [8, 8], [-87, -87], [123, -12], [5, 25], [1, 0], [1, -16], [125, 124], [-6, -4], [123, 5], [8, -9], [124, 100], [-7, -9], [-7, -6], [8, -16], [8, -10], [0, -7], [-15, -6], [-86, -87], [-15, -7], [0, -9], [1, 1], [9, 25], [5, -5], [-12, -12], [-8, -9], [-5, 8], [125, 125], [-16, 5], [-11, -12], [-4, -4], [-12, -13], [-86, -86], [124, 99], [-4, -5], [5, 8], [123, 123], [-9, -9], [5, 100], [-5, -4], [-16, -16], [100, 99], [-15, -15], [-87, -86], [8, -4], [25, -9], [-15, 8], [-9, -10], [8, -8], [0, -6], [124, 124], [-8, -10], [1, 6], [-9, -5], [-6, -8], [9, 9], [-12, 0], [9, 5], [-5, -5], [100, 100], [-86, -12], [123, -8], [125, -6], [124, 98], [5, -86], [-13, -4], [-86, 5], [123, -3], [-15, -11], [5, 5], [25, 8], [-87, 321], [-86, 100], [9, -16], [5, 123], [9, -12], [-9, 99], [124, -7], [124, 8], [5, -15], [-17, -16], [-5, -3], [-17, -87], [-17, 1], [124, -8], [-8, -86], [-10, -10], [-17, 3], [1234567890, 9876543210], [-9876543210, 1234567890], [1092387465, 2938475610], [246813579, -975312468], [-99, -99], [-12345, 6789], [987654, -123457], [-987654, -123457], [1234567890, 1234567890], [1092387465, 2938475609], [6789, 6789], [1234567890, 9876543211], [2938475610, 6789], [-987654, -987654], [1092387465, 987654], [-16, -17], [6787, 6788], [987655, -123457], [2938475609, 3], [-16, -99], [-987655, -987654], [3, 2938475610], [-17, 2], [-9876543210, -987654], [2, -123457], [987654, 987654], [-99, -17], [2938475611, 6789], [-99, 987654], [-987655, -99], [-17, -17], [-975312468, 1234567892], [2938475610, -975312468], [2, -99], [6790, 6789], [2938475610, 2938475609], [-123457, -17], [3, 3], [3, -12345], [6786, -10], [-16, 6786], [3, 2938475609], [1234567891, 9876543210], [2938475610, -16], [2938475609, -10], [-12345, -12346], [987654, -12347], [6790, 6790], [2938475610, -12346], [246813579, 2938475610], [2938475610, 2938475610], [-10, 6789], [6787, 6787], [9876543210, -99], [-12345, 246813579], [-975312468, 6790], [1234567891, 9876543211], [6788, 6788], [-10, 6787], [-99, 3], [987653, 987653], [2938475610, 9876543210], [1234567892, -123457], [1234567890, 1234567891], [987653, -12345], [6788, 6787], [987654, -10], [-123457, -123457], [-123457, 2], [1092387466, 987654], [-12345, -12345], [6787, 1092387466], [-99, 6790], [2938475609, 9876543209], [-975312468, 9876543209], [-975312467, 246813579], [-975312468, 6789], [-9876543210, -9876543210], [-975312468, 6788], [9876543210, 9876543210], [246813579, -17], [1092387465, 1234567892], [-123458, -123457], [2, 3], [-123457, 1], [6787, -12346], [6788, 9876543210], [-975312468, -975312468], [-99, 1092387466], [9876543211, 2938475610], [2938475610, -10], [-99, 1234567890], [6788, 987655], [1234567891, -975312468], [9876543209, -17], [6788, 3], [-12347, -123457], [-987655, -123457], [987653, 9876543209], [987655, 6789], [6790, 2938475610], [-987655, 987655], [2938475610, 9876543211], [6788, 9876543209], [9876543209, 6787], [-975312468, 246813579], [1092387466, 1092387466], [3, 4], [2938475611, -11], [9876543211, 9876543210], [2938475609, 9876543210], [987654, 6789], [2938475611, 2938475611], [6788, -16], [-12346, -12346], [987653, 6789], [987654, -123458], [1234567889, -987654], [-11, -9876543210], [-99, 9876543211], [1234567891, -12347], [1234567892, -975312469], [9876543209, 9876543209], [-12346, 6789], [987653, 6790], [-987654, -17], [1234567891, 1234567891], [-987656, -123457], [-987655, 6785], [-975312467, -9876543211], [1234567889, 1234567889], [-987657, 246813579], [-975312469, 3], [1234567891, -16], [1092387465, -987654], [-987657, 1234567890], [6787, 2938475610], [-17, 6787], [-12345, 6788], [1234567891, -123458], [2938475609, 9876543211], [987654, 6788], [2938475609, 4], [6785, 6785], [9876543211, -17], [-123457, 1234567893], [-9876543211, 6789], [4, 3], [-11, 1092387466], [-12347, 6790], [9876543209, 1092387466], [6788, -123457], [1234567892, -975312470], [-123458, -123458], [1234567890, -987655], [1092387465, 4], [6785, 6788], [987653, -123457], [-12346, 9876543209], [1234567892, 9876543210], [-99, -987655], [6786, 9876543211], [-18, -17], [-975312470, -975312470], [1234567891, -99], [-123458, -123459], [6786, 6786], [1234567891, 1234567890], [-12347, -12346], [-12345, 9876543211], [1092387466, -16], [-9, -987654], [-987653, -987653], [2938475609, 6789], [246813579, 246813579], [-987655, 1234567892], [6788, 246813579], [2938475611, 6787], [6790, -12345], [-975312467, -9876543212], [2938475610, 2938475611], [-123459, -123459], [-975312469, -975312470], [-9876543211, -9876543211], [987655, -99], [9876543211, 9876543211], [-18, -19], [9876543210, 9876543209], [1234567892, 1234567892], [-18, -987654], [6786, 1092387466], [-987656, -987656], [1234567892, 1234567891], [6789, -975312468], [-9, -987655], [2938475611, 1234567890], [-987657, 2938475609], [1234567892, 2], [-123459, 2938475610], [-18, 2938475610], [6789, 6788], [1234567891, -12346], [1092387466, 5], [5, -975312469], [-12344, -12344], [6789, -12347], [-16, 6789], [9876543212, 9876543211], [1234567892, 1092387466], [-12344, -12345], [6785, 6787], [-9876543209, -9876543210], [-9876543211, -975312470], [9876543211, 9876543208], [-9876543210, -18], [1234567890, 1092387465], [2938475610, 6788], [-11, -987656], [6786, 6785], [-18, -18], [1092387466, -17], [6787, 2], [1234567893, -123458], [2938475612, -17], [-123459, -99], [246813579, -16], [2938475610, -9], [-12345, -123458], [-11, -11], [2938475611, 2938475609], [1, 6790], [1092387466, 6788], [6789, 9876543209], [6786, 6787], [3, -12344], [3, 6789], [5, 1234567890], [-9876543212, -9876543212], [9876543211, 3], [2938475609, -123457], [9876543212, 9876543210], [-12347, -17], [-9876543211, -9876543210], [1234567893, 6786], [6790, 987654], [-123457, -12344], [6790, -975312470], [246813579, 9876543209], [-975312468, 9876543210], [1234567891, -12345], [-52, 1234567889], [1092387465, 1234567891], [-12347, 1234567893], [2, 2], [-12346, 1092387465], [6791, 6790], [9876543209, -12346], [1234567890, -12346], [-16, -12346], [-987654, -99], [2938475612, 3], [-12344, 6787], [-123458, 6789], [-99, -12345], [9876543210, 2938475610], [-16, 9876543210], [-10, 3], [-987655, -10], [-12346, -9], [9876543210, -18], [-12346, -8], [2938475611, -10], [-12344, -123457], [9876543209, -99], [-99, 1234567891], [1234567889, -12344], [0, 246813579], [-975312470, 2938475611], [6789, 2], [-9, 6787], [6786, 75], [0, 987654], [6785, -975312468], [-99, -11], [-10, -12344], [2938475611, -18], [-9876543209, -9876543211], [2938475612, 9876543212], [987655, 987654], [6791, -975312468], [9876543213, 9876543211], [9876543213, -12347], [246813579, -975312470], [-9, 3], [-9, 246813579], [-987656, 2938475611], [9876543208, -17], [2, -10], [6787, -10], [-12346, 987654], [4, 5], [9876543208, 9876543208], [9876543211, -16], [6788, 6790], [-9, -9876543210], [-11, 9876543209], [-16, -18], [6789, -123457], [-975312467, -9], [9876543209, 1234567891], [-9876543211, 2], [1234567889, 1234567891], [9876543207, 9876543207], [2938475611, -12], [-987656, 3], [-975312469, 6788], [9876543207, 6788], [-12347, -11], [2938475608, 6790], [6787, 2938475612], [2938475612, 2938475611], [1234567893, 1092387466], [-10, 1], [987653, 2938475610], [2938475612, 1], [987653, -987655], [4, -12345], [987655, -100], [987653, -12347], [6788, 9876543213], [6788, -18], [-975312469, -9876543212], [-123458, 6786], [-987656, 1], [6788, 6789], [6785, 6786], [-987653, -9876543212], [-9876543211, -12345], [-19, 6790], [-975312470, -99], [-9876543209, -9876543209], [987655, -9876543212], [6787, -18], [-12347, -12347], [-16, 6788], [-987653, -99], [-16, 246813579], [6790, 9876543210], [6786, 6788], [-975312470, -975312469], [987655, -10], [1234567889, -12346], [9876543213, 1234567891], [1092387466, 4], [1092387464, 1092387464], [9876543210, -123457], [-12344, -10], [987653, -16], [-975312469, -975312468], [-975312469, 1092387464], [2938475611, 2938475613], [9876543208, 3], [3, 1234567890], [-8, -8], [-987655, 1234567891], [-10, -987656], [1234567891, -17], [-9, -8], [9876543212, -11], [-9876543211, 1234567890], [9876543209, 2938475611], [2938475613, 9876543209], [6788, -987656], [1234567889, 6787], [-987654, -123458], [-12348, -12347], [-987655, -987655], [987655, 4], [-12347, 9876543211], [9876543210, 3], [6785, -8], [-15, -987657], [-12348, -16], [987653, -8], [-12345, 1234567891], [246813578, -987657], [6788, 2938475610], [987655, 5], [-19, 2938475610], [-17, -12], [1234567889, 2938475610], [2938475612, 1092387466], [9876543208, 9876543207], [2938475612, 2938475612], [-12, 6789], [-975312469, 2], [6790, -9], [-123458, 2938475609], [-18, 3], [5, -9876543209], [-100, -9], [-987654, -975312468], [-975312469, 4], [1234567893, -12347], [1234567893, 6789], [2, 1], [-987656, -11], [-9876543211, 9876543210], [9876543213, 6788], [-99, 6785], [-16, -123457], [1234567890, -11], [1092387464, -100], [246813578, -10], [-10, -11], [9876543208, -975312469], [6788, 1234567891], [-17, 4], [1234567891, -975312469], [6789, -975312470], [-12348, 6788], [1092387465, -975312470], [-9876543212, -9876543211], [4, 9876543210], [3, 2], [4, 4], [0, 3], [6785, -987654], [1092387465, -17], [-987657, -987657], [-12344, -9876543212], [6789, -9876543211], [1092387465, 1092387465], [-9876543209, 2938475611], [-987656, -19], [-987656, -12345], [6784, -987654], [3, 6788], [9876543209, 4], [-987653, 2938475613], [6786, -975312468], [1234567890, 1234567892], [-9, 9876543212], [6789, 3], [-52, -99], [1092387466, 1092387465], [987655, 987655], [4, 6791], [-19, -19], [987655, 6], [-15, 3], [-12347, 2], [-123459, 5], [2938475611, 987654], [-975312469, -987653], [-975312471, 6787], [-12344, -12346], [-9876543209, 2938475610], [2938475611, 1092387466], [-12, -11], [9876543210, -987657], [-9876543211, -10], [-15, 2938475613], [1, -99], [1234567892, 4], [-17, -99], [-987653, -51], [1234567891, -11], [-975312467, -8], [-975312467, -12345], [5, -16], [6784, -987653], [9876543214, 6788], [-7, -8], [-12, 246813579], [2938475612, 6785], [5, 0], [0, 5], [5, 7], [56789, 126], [0, 15], [25, 0], [-1, 0], [0, -1], [-1, -1], [-12345, 2938475610], [-975312468, 1234567890], [1234567890, 1092387466], [246813579, 987654], [-975312468, 1234567889], [-9876543210, 1234567891], [6788, -99], [3, 1092387465], [2938475610, -12345], [987654, 2938475610], [246813579, -975312469], [246813579, 2938475611], [246813579, -123457], [-12345, 2938475611], [1234567890, -10], [2, 1234567891], [-975312468, 1092387466], [6788, 1234567890], [246813580, 246813579], [3, -10], [-975312469, 6789], [246813579, -10], [-11, -10], [-11, -9], [-975312469, -975312469], [2, 1092387465], [1092387465, 2], [6788, 1234567892], [6788, 1234567893], [-12345, -98], [-975312469, 1234567893], [-17, -9], [-11, -8], [246813580, -975312470], [1092387466, 1092387464], [6788, -975312471], [-12, -8], [1092387466, 2], [1092387466, -11], [1092387465, 1092387466], [-100, 1092387466], [246813579, 4], [6789, 2938475611], [-12344, -17], [2, 1092387464], [1092387466, -123457], [-975312468, 2938475611], [1234567889, 1234567890], [-8, 246813579], [-10, -12345], [-12, -975312468], [-10, -123457], [-98, 246813580], [-12345, 1092387466], [-10, -8], [-12, 246813580], [1234567889, 1092387464], [-12, 1092387465], [246813580, 1234567888], [-975312471, 9876543210], [2938475611, 6788], [-123457, 1234567888], [-975312470, -123457], [-11, 9876543210], [-10, -975312470], [-975312469, 246813579], [6787, 1234567891], [1234567889, -10], [1234567890, 246813580], [-8, 4], [-975312471, 246813579], [-100, 1234567890], [-12346, 1092387466], [987654, 1234567893], [-8, 246813580], [-975312468, -975312469], [1234567889, 246813580], [1234567892, 1234567893], [-9876543209, 1234567891], [1234567891, -12344], [-10, 2], [1, 2], [-12345, -12344], [1234567892, -9], [1234567890, 1092387464], [-7, 4], [-98, -975312470], [-123457, 1234567891], [-975312471, 246813578], [246813579, 1234567891], [-17, -7], [-98, -7], [1234567888, 1234567888], [246813580, -123457], [2938475611, 3], [-17, 2938475611], [1, 1092387466], [987654, 2938475611], [-975312471, 1234567890], [1092387465, 1092387467], [-12345, 2938475609], [-975312469, -12346], [6789, -98], [-8, 1], [6788, -17], [1234567893, 2938475610], [-12, 1234567890], [-12, -975312469], [-9876543210, -123458], [1234567888, 1234567890], [1234567894, -8], [2938475609, 2938475609], [4, -10], [6789, 1234567889], [-6, 4], [-123458, -10], [-9876543210, 1234567888], [-975312469, -7], [-99, -123457], [6790, 6788], [-975312471, 1234567892], [246813578, 3], [246813579, -975312472], [-7, -12345], [-9, -975312471], [246813579, 6789], [-16, 3], [-975312470, 6787], [-123456, 1234567888], [-101, 1234567890], [-12, 1234567888], [-975312470, -975312471], [1234567892, -975312471], [-123457, 2938475609], [987654, -12346], [6789, -12344], [1234567894, 1234567894], [4, 2], [246813582, 246813582], [1092387467, 1092387466], [-98, -98], [1092387464, 6791], [-123456, 31], [-9876543209, -123458], [-97, -975312470], [-123456, -11], [6787, -97], [-10, -9], [-100, 1092387464], [-11, -12346], [1092387467, 2938475609], [-9876543211, -100], [-12, -123458], [1234567889, -8], [-12, -12346], [1092387464, -9876543211], [-123458, -975312470], [-9, -9876543209], [1234567893, 1234567891], [1234567891, -987654], [-975312469, -123458], [6787, -975312468], [-975312471, -975312471], [246813578, 1092387466], [6791, 6791], [-975312470, 246813582], [6788, 1234567889], [1234567894, 1234567895], [-123456, -123457], [-123457, -123458], [-123456, -12344], [246813580, 246813580], [1, -123457], [-8, -123457], [1092387466, 246813580], [-9876543211, 31], [-13, -13], [-7, -123457], [-7, 1092387466], [1234567895, 1234567890], [-987654, 2], [2938475610, 1234567891], [-12344, -975312469], [1234567889, -975312468], [-123456, -12346], [246813581, 246813580], [1092387465, 1092387463], [-9876543210, -123457], [246813578, -975312470], [-101, -101], [1234567892, 6791], [-12, -100], [-987654, -975312470], [-12344, 1234567893], [246813578, 246813579], [-975312471, -975312470], [9876543210, -12344], [-11, 6789], [246813579, 1234567888], [-975312472, -13], [-7, 1092387465], [1234567891, 1234567892], [-8, -12346], [-98, -12345], [2938475609, -12344], [-8, 1234567888], [1234567895, -975312470], [-975312468, -11], [4, 1092387462], [-99, -9], [1234567888, -10], [6791, 1234567895], [-9, -11], [-975312472, -9], [-975312469, -97], [1234567894, 1234567893], [-9876543211, 1234567892], [-97, -123457], [-97, 1092387465], [-6, -98], [1092387463, 1234567891], [246813578, -975312471], [9876543210, -12346], [246813579, -8], [246813583, 246813582], [6789, -12345], [4, -123457], [246813579, 987653], [246813578, -8], [1092387468, 1092387468], [-17, 1234567890], [6790, 1234567889], [6788, 2938475611], [3, -99], [246813579, -12], [-975312470, -123456], [-975312472, -12345], [1234567894, -975312470], [31, 246813578], [-7, -12344], [246813578, 246813578], [1, 1234567892], [6790, 6791], [6789, 246813582], [-7, -7], [987653, 1234567891], [-8, -12345], [31, 987654], [-975312468, -12346], [31, 2], [1234567895, 246813580], [1234567895, 1234567895], [-9876543210, -9876543211], [-975312471, 6790], [1092387465, -975312472], [-9, 1092387464], [-987655, 2], [-98, -123457], [6789, 6791], [-12344, 246813582], [-12346, 1092387464], [-101, -100], [987654, -8], [1092387467, 246813579], [1092387463, 1092387463], [1092387464, -975312471], [6792, 6791], [-98, -99], [2938475610, -12344], [6792, 2], [1234567890, 2938475610], [1, 1234567889], [1234567889, -975312469], [246813579, 5], [987654, 2938475612], [6791, 6789], [1234567893, -123457], [-12, 1092387467], [1092387463, 246813580], [246813580, -975312468], [-12, -99], [-10, 6790], [6788, 246813582], [6792, 1234567892], [-17, 1234567888], [-6, -12344], [32, 31], [-12345, 1092387464], [1092387464, 246813583], [32, 1234567895], [1092387468, 3], [-10, 5], [9876543210, -12345], [-7, 1092387463], [31, 1234567890], [-123456, 6791], [1234567891, 246813581], [9876543209, 9876543210], [1234567892, 1234567896], [-12344, 2938475609], [-101, -975312468], [6792, 246813581], [1234567888, -975312470], [-9876543211, 246813579], [-123457, -12345], [-101, -98], [1234567893, 6791], [1234567891, -9876543209], [-123456, 9876543210], [-123458, 1092387467], [-9, 1234567888], [-12346, 1234567895], [-123456, -123456], [3, 246813580], [-99, -98], [-975312472, -975312472], [-12, -9876543209], [-12346, -975312469], [5, -123457], [1092387463, 1234567889], [-975312468, -123458], [1234567888, -16], [-9876543210, 4], [2938475611, 1234567889], [3, 1092387464], [-975312469, 1234567895], [1234567891, 1092387465], [-12344, 6790], [-99, -12346], [9876543209, -7], [-10, 246813579], [-9, 6789], [2938475610, -123458], [-12344, -11], [1234567888, -11], [1, -13], [1234567893, 1234567892], [-11, -975312472], [1234567896, 987654], [987653, -101], [-11, -123457], [2938475611, -100], [-123458, -12], [2938475609, -975312469], [-123455, 1234567888], [9876543209, -12345], [-123456, 1234567893], [-9, 6], [-12, 246813578], [6787, 246813579], [-11, -12345], [6792, 2938475609], [-12, 1234567891], [-16, -123455], [1092387468, -97], [-14, -14], [9876543210, 246813582], [2938475609, 1092387464], [-97, 4], [-97, 6788], [246813582, -99], [2938475609, 2938475610], [-987654, 246813580], [-101, 6791], [1092387465, 1234567895], [1092387465, 1234567890], [1234567892, 6792], [-975312467, 1234567889], [1092387463, -9], [6792, 6792], [-9876543209, -8], [246813578, 246813580], [-975312471, 246813583], [4, 1092387467], [6789, -9], [-12, 1092387466], [5, 1234567891], [-9, 1092387468], [246813578, 32], [-123457, -123456], [3, -16], [1092387463, 1092387464], [9876543209, 1234567893], [246813581, -11]]
    results = [16, 72, 0, 20, 42, 49, 0, 0, 54, 35, 45, 0, 10, 45, 12, 0, 0, 3, 30, 0, 64, 49, 6, 25, 0, 6, 20, 24, 15, 72, 0, 63, 42, 48, 0, 0, 30, 42, 35, 0, 1, 45, 25, 4, 72, 40, 25, 30, 2, 16, 6, 36, 36, 20, 40, 9, 81, 0, 20, 36, 0, 25, 42, 32, 45, 40, 0, 64, 0, 16, 0, 6, 45, 48, 81, 0, 45, 25, 0, 12, 24, 30, 32, 30, 12, 30, 9, 5, 25, 40, 7, 0, 54, 15, 18, 81, 28, 32, 25, 42, 15, 49, 7, 32, 48, 0, 21, 0, 0, 0, 72, 81, 45, 28, 28, 0, 45, 81, 0, 0, 16, 20, 42, 56, 35, 27, 54, 20, 0, 14, 0, 14, 16, 63, 9, 36, 45, 49, 16, 0, 18, 0, 0, 49, 9, 15, 0, 36, 27, 0, 0, 0, 30, 28, 0, 0, 0, 0, 0, 49, 0, 45, 0, 1, 64, 0, 27, 9, 0, 14, 0, 15, 56, 0, 49, 14, 24, 25, 42, 0, 81, 72, 63, 72, 0, 64, 0, 63, 10, 56, 6, 7, 42, 0, 64, 54, 0, 0, 0, 40, 8, 63, 24, 49, 35, 27, 45, 0, 25, 0, 72, 63, 72, 36, 12, 1, 0, 0, 36, 1, 48, 36, 27, 32, 36, 0, 9, 7, 18, 81, 54, 0, 28, 1, 42, 25, 7, 81, 63, 27, 6, 20, 0, 0, 49, 40, 8, 9, 32, 36, 25, 7, 21, 9, 12, 6, 0, 54, 56, 0, 64, 0, 20, 40, 21, 54, 0, 45, 6, 56, 0, 9, 72, 36, 0, 42, 5, 36, 36, 9, 81, 81, 10, 72, 7, 0, 14, 0, 81, 0, 1, 45, 1, 72, 0, 4, 32, 36, 36, 2, 72, 45, 0, 63, 4, 0, 0, 72, 6, 30, 45, 16, 63, 54, 2, 12, 20, 35, 0, 0, 8, 0, 0, 0, 6, 30, 64, 42, 14, 24, 14, 81, 54, 0, 40, 1, 9, 0, 48, 81, 42, 12, 27, 0, 4, 3, 63, 0, 49, 0, 18, 0, 28, 0, 81, 0, 5, 18, 5, 21, 4, 30, 0, 54, 0, 36, 36, 6, 28, 72, 45, 0, 0, 0, 0, 54, 0, 48, 0, 28, 81, 9, 36, 0, 0, 18, 63, 30, 0, 40, 9, 0, 8, 9, 4, 20, 8, 3, 21, 0, 27, 81, 6, 56, 0, 0, 24, 20, 64, 6, 0, 0, 9, 48, 63, 63, 9, 2, 9, 49, 2, 18, 72, 56, 7, 0, 14, 2, 18, 0, 0, 2, 15, 20, 0, 21, 24, 64, 18, 48, 6, 72, 30, 6, 5, 0, 0, 81, 10, 56, 49, 48, 27, 54, 0, 48, 0, 0, 54, 3, 24, 16, 0, 0, 18, 72, 36, 3, 24, 0, 64, 5, 0, 7, 72, 2, 0, 9, 27, 48, 63, 32, 56, 25, 20, 7, 0, 40, 35, 48, 24, 5, 56, 0, 25, 0, 14, 0, 12, 56, 4, 18, 18, 0, 72, 24, 45, 0, 32, 36, 21, 27, 2, 6, 0, 24, 45, 42, 0, 0, 0, 0, 72, 8, 28, 9, 0, 64, 0, 2, 0, 6, 16, 0, 20, 35, 49, 8, 9, 25, 9, 54, 30, 16, 24, 36, 9, 48, 0, 18, 27, 18, 30, 25, 4, 81, 30, 15, 14, 45, 4, 27, 7, 24, 0, 6, 2, 0, 0, 15, 9, 8, 63, 3, 1, 56, 35, 30, 12, 32, 56, 18, 10, 0, 0, 35, 54, 0, 0, 0, 0, 1, 0, 0, 0, 36, 72, 0, 72, 15, 0, 0, 81, 9, 63, 5, 0, 2, 48, 0, 0, 0, 81, 0, 0, 9, 81, 10, 10, 16, 24, 40, 27, 63, 8, 0, 24, 8, 16, 12, 6, 30, 0, 36, 9, 28, 8, 42, 8, 0, 72, 0, 16, 0, 0, 30, 0, 0, 36, 10, 0, 0, 8, 56, 0, 0, 0, 81, 7, 0, 0, 32, 9, 0, 36, 12, 0, 72, 0, 6, 9, 4, 0, 2, 20, 18, 0, 28, 0, 7, 8, 9, 49, 56, 64, 0, 3, 7, 6, 4, 0, 35, 45, 54, 72, 8, 56, 0, 0, 18, 0, 0, 32, 81, 0, 81, 24, 0, 0, 63, 63, 0, 2, 24, 18, 35, 9, 81, 18, 0, 48, 0, 16, 0, 2, 63, 24, 36, 16, 8, 4, 42, 64, 4, 6, 72, 0, 6, 49, 0, 0, 6, 63, 0, 16, 72, 12, 4, 0, 81, 3, 4, 72, 56, 1, 48, 1, 0, 72, 20, 42, 56, 24, 0, 7, 56, 0, 1, 9, 49, 42, 0, 8, 0, 36, 72, 36, 0, 15, 0, 0, 1, 2, 0, 0, 12, 72, 0, 0, 9, 72, 6, 35, 2, 48, 40, 36, 64, 0, 8, 8, 81, 0, 5, 9, 18, 63, 12, 2, 49, 35, 48, 3, 8, 0, 72, 6, 45, 28, 27, 64, 64, 0, 0, 8, 27, 18, 0, 10, 0, 8, 28, 64, 2, 0, 18, 49, 3, 40, 4, 48, 2, 0, 25, 0, 0, 10, 36, 10, 56, 9, 8, 24, 0, 32, 63, 9, 4, 2, 72, 0, 4, 0, 9, 81, 45, 8, 9, 21, 14, 0, 0, 18, 0, 16, 4, 56, 24, 2, 20, 12, 10, 24, 0, 0, 21, 0, 6, 1, 0, 12, 36, 8, 2, 0, 9, 35, 8, 3, 9, 0, 56, 72, 30, 36, 0, 72, 4, 18, 54, 35, 27, 64, 48, 0, 9, 12, 45, 5, 0, 54, 63, 0, 81, 0, 4, 8, 3, 6, 2, 24, 3, 7, 0, 16, 81, 40, 45, 18, 54, 16, 63, 5, 18, 2, 30, 56, 16, 0, 36, 28, 56, 18, 0, 0, 1, 25, 0, 4, 63, 27, 4, 72, 0, 3, 28, 81, 12, 5, 72, 16, 42, 18, 12, 27, 1]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(multiply)
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
    result = ''
    while x > 0:
        result = str(x % base) + result
        x = x // base
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()




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
    inputs = [[8, 3], [9, 3], [234, 2], [16, 2], [8, 2], [7, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [10, 5], [15, 4], [25, 6], [33, 7], [45, 8], [50, 9], [13, 5], [17, 3], [42, 8], [15, 2], [8, 4], [17, 8], [9, 5], [7, 6], [5, 8], [45, 7], [4, 9], [3, 3], [8, 8], [2, 8], [15, 7], [50, 5], [8, 7], [25, 5], [17, 9], [5, 9], [2, 6], [9, 9], [4, 4], [7, 7], [5, 4], [3, 7], [13, 7], [15, 3], [2, 2], [17, 7], [7, 5], [10, 8], [3, 6], [16, 8], [18, 2], [15, 5], [6, 6], [46, 8], [7, 9], [50, 2], [41, 8], [16, 4], [46, 5], [17, 2], [3, 2], [3, 9], [13, 8], [9, 6], [42, 7], [10, 4], [45, 6], [15, 8], [43, 7], [5, 5], [3, 5], [4, 3], [13, 9], [9, 8], [33, 9], [6, 3], [10, 7], [8, 9], [18, 7], [19, 7], [43, 5], [46, 7], [8, 5], [16, 7], [34, 3], [16, 6], [6, 4], [4, 6], [5, 7], [15, 6], [14, 5], [14, 6], [10, 9], [46, 6], [5, 2], [18, 9], [18, 8], [7, 4], [35, 9], [4, 8], [6, 5], [50, 7], [50, 8], [13, 4], [256, 5], [2019, 3], [34567, 9], [27, 3], [987654321, 8], [9999999, 9], [123456789, 3], [2669, 7], [48298461, 8], [245678, 7], [9999999, 8], [2019, 4], [987654321, 9], [245678, 8], [123456789, 8], [2019, 9], [6, 9], [2018, 9], [123456789, 4], [2, 4], [34567, 4], [9, 4], [256, 9], [48298461, 4], [245678, 3], [48298462, 9], [2669, 4], [1, 3], [2, 9], [48298462, 4], [2020, 3], [27, 2], [2669, 8], [4, 2], [2, 5], [245678, 9], [9, 7], [48298461, 2], [9999999, 6], [9999999, 5], [245678, 4], [26, 2], [2020, 4], [987654321, 3], [2018, 8], [34568, 9], [10, 2], [10, 3], [27, 8], [256, 4], [257, 4], [34568, 2], [9, 2], [34569, 2], [1, 2], [245678, 5], [2670, 7], [2, 7], [27, 9], [5, 3], [34567, 2], [34568, 4], [2669, 2], [26, 4], [123456789, 2], [2019, 8], [34569, 9], [34567, 3], [0, 3], [257, 8], [2669, 3], [26, 7], [2019, 5], [28, 3], [123456790, 8], [34567, 8], [257, 7], [48298461, 6], [256, 8], [2669, 6], [26, 6], [34568, 3], [27, 5], [26, 5], [9999999, 4], [48298460, 2], [2019, 6], [48298460, 9], [48298463, 6], [48298460, 7], [123456790, 9], [48298463, 9], [27, 6], [34569, 4], [27, 4], [34570, 9], [256, 3], [245679, 4], [245679, 8], [257, 9], [26, 3], [9999999, 2], [1, 6], [48298463, 8], [2669, 5], [123456791, 9], [257, 6], [0, 8], [123456790, 7], [257, 3], [245679, 9], [34570, 7], [1, 5], [123456790, 4], [48298462, 2], [9999999, 7], [34569, 3], [123456791, 4], [255, 5], [123456788, 4], [123456792, 4], [255, 6], [10000000, 8], [255, 9], [8, 6], [123456791, 3], [255, 2], [1, 8], [34568, 8], [10000000, 5], [255, 3], [48298461, 3], [48298461, 9], [123456790, 3], [34569, 7], [34570, 3], [123456789, 6], [123456788, 3], [257, 5], [987654321, 5], [2020, 9], [2018, 6], [1, 7], [48298461, 5], [6, 8], [48298462, 8], [34571, 7], [0, 7], [34571, 2], [28, 7], [34571, 4], [257, 2], [34569, 5], [11, 9], [48298461, 7], [48298462, 6], [245680, 4], [11, 6], [34568, 5], [10000000, 6], [48298462, 3], [2018, 3], [34569, 8], [245679, 5], [245680, 3], [10000000, 4], [10000000, 7], [9999999, 3], [34571, 6], [28, 9], [1, 4], [11, 7], [2670, 4], [0, 5], [123456791, 8], [123456788, 2], [9999998, 5], [34571, 8], [245679, 3], [123456792, 7], [34568, 7], [123456792, 5], [34568, 6], [123456788, 5], [2020, 2], [2670, 6], [48298460, 8], [245678, 6], [9999998, 3], [34570, 5], [48298460, 5], [10000000, 2], [123456792, 3], [2020, 8], [34571, 3], [245680, 8], [123456791, 7], [6, 2], [123456788, 8], [255, 8], [123456792, 2], [258, 5], [258, 9], [48298463, 3], [2671, 2], [245677, 4], [10000001, 2], [10000001, 8], [48298463, 4], [34570, 8], [34571, 9], [48298462, 7], [48298460, 4], [0, 9], [9999998, 2], [11, 3], [9999998, 6], [2671, 4], [2018, 2], [245676, 5], [123456791, 2], [9999998, 7], [28, 2], [28, 5], [10000001, 6], [34570, 2], [245676, 2], [11, 5], [2672, 5], [48298460, 6], [34570, 4], [256, 6], [123456790, 5], [48298464, 4], [2669, 9], [123456790, 2], [0, 2], [123456790, 6], [245677, 5], [2020, 7], [255, 4], [2019, 2], [28, 4], [10000001, 7], [48298464, 6], [30, 2], [25, 2], [123456788, 6], [258, 2], [26, 8], [245679, 6], [2018, 4], [0, 4], [34567, 7], [2018, 5], [27, 7], [10000000, 9], [987654320, 8], [245679, 7], [3, 8], [245677, 9], [34567, 6], [987654320, 6], [245677, 7], [245677, 6], [987654321, 6], [28, 8], [987654320, 9], [245677, 8], [987654320, 7], [987654320, 5], [4, 7], [245677, 3], [256, 2], [245678, 2], [26, 9], [245679, 2], [2670, 5], [2670, 8], [987654322, 6], [987654322, 2], [2017, 3], [2020, 5], [10000001, 4], [0, 6], [987654321, 2], [123456789, 9], [10000002, 6], [987654323, 2], [10000002, 7], [123456788, 9], [28, 6], [2017, 7], [25, 7], [2670, 9], [987654322, 8], [10000001, 9], [987654323, 4], [25, 3], [29, 2], [10, 6], [987654323, 7], [987654321, 4], [29, 3], [2020, 6], [987654320, 2], [245676, 3], [9999998, 9], [245676, 4], [245676, 9], [2016, 7], [987654319, 6], [987654319, 8], [10000002, 5], [2671, 6], [7, 3], [987654319, 4], [2017, 2], [987654319, 5], [2670, 3], [2018, 7], [25, 4], [987654319, 7], [10000001, 3], [256, 7], [2016, 5], [245677, 2], [34567, 5], [2017, 6], [29, 4], [10000001, 5], [29, 9], [48298462, 5], [987654320, 3], [9999998, 8], [48298463, 7], [987654323, 3], [2671, 8], [48298459, 2], [10000002, 2], [987654322, 4], [987654323, 6], [25, 9], [2016, 4], [245680, 7], [123456789, 7], [2668, 8], [123456789, 5], [987654322, 3], [245675, 4], [2017, 8], [987654321, 7], [48298463, 5], [48298459, 4], [987654322, 7], [48298459, 3], [12, 9], [2021, 2], [987654323, 8], [12, 8], [987654319, 9]]
    results = ['22', '100', '11101010', '10000', '1000', '111', '2', '3', '4', '5', '6', '7', '20', '33', '41', '45', '55', '55', '23', '122', '52', '1111', '20', '21', '14', '11', '5', '63', '4', '10', '10', '2', '21', '200', '11', '100', '18', '5', '2', '10', '10', '10', '11', '3', '16', '120', '10', '23', '12', '12', '3', '20', '10010', '30', '10', '56', '7', '110010', '51', '100', '141', '10001', '11', '3', '15', '13', '60', '22', '113', '17', '61', '10', '3', '11', '14', '11', '36', '20', '13', '8', '24', '25', '133', '64', '13', '22', '1021', '24', '12', '4', '5', '23', '24', '22', '11', '114', '101', '20', '22', '13', '38', '4', '11', '101', '62', '31', '2011', '2202210', '52367', '1000', '7267464261', '20731370', '22121022020212200', '10532', '270174735', '2042156', '46113177', '133203', '2484401020', '737656', '726746425', '2683', '6', '2682', '13112330310111', '2', '20130013', '21', '314', '2320033213131', '110111000012', '110784027', '221231', '1', '2', '2320033213132', '2202211', '11011', '5155', '100', '2', '414005', '12', '10111000001111100111011101', '554200143', '10024444444', '323332232', '11010', '133210', '2112211110001000200', '3742', '52368', '1010', '101', '33', '10000', '10001', '1000011100001000', '1001', '1000011100001001', '1', '30330203', '10533', '2', '30', '12', '1000011100000111', '20130020', '101001101101', '122', '111010110111100110100010101', '3743', '52370', '1202102021', '0', '401', '10122212', '35', '31034', '1001', '726746426', '103407', '515', '4443111553', '400', '20205', '42', '1202102022', '102', '101', '212021121333', '10111000001111100111011100', '13203', '110784025', '4443111555', '1124346560', '277266781', '110784028', '43', '20130021', '123', '52371', '100111', '323332233', '737657', '315', '222', '100110001001011001111111', '1', '270174737', '41134', '277266782', '1105', '0', '3026236222', '100112', '414006', '202534', '1', '13112330310112', '10111000001111100111011110', '150666342', '1202102100', '13112330310113', '2010', '13112330310110', '13112330310120', '1103', '46113200', '313', '12', '22121022020212202', '11111111', '1', '103410', '10030000000', '100110', '10100212211000220', '110784026', '22121022020212201', '202533', '1202102101', '20130035113', '22121022020212122', '2012', '4010314414241', '2684', '13202', '1', '44331022321', '6', '270174736', '202535', '0', '1000011100001011', '40', '20130023', '100000001', '2101234', '12', '1124346561', '4443111554', '323332300', '15', '2101233', '554200144', '10100212211000221', '2202202', '103411', '30330204', '110111000021', '212021122000', '150666343', '200211001102100', '424015', '31', '1', '14', '221232', '0', '726746427', '111010110111100110100010100', '10024444443', '103413', '110111000020', '3026236224', '202532', '223101104132', '424012', '223101104123', '11111100100', '20210', '270174734', '5133222', '200211001102022', '2101240', '44331022320', '100110001001011010000000', '22121022020212210', '3744', '1202102102', '737660', '3026236223', '110', '726746424', '377', '111010110111100110100011000', '2013', '316', '10100212211000222', '101001101111', '323332231', '100110001001011010000001', '46113201', '2320033213133', '103412', '52372', '1124346562', '2320033213130', '0', '100110001001011001111110', '102', '554200142', '221233', '11111100010', '30330201', '111010110111100110100010111', '150666341', '11100', '103', '554200145', '1000011100001010', '111011111110101100', '21', '41142', '4443111552', '20130022', '1104', '223101104130', '2320033213200', '3585', '111010110111100110100010110', '0', '20130035114', '30330202', '5614', '3333', '11111100011', '130', '150666344', '4443112000', '11110', '11001', '20130035112', '100000010', '32', '5133223', '133202', '0', '202531', '31033', '36', '20731371', '7267464260', '2042160', '3', '414004', '424011', '242000505412', '2042155', '5133221', '242000505413', '34', '2484401018', '737655', '33321631442', '4010314414240', '4', '110111000011', '100000000', '111011111110101110', '28', '111011111110101111', '41140', '5156', '242000505414', '111010110111100110100010110010', '2202201', '31040', '212021122001', '0', '111010110111100110100010110001', '277266780', '554200150', '111010110111100110100010110011', '150666345', '277266778', '44', '5611', '34', '3586', '7267464262', '20731372', '322313212202303', '221', '11101', '14', '33321631445', '322313212202301', '1002', '13204', '111010110111100110100010110000', '110111000010', '20731368', '323332230', '414003', '5610', '242000505411', '7267464257', '10030000002', '20211', '21', '322313212202233', '11111100001', '4010314414234', '10122220', '5612', '121', '33321631441', '200211001102102', '514', '31031', '111011111110101101', '2101232', '13201', '131', '10030000001', '32', '44331022322', '2112211110001000122', '46113176', '1124346563', '2112211110001000202', '5157', '10111000001111100111011011', '100110001001011010000010', '322313212202302', '242000505415', '27', '133200', '2042161', '3026236221', '5154', '223101104124', '2112211110001000201', '323332223', '3741', '33321631443', '44331022323', '2320033213123', '33321631444', '10100212211000211', '13', '11111100101', '7267464263', '14', '2484401017']
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(change_base)
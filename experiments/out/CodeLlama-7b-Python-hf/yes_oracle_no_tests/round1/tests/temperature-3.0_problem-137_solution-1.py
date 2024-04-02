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
    a = float(str(a).replace(",", "."))
    b = float(str(b).replace(",", "."))
    if a > b:
        return a
    elif a == b:
        return None
    else:
        return b


def compare_one_elegant(a, b):
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
    a = float(str(a).replace(",", "."))
    b = float(str(b).replace(",", "."))
    return max(a, b) if a != b else None




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
    inputs = [[1, 2], [1, 2.5], [2, 3], [5, 6], [1, '2,3'], ['5,1', '6'], ['1', '2'], ['1', 1], [3, 3], [-1, -1], [0, 0], [-2.5, 2.5], [10, '10.0'], ['5,000', 5000], ['7.3', 7.3], [-3, '-3.0'], ['-4,1', '-4.0'], [-2.0, 3], [1, 0], ['77.3', '7.3'], [10, 0], [-1.0425166390148266, -1.123543564552395], ['5,000', 4999], ['773.3', '7.3'], [1, -1], ['7.3', -2.5], [5000, 0], [4999, 5000], [4999, -1], ['7.3', -2.0], [-1, 10], ['7.30', '-3.0'], [10, '77.3'], [5001, 0], [5000, 5001], [5000, 5000], [0, 5001], [-2.0, 2.5], [10, -1], ['5,0050', 10], [11, 10], ['7.3', '7.3'], [-1, -3], [10, 10], [10, '1.0'], [0, 4999], ['5,000', '5,000'], [4999, 5001], ['773.3', 5000], [5000, 3], [2, 1], ['5,000', '05,000'], [0, -1], [3, 0], [3, -1], [-1, '77.3'], [1, 5001], [5001, -3], [1.496091849454374, 2.5], [-2.0, 2], [-1, -2], [-3, 2], [-1.0425166390148266, -1.0425166390148266], [9, 10], [5002, -3], [1, 1], [1.496091849454374, 2], [4999, 1], [1, 9], [-3, -3], [0, 1], [-3, -2], ['11.0', '1.0'], ['7.3', '-4,1'], [10, 5000], [5002, 5000], [-3, 5000], [7.3, 7.3], ['7.3', 1.496091849454374], [-2.0, 5002], [41, 40], ['-4.0', '-4.0'], [2.5, 5002], [4999, 4999], [1, -2], [-1.123543564552395, 2.5], [9, '77.3'], [41, -2], [5000, 2], [9, '10.0'], [-1.123543564552395, 3], [-2.0, -2.0], [5002, '77.3'], [10, 5002], [1, 10], [11, 0], [5000, 4998], [1.496091849454374, -1.0425166390148266], [-2, 4999], ['7.33', '7.3'], [-2, 2], ['-4,1', '7.3'], [10, '-4,1'], [40, -2], [11, 11], ['05,000', '1.0'], ['11.0', '77.3'], [-3, 3.14], [-9.876, '-9.123'], ['-8,9', -7.654], ['1.23', '1,45'], ['-6.7', '6.7'], ['3', '3.0'], ['-2', '-2.0'], ['0', 0], [1, '1.00000001'], ['1.25', '1,250'], ['1,45', '1.25'], ['15,415', '1,45'], ['3', '1.25'], ['6.7', '1.25'], ['1,45', '1.225'], ['1.25', '1.25'], ['1,45', 0], ['0', '1.25'], ['1.25', '6.7'], ['00', 0], ['15.25', '1.25'], [-7.915238266264661, -7.654], ['7', '1.25'], [1, -3], ['1', '1.125'], [1, '1,45'], ['3,415', '41,45'], [-8.74973784205587, -9.876], ['-9.123', '-9.123'], ['-9.12', '-9.123'], ['1.205', '1.25'], ['3', '15.25'], [-3, -7.915238266264661], ['-2.0', '1.25'], ['00', '00'], ['3', '1.205'], ['1.225', '1.225'], ['-8,9', '00'], ['1.23', '1.225'], ['15.25', '15.25'], ['3', '1.215'], ['6.7', '-15,4159'], ['1,250', '1.2'], ['3.0', '-2.0'], ['16.7', '16.7'], ['15,415', '1'], ['41,45', '41,45'], [-2, -3], [2.767386384178415, 3.14], ['41,45', '4,45'], ['145', '145'], ['-6.7', '-2.0'], [-7.654, -7.014581866391794], ['00', '1.25'], [-8.74973784205587, -8.74973784205587], ['1.23', '16.7'], ['1,45', '1,45'], ['0', '1,45'], ['1,45', '1,4'], ['1,45', '1,'], ['33', '1.25'], ['00', -1], [-12.967215344684003, -4.51094653769451], ['1.20', '33.0'], ['1.23', '-6.7'], ['1.23', '1.125'], ['1.215', '1.215'], ['1', '15,415'], ['1.25', '6337'], ['-.123', '-.123'], ['0', -1], ['1.25', '63371.25'], ['1.23', '1.1'], ['0', '0'], ['33.0', '1.215'], ['1', '1.225'], ['1.0205', '1.25'], ['0', -2], ['415', '41,45'], [-12.774935986016603, -12.967215344684003], ['.0', '-2.0'], ['1.1', '1.25'], ['1.23', '1.23'], ['000', '1,'], ['415', '415'], ['2151,250', '1.2155'], [-2, -1], [-7.915238266264661, -7.014581866391794], ['3', '3'], ['-9.12', '415'], ['1.20', '1.25'], [-12.774935986016603, -12.774935986016603], [34, -2], ['-2.000', '-2.0'], ['41,45', '6.7'], ['11.23', '1.225'], ['-9.12', '1.1'], ['1,250', '1,250'], ['1.2', '-9.1'], ['1.1', '33'], ['-6.7', '1.23'], ['63371.25', '-2'], ['115.25', '15.25'], ['1,45', '0'], ['1,4', '1,45'], [-3, 34], [-2, -2], ['333', '1.1'], [-2, 3.14], ['-2.000', '-9.1'], ['1.0205', '1.1'], ['-8,9', '-8,9'], ['-2.0', '16.7'], ['1.03', '-6.7'], ['3.0', '-2.'], ['1.23', '415'], ['33', '1.205'], ['330003', '1.25'], [-6.4514534689514935, -9.876], ['63371.25', '1.0205'], ['1.1', '1.2'], ['11', '1.225'], ['00', -3], ['000', -2], [1, 11], ['333', '333'], ['1.23', '41,45'], ['-2.000', '63371.25'], ['115.25', '11.23'], ['-.123', '4,45'], ['-6.7', '16.7'], [-8.298650833465093, -7.014581866391794], ['1.205', -1], ['-2.0', '1.20000'], ['00', '0'], ['41,45', '000'], [-2, 34], ['33', '4,45'], ['15', '1.25'], ['1.323', '1.23'], [-7.014581866391794, -7.915238266264661], ['15,4115', '6337'], [1, 34], ['.7', '16.7'], ['7', '7'], [-8.298650833465093, -12.967215344684003], ['333', '33'], ['000', '00'], [-7.654, -7.654], [35, -2], ['15.25', '21.25'], ['5', '-2.0'], [-1, 34], ['1.1', '1.1'], ['1.205', '1.205'], ['415', '-9.12'], ['-8,9', '3113'], ['-9.12', '3'], ['6.7', '3,415'], ['1.23', '63371.25'], ['21.20', '00'], ['3113', '63371.25'], [-15.232196952601557, -5.75363867961704], ['11', '1.125'], ['13.323', '1.323'], ['11', '1.20'], [12, 11], ['-84,45', -7.654], [84, -2], [-3, -1], ['13.323', '1.225'], ['1.23', '15.25'], ['145', '1.0205'], [1, 35], ['-2.000', '-9.123'], ['3300', '4,45'], ['3,415', '0'], ['3415', '3,415'], ['1.00000001', '21.25'], ['33.0', '33.0'], [2.767386384178415, -7.654], ['000', '-2.000'], [-15.232196952601557, -15.232196952601557], ['5', '-15,4159'], [2.767386384178415, -8.226976895748662], ['1.00000001', '41,45'], ['-6.75', '-6.00075'], [-8.900537956858544, -12.774935986016603], ['-9.12', '1.11'], ['-6.00075', '7'], ['0', 84], ['-6.7', '15,4115'], ['1.133000323', '1.33000323'], ['-6.75', '21.25'], [12, 12], ['1.1', '63371.25'], [-5.75363867961704, -12.774935986016603], ['6337', '-84,45'], ['11.1', '1.1'], [3.712550934925414, 2.767386384178415], ['-8,9', '1.25'], ['-9.12', '-9.12'], ['6.7', '-15,41159'], [-7.654, -4.5668177959472835], ['-6.7', '-6.7'], [1, 70], ['125', '21.25'], ['15,41', '1'], ['1.000000001', '1.00000001'], ['-2.0', '115.25'], ['-15,41159', '11.23'], [-9.13887722899935, -7.654], ['-2.000', '1.125'], ['00', '6.7'], ['11.23', '11.23'], [-3, 11], ['41,4', '4,45'], [-2, 70], [34, 34], [-4, 11], ['1.20', '1.20'], ['-9.12', '44'], ['-6.7', '41,45'], ['151,411115', '15,4115'], ['-6.7', '3415'], ['-.123', '1.23'], ['1.20000', '1.215'], [-12.967215344684003, -12.967215344684003], ['-9.1', '1.23'], ['1.23', '1225'], ['4,45', '4,45'], ['-.123', '1415.23'], ['15,41', '11'], ['1.23', '13.02125'], ['1.02205', '1.02205'], ['77', '7'], [-4, -3], ['6.7', '11'], ['115.25', '-2'], [-8.648925493228285, -7.654], [-12.774935986016603, -7.654], ['-2.0044', '000'], ['415', '1415.23'], ['.0', '115.25'], [-2, 1], ['.7', '3.0'], ['41,45', '1.1'], ['1,545', '3415'], ['00', '1.03'], ['-8,9', -9.761009327429885], [2.8215418518706716, 3.14], ['-2.0', '1.11'], [-7.014581866391794, -7.014581866391794], [-7.947227268681752, -7.947227268681752], ['1.225', '15,4115'], [2.8215418518706716, -7.014581866391794], ['-8,9', '13.02125'], ['41,4', '33'], [-10.397627547678898, -11.107660229810385], ['-9.12', '11.23'], ['-125.00075', '7'], ['1.20000', '1.00000001'], [-1, 33], ['0011', '0011'], [2, 34], ['1225', '13.02125'], ['1.25', '-2'], [2.767386384178415, 4.569736337135209], ['-2', '-2'], ['1,45', '145'], ['000', -3], [-1, 35], ['33', '33'], ['155', '15'], [-1, 36], ['-8,9', '000'], ['1,250', '151,411115'], ['63371.25', '6337'], [-12.774935986016603, -7.014581866391794], ['1,545', '3333300'], [-8.648925493228285, -98.33564388101799], ['00', '-9.123'], ['0', '-9.123'], ['415', '-9.1'], ['155', '155'], ['1', '-9.12'], [-5.75363867961704, -7.654], ['1.000000001', '1.000000001'], ['00', '3,415'], [-9.761009327429885, -8.226976895748662], ['1.205', '1.00000001'], ['115.25', '15,415'], [-6.4514534689514935, -7.654], [-6.122895581745484, -6.122895581745484], [-1, 38], ['15500', '67.7'], [4.569736337135209, 2.767386384178415], ['11.23', '.7'], ['16.7', '16.77'], ['33', '77'], ['12257', '13.02125'], ['-6.00075', '-6.00075'], ['-15,4159', '63371.25'], ['1.125', '11.125'], ['55', '5'], ['03415', '1,45'], ['1,5', '1.25'], ['1,45', '00'], [-69.38740384414959, -69.38740384414959], [1, '11'], ['-8,9', '.0'], [-8.648925493228285, -8.74973784205587], ['2151,250', '-2'], ['1', '12251'], ['-91.12', '-9.12'], ['41.22515', '-9.1'], ['.7', '1.2155'], ['33.0', '-2.0'], ['1.233', '1.23'], ['-9.1', '1.0000'], ['41,455', '-9.1'], ['415', '414,45'], ['1.125', '-8,9'], ['4,45', '1.1'], ['000', 0], ['63371.25', '3415'], [-9.13887722899935, -4.5668177959472835], ['333', '3333'], ['-15,41593', '3333'], [-3, 84], ['1,45', '41,45'], [36, 84], ['41,4', '1,'], ['-9.12', '-15,4159'], ['151.25', '-2.0'], ['12257', '-9.1'], ['1.3300023', '1,45'], ['1.2155', '155'], [-4, -2], [-7.915238266264661, -4.51094653769451], ['6337', '1.215'], ['12215', '1225'], ['5', '16.77'], ['-2.0', '1.02205'], [75, -68], [-68, -68], ['151.235', '155'], [-7.945789698508423, -7.014581866391794], ['0', '1,5'], ['00', 84], ['3333300', '13415,545'], ['-9.12', '444'], ['1.2205', '1.00000001'], [-12.774935986016603, -7.915238266264661], ['15500', '41,45'], ['777', '000'], ['00', '3300'], ['1', '1'], ['03415', '1.23'], [-7.654, -12.774935986016603], ['1.20', '0011'], ['-9.123', '1.5'], [11, 34], ['111', '1'], [-15.232196952601557, -7.014581866391794], [-69.90474800626136, -69.38740384414959], ['00', '151.25'], ['-9444.12', '-9.12'], ['15', '15'], ['11.23', '11.123'], [-15.232196952601557, -5.649489992448723], [0, -4], ['1.0000000001', '1.000000001'], [-9.876, -9.876], ['-91.1215', '1.25'], ['0', '-91.1215'], ['55', '-2.0'], ['3113', '151.235'], ['-91.12', '1.2333330025'], ['0', '-2'], ['-125.00075', '77'], ['13415,5451', '1'], ['00', '01.03'], [34, 35], ['3,4415', '3,4415'], [-8.298650833465093, -12.0138597047669], [34, 0], ['115.25', '115.25'], ['-84,45', '-2.0'], [-14.727099773983543, -9.876], ['1,45', '-9.1'], ['63371.25', '63371.25'], ['-15,41159', '-2.0'], ['1,545', '-84,45'], [-8.298650833465093, -8.298650833465093], ['414,45', '414,45'], ['11', '21.125'], ['1.5', '1.233'], [-1, 2], ['1,250', '1.2155'], ['111.23', '11.23'], ['1', '15,41'], ['1.25', '1.33003'], ['1.2205', '1.000000001'], ['-91.1215', '-2.0'], ['11.223', '11.23'], ['3415', '3415'], ['-15,4159', '13415,5451'], [11, 2], ['-6.050075', '-6.00075'], ['33', '-9.123'], [1, -4], [-5.75363867961704, -4.9122923154404425], ['-6.050075', '-6.050075'], [38, -50], ['9.1', '-9.1'], ['6337', '-.123'], [-7.915238266264661, -8.22566929632332], ['0', '77'], ['3333', '33'], [-9.084182019357039, -9.084182019357039], ['-2.0044', '-2'], ['13.02125', '13.02125'], ['1.23', '63371.275'], ['15500', '1.5'], ['3415', '1.2'], [-5.649489992448723, -7.959931287366305], ['1.2034155', '1.205'], [-68, 12], ['1.22205', '1.2205'], ['115', '1.225'], ['55', '-2.0044'], ['1,54533', '33'], ['444', '12251'], ['0', '1.5'], ['1.02125', '13.02125'], ['-6.7333', '3333'], ['1.2155', '-6.050075'], ['-6.75', '33'], ['-11159', '-15,41159'], ['1.2', '1,45'], ['-2.0', '-2.0'], ['215150', '2151,2550'], ['1.0205', '1,4'], ['1.125', '11.23'], ['41,4', '3,415'], ['115.255', '115.25'], [-4.51094653769451, -5.4389252401123995], ['41533', '1415.23'], ['1.020000', '1.00000001'], ['414', '41,4'], [-7.654, -9.761009327429885], ['15500', '1515'], ['000', '000'], [3.14, -6.122895581745484], ['3300', '3300'], ['1.0205', '11.1'], ['1.02125', '3,415'], ['01.03', '0'], ['1.5', '3,44115'], ['1.2034155', '1.2034155'], ['1225', '1225'], ['11', '115'], ['1.2333330025', '-91.12'], ['3113', '-2'], ['-6.00075', '77'], ['1.1333000323', '1.1333000323'], [-9.876, -13.001526912961886], ['15500', '67.'], ['12215', '11225'], ['-2.', '-2.000'], ['3,4341515', '3,4341515'], ['13.323', '1.23'], ['5', '16.7'], [-8.74973784205587, -5.75363867961704], ['-9444.12', '1.2205'], ['15,41000', '15,41000'], ['1,45', -50], ['1.2125', '1.2'], [3.712550934925414, -6.06088794991491], [-7.947227268681752, 2.767386384178415], [-98.33564388101799, -9.084182019357039], ['701.037', '77'], ['1.23335', '9.1'], [75, 1], ['1.20', '13.323'], ['0', '1.03'], ['1.123', '-6.7'], ['1.22205', '15,4115'], ['-15,41159', 0], ['-15,41593113', '155'], ['13.323', '-9.123'], [-69.90474800626136, -5.75363867961704], ['1.20', '11'], ['-6.7', '155'], ['12.2155', '1.2155'], ['1.02205', '1225'], ['3,4415', '71.33003'], ['44115', '4415'], ['441,45', '441,45'], ['13415,5451', '13415,5451'], ['1,', 2], [1, '1.'], [100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 2], [-1.0, '-2,3'], ['5,1', -6], ['1.1', '1.0'], ['1.', 1], ['0.0', 0], [-11.11171337843259, -9.876], ['-23', '-9.123'], ['-2.0', '-2'], [-7.654, '-9.123'], [0, -3], [-11.11171337843259, '-9.123'], [3.14, 3.14], ['-3.023', '-9.123'], ['-26.73', '-9.123'], [3.14, 3.5098365670180556], [-3, 0], ['0', -3], ['1.2', '1.25'], [3.5098365670180556, 3.14], ['1,250', '-3.023'], [1, '1.2'], ['1,45', '1.23'], ['-26.73', '1.00000001'], ['-6.7', '-2'], ['-2', '1.00000001'], ['.2', '1.2'], [-11.11171337843259, -11.11171337843259], [4.452161057484629, -9.876], [4.452161057484629, 4.452161057484629], ['3.0', '3.0'], [-11.931240615627274, '-9.123'], ['-9.123', '-2.03'], ['1,250', '1.00000001'], ['1,250', '11.000000010'], [-9.876, -9.707613442054273], ['-23', '11.000000010'], ['1,250', '11.00000001'], [-5.403249230556667, '.2'], ['-2.0', '-9.123'], ['-3.023', -7.654], ['-2', '-9.123'], ['6.7', '6.7'], [-9.514520957128042, -9.876], [-9.514520957128042, -9.514520957128042], ['23', 0], [1.9155795783061915, 3.14], [11, -2], [-9.876, -8.997546011069746], [-9.876, -9.514520957128042], [-5.403249230556667, -7.654], ['-9.123', '-2.0'], ['0', 11], [-9.514520957128042, -8.997546011069746], ['1.00000001', '-6.7'], ['-21.00000001', '-2'], [-6.410274451315487, '0'], [-9.876, -12.944537034527363], [2.1344375030805596, 2.1344375030805596], ['1,250', '-2.03'], [2.506774567617957, 1.6388390454446027], ['-3.023', '-3.023'], ['23', '1.000000001'], [2.506774567617957, 1.0206072532818764], ['1.000000000', '1.000000001'], [-4.636255829707621, -8.997546011069746], [-6.410274451315487, '3'], ['1.23', '-9.2'], [-7.654, '11.000000010'], ['-2.73', '1.00000001'], [-11.651945761505571, -9.876], [-4.636255829707621, -4.636255829707621], [-4, '0'], ['116.700000001', '1.000000001'], ['1.000000001', '-9.2'], ['116.700000001', '116.700000001'], ['1.000000000', '6.7'], ['-8,9', '6.77'], [-2, 11], [-6.104752540884294, -9.876], ['-8,9', -7.934743523840704], [-9.514520957128042, -6.104752540884294], [-9.05245650953129, -8.997546011069746], [-11.11171337843259, -11.931240615627274], [2.091017020991142, 2.091017020991142], [-5.403249230556667, -5.403249230556667], ['116.700000001', '-9.2'], [-9.686625445264218, '-9.123'], [3.1711504871820364, 3.14], ['116.7000000001', '116.700000001'], [0, '-22'], [-11.651945761505571, -11.651945761505571], ['1,250', '11.0000000100'], [-4.636255829707621, 3.1711504871820364], ['-22', '-22'], ['11.0000000100', '11.0000000100'], ['-9', '-9.123'], [3.14, 2.091017020991142], ['-2.73', '-2.03'], ['-2.03', '-2.03'], [-5.980190696257784, '3'], ['-33.023', '-3.023'], ['6.7', '-2.0'], [3.865653910216933, 4.073918637875315], ['31.2', '33'], ['-2.023', '-2.03'], [-5.980190696257784, -9.514520957128042], [-8.374241519953129, -8.374241519953129], ['23', '-9.123'], [-3, 1.8062716857029506], [3.1711504871820364, 3.1711504871820364], ['-2', '-22'], [-6.104752540884294, 1.6388390454446027], [-5.980190696257784, 2.079441987825791], [3.5119518593157366, 2.506774567617957], [-6.410274451315487, '-2.00'], ['116.7000000001', '-6.7'], [-6.410274451315487, '1.00000001'], ['-8,9', '6.7'], [1, 3.14], [1.8180729788847423, 1.7876030675945356], [-8.906662049468062, -7.654], [-5.980190696257784, -9.804910491929277], [-11.651945761505571, -12.944537034527363], ['-89', '-8,9'], [1.1541131551442234, 2.1344375030805596], [-9.707613442054273, -9.707613442054273], [-8.906662049468062, -11.11171337843259], ['23', '33'], [4.063414424831626, 4.073918637875315], ['31.23', '1.23'], [-11.617559750797245, -9.707613442054273], [-11.651945761505571, -9.05245650953129], [1.8062716857029506, -9.514520957128042], ['-9.123', '-26.73'], ['-2.73', '116.700000001'], [4.063414424831626, -9.755810211622222], [-9.208288330318375, '-9.123'], [0, 49], ['1,5250', '11.00000001'], [-11.651945761505571, 1.1541131551442234], [-7.7849907211524485, -8.997546011069746], ['1.00000001', '11.00000001'], [-9.804910491929277, 2.8877032195044543], ['-29.123', '-21.00000001'], [1.8180729788847423, -9.514520957128042], ['1.000000001', '-29.123'], [3.898938614903911, 3.1711504871820364], [-8.543777712835121, -7.654], ['-2.00', '3.0'], ['-26.73', '11.0000000100'], ['1.2', '-2.00'], [-4.636255829707621, -11.651945761505571], ['1,45', '-21.00000001'], [-11.651945761505571, -18.187100371299287], ['3.0', '116.700000001'], ['116.7000000001', '-9.123'], ['1.000000001', '11.0000000100'], ['-2.03', '11.000000010'], [2, 2], [1.9155795783061915, -11.651945761505571], [4.452161057484629, 2.506774567617957], [1.8180729788847423, 1.8180729788847423], ['3.', '116.700000001'], ['-9.2', '-9.123'], [3.5119518593157366, 4.452161057484629], ['-9.2', '-9.2'], ['116.700000001', '1.0001'], ['.2', '.2'], [2.6874712351441374, -9.514520957128042], ['.2', '-9.123'], [0, 2], [-4.636255829707621, 3.865653910216933], ['.2', '-2.023'], ['-9.1213', '-9.1213'], ['31.2', '-9.2'], [-11.651945761505571, 4.073918637875315], ['3.', '33.'], ['23', -11.11171337843259], [-11.651945761505571, -8.997546011069746], ['-2.023', 11], [-9.686625445264218, -9.686625445264218], [1.7459388376772054, 1.322437089578019], [-7.934743523840704, 2.226295551080672], ['-6.72', '1.00000001'], [2.2929741837650237, 1.322437089578019], [4.063414424831626, 3.14], [4.031158731806144, -9.514520957128042], [-3, 12], [0, 11], ['3.0', '1.2'], ['1123700000001', '116.700000001'], [-2, 1.8062716857029506], [-9.707613442054273, -9.686625445264218], [-4.636255829707621, -15.114554817875211], ['-21.00000001', '-21.00000001'], [1.6388390454446027, 1.6388390454446027], ['-99.2', '-99.2'], [1.8180729788847423, -6.410274451315487], [-11.651945761505571, 0.2002599393512665], ['8,9', '-8,9'], [-9.804910491929277, -9.686625445264218], [-7.187050569843611, 2.1344375030805596], ['31.23', '1.000000001'], [-3, -4], [4.031158731806144, -9.804910491929277], [3.898938614903911, -5.403249230556667], [2.6874712351441374, 2.6874712351441374], [12, 2], ['-9.2', '11.0000000100'], ['1.000000001', '1.0000001'], ['-9.2', '00100'], [1.6412621306995587, 1.6388390454446027], [-18.187100371299287, -6.410274451315487], ['-3.023', '-2'], [1.6388390454446027, -11.931240615627274], ['1123700000001', '3.0'], ['1.0010000001', '1.000000001'], ['111.0000', '11.0000000100'], ['-22', '-26.73'], [3.8141252898018707, 3.7057202433370326], ['-9.123', '-9.1323'], [3.865653910216933, 2.6874712351441374], [-5.980190696257784, -6.631137567433889], ['-2.0', -7.654], [3.5119518593157366, -9.707613442054273], ['-20.03', '11.000000010'], [-4.076712034563361, -9.05245650953129], [1.6388390454446027, 2.8877032195044543], [-6.410274451315487, '00'], [11, 1], ['31.2', '-9.123'], [3.5605751592559205, -9.876], ['00100', '1.23'], [4.063414424831626, -9.208288330318375], [-5.403249230556667, -6.410274451315487], ['1.25', '-9.123'], [-7.934743523840704, -7.934743523840704], [-9.344465870872105, -8.468456444880985], ['1.0010000001', '11.000000010'], [-3, '0'], ['-9.123', '1.000000000'], ['116.700000001', '-9.92'], ['1.001', '-6.7'], ['33.', '116.700000001'], ['-9.', '-9.2'], [-4, -4], ['-9.11223', '-9.11223'], [1.5604055856320835, 1.1541131551442234], [4.073918637875315, 4.452161057484629], [3.7057202433370326, 3.7057202433370326], ['-6.72', '-9.123'], [-3.105257478570193, -4.636255829707621], ['-9', '-93.123'], [-8.468456444880985, 5.408759332706278], ['11.0000000010', '11.0000000010'], ['-20.03', '116.7000000001'], [-13.993306012707142, 3.5119518593157366], [-11.651945761505571, 3.14], [-5.403249230556667, -9.755810211622222], [-20.35575943991219, -8.468456444880985], [2.1344375030805596, 4.452161057484629], [-5.129467798985429, -7.654], ['1.00000001', '-9.123'], [-11.328754454519512, '.2'], [-8.906662049468062, -11.210098728611017], [12, 1], ['-2201', '-212.00000001'], [3.898938614903911, 3.898938614903911], [-9.876, -6.104752540884294], [-9.755810211622222, 3.865653910216933], [-6.104752540884294, 1.4502280067005207], ['.2', '1232'], [3.14, 1.9155795783061915], [3.5605751592559205, -13.304004571051902], [-18.187100371299287, -8.468456444880985], ['1.000000000', '-9.1233'], ['1,5250', '1,5250'], [-5, -4], [-8.056337912443711, -8.997546011069746], ['11.000000010', '11.000000010'], [1.9155795783061915, 1.9155795783061915], ['33', '116.7000000001'], [-11.651945761505571, 0.6862384998319798], [3.14, 1.3891044281947666], ['-26.73', '.2'], [10, 11], [-12.623799923993685, -11.651945761505571], [0, 48], [-11.651945761505571, -11.328754454519512], [1.5604055856320835, 1.5604055856320835], [-9.686625445264218, -9.707613442054273], [-11.05875160279082, -11.651945761505571], [2.1873356443842775, 1.9155795783061915], [-6.484980695659161, -6.642959048484541], ['1,20', '-3.023'], [3.5119518593157366, 1.4502280067005207], [-9.064301674215525, -8.997546011069746], [-13.962701352806974, '-9.123'], [-9.804910491929277, 4.073918637875315], [2.581352134350697, 3.14], [0.8812652369326962, 1.1019679079350322], [-5.436029261483907, -9.876], ['-30.023', '-9.123'], [11, -3], [-7.934743523840704, 1.1541131551442234], [-22.122410199397468, -8.468456444880985], ['-9', '3.0'], [1.910960686555556, 3.865653910216933], [1.5604055856320835, -4.636255829707621], [-5.436029261483907, -5.436029261483907], [-13.056145599512103, 3.5119518593157366], [2.1344375030805596, -13.962701352806974], [-6.887985839769855, -8.906662049468062], ['11.000000001', '1,5250'], [-3, 49], ['1,20', '1,20'], [1.6388390454446027, 2.0493903471747634], ['.2', '-9.92'], [1.7459388376772054, 1.7459388376772054], ['1,250', '-9.1213'], [-11.617559750797245, -9.514520957128042], [1.5604055856320835, 3.865653910216933], [2.226295551080672, 1.4502280067005207], ['-9.1213', '-91.1213'], [2.091017020991142, 2.971135439138305], [-15.114554817875211, -13.962701352806974], ['116.700000001', '1.0010000001'], ['-8,99', '-8,9'], ['00100', '00100'], ['-2.0300', '1232'], ['1.3323', '31.23'], ['-29.123', '116.700000001'], ['-2.0300', '-8,9'], [2.226295551080672, 1.9861619902493355], [3.898938614903911, 4.044626695207136], [-8.056337912443711, -4.636255829707621], ['11237000000011,5250', 1.322437089578019], [-6.887985839769855, -8.976482342288637], [2.581352134350697, -12.38768626074286], [-13.962701352806974, -5.980190696257784], [3.14, 2.7956678864919873], [3, -4], [3.14, 4.488747947339361], [1.3891044281947666, -6.104752540884294], [-63, 10], [4.063414424831626, -11.617559750797245], ['116.7000000001', '1,250'], [2.1964045622059976, 1.8830987968399917], [-3, 2.971135439138305], ['31.23', '-2.023'], [1.8062716857029506, -8.374241519953129], [1.1541131551442234, 1.1541131551442234], [1.4502280067005207, -15.114554817875211], [-5.403249230556667, -13.962701352806974], ['150', '51,250'], ['1.0010000001', '6.7'], [2.226295551080672, 2.226295551080672], [4.419932179709408, 1.322437089578019], [0, 10], [-9.876, 5.408759332706278], [1.784943491672312, 2.0493903471747634], [-11.94746282248088, -11.651945761505571], [1.322437089578019, 1.322437089578019], [2.226295551080672, -7.934743523840704], [-9.804910491929277, 2.757142833975825], [1.6412621306995587, 1.6412621306995587], [2.2669562582463536, 1.8062716857029506], [1.2806826733888153, 2.6845541156529644], [-5.980190696257784, 2.6874712351441374], ['-9.2', '51,250'], [-9.707613442054273, 3.5605751592559205], [-9.514520957128042, 2.1964045622059976], [-14.862049118108715, -12.000815116055994], ['1123700000001', '1123700000001'], ['3', '33.0'], [1.5700165584201082, 1.1541131551442234], [1.1019679079350322, 1.1019679079350322], [-12.944537034527363, -12.944537034527363], ['-2.0', '3.0'], [-9.514520957128042, -9.208288330318375], ['1,250', '1,2550'], [-22.122410199397468, -9.876], [2, 49], [-9.208288330318375, -8.997546011069746], ['-21.00000001', '33.'], [-9.514520957128042, -7.654], [-11.617559750797245, -11.617559750797245], [-5.980190696257784, -15.114554817875211], [1.6412621306995587, -7.654], [-6.104752540884294, 1.9455316441084491], [1.9155795783061915, 3.1711504871820364], [2.1140423577676475, 1.6388390454446027], ['11.00000001', '11.00000001'], [1.8062716857029506, -8.997546011069746], [-7.654, -9.804910491929277]]
    results = [2, 2.5, 3, 6, '2,3', '6', '2', None, None, None, None, 2.5, None, 5000, None, None, '-4.0', 3, 1, '77.3', 10, -1.0425166390148266, 4999, '773.3', 1, '7.3', 5000, 5000, 4999, '7.3', 10, '7.30', '77.3', 5001, 5001, None, 5001, 2.5, 10, 10, 11, None, -1, None, 10, 4999, None, 5001, 5000, 5000, 2, None, 0, 3, 3, '77.3', 5001, 5001, 2.5, 2, -1, 2, None, 10, 5002, None, 2, 4999, 9, None, 1, -2, '11.0', '7.3', 5000, 5002, 5000, None, '7.3', 5002, 41, None, 5002, None, 1, 2.5, '77.3', 41, 5000, '10.0', 3, None, 5002, 5002, 10, 11, 5000, 1.496091849454374, 4999, '7.33', 2, '7.3', 10, 40, None, '05,000', '77.3', 3.14, '-9.123', -7.654, '1,45', '6.7', None, None, None, '1.00000001', None, '1,45', '15,415', '3', '6.7', '1,45', None, '1,45', '1.25', '6.7', None, '15.25', -7.654, '7', 1, '1.125', '1,45', '41,45', -8.74973784205587, None, '-9.12', '1.25', '15.25', -3, '1.25', None, '3', None, '00', '1.23', None, '3', '6.7', '1,250', '3.0', None, '15,415', None, -2, 3.14, '41,45', None, '-2.0', -7.014581866391794, '1.25', None, '16.7', None, '1,45', '1,45', '1,45', '33', '00', -4.51094653769451, '33.0', '1.23', '1.23', None, '15,415', '6337', None, '0', '63371.25', '1.23', None, '33.0', '1.225', '1.25', '0', '415', -12.774935986016603, '.0', '1.25', None, '1,', None, '2151,250', -1, -7.014581866391794, None, '415', '1.25', None, 34, None, '41,45', '11.23', '1.1', None, '1.2', '33', '1.23', '63371.25', '115.25', '1,45', '1,45', 34, None, '333', 3.14, '-2.000', '1.1', None, '16.7', '1.03', '3.0', '415', '33', '330003', -6.4514534689514935, '63371.25', '1.2', '11', '00', '000', 11, None, '41,45', '63371.25', '115.25', '4,45', '16.7', -7.014581866391794, '1.205', '1.20000', None, '41,45', 34, '33', '15', '1.323', -7.014581866391794, '6337', 34, '16.7', None, -8.298650833465093, '333', None, None, 35, '21.25', '5', 34, None, None, '415', '3113', '3', '6.7', '63371.25', '21.20', '63371.25', -5.75363867961704, '11', '13.323', '11', 12, -7.654, 84, -1, '13.323', '15.25', '145', 35, '-2.000', '3300', '3,415', '3415', '21.25', None, 2.767386384178415, '000', None, '5', 2.767386384178415, '41,45', '-6.00075', -8.900537956858544, '1.11', '7', 84, '15,4115', '1.33000323', '21.25', None, '63371.25', -5.75363867961704, '6337', '11.1', 3.712550934925414, '1.25', None, '6.7', -4.5668177959472835, None, 70, '125', '15,41', '1.00000001', '115.25', '11.23', -7.654, '1.125', '6.7', None, 11, '41,4', 70, None, 11, None, '44', '41,45', '151,411115', '3415', '1.23', '1.215', None, '1.23', '1225', None, '1415.23', '15,41', '13.02125', None, '77', -3, '11', '115.25', -7.654, -7.654, '000', '1415.23', '115.25', 1, '3.0', '41,45', '3415', '1.03', '-8,9', 3.14, '1.11', None, None, '15,4115', 2.8215418518706716, '13.02125', '41,4', -10.397627547678898, '11.23', '7', '1.20000', 33, None, 34, '1225', '1.25', 4.569736337135209, None, '145', '000', 35, None, '155', 36, '000', '151,411115', '63371.25', -7.014581866391794, '3333300', -8.648925493228285, '00', '0', '415', None, '1', -5.75363867961704, None, '3,415', -8.226976895748662, '1.205', '115.25', -6.4514534689514935, None, 38, '15500', 4.569736337135209, '11.23', '16.77', '77', '12257', None, '63371.25', '11.125', '55', '03415', '1,5', '1,45', None, '11', '.0', -8.648925493228285, '2151,250', '12251', '-9.12', '41.22515', '1.2155', '33.0', '1.233', '1.0000', '41,455', '415', '1.125', '4,45', None, '63371.25', -4.5668177959472835, '3333', '3333', 84, '41,45', 84, '41,4', '-9.12', '151.25', '12257', '1,45', '155', -2, -4.51094653769451, '6337', '12215', '16.77', '1.02205', 75, None, '155', -7.014581866391794, '1,5', 84, '3333300', '444', '1.2205', -7.915238266264661, '15500', '777', '3300', None, '03415', -7.654, '0011', '1.5', 34, '111', -7.014581866391794, -69.38740384414959, '151.25', '-9.12', None, '11.23', -5.649489992448723, 0, '1.000000001', None, '1.25', '0', '55', '3113', '1.2333330025', '0', '77', '13415,5451', '01.03', 35, None, -8.298650833465093, 34, None, '-2.0', -9.876, '1,45', None, '-2.0', '1,545', None, None, '21.125', '1.5', 2, '1,250', '111.23', '15,41', '1.33003', '1.2205', '-2.0', '11.23', None, '13415,5451', 11, '-6.00075', '33', 1, -4.9122923154404425, None, 38, '9.1', '6337', -7.915238266264661, '77', '3333', None, '-2', None, '63371.275', '15500', '3415', -5.649489992448723, '1.205', 12, '1.22205', '115', '55', '33', '12251', '1.5', '13.02125', '3333', '1.2155', '33', '-15,41159', '1,45', None, '215150', '1,4', '11.23', '41,4', '115.255', -4.51094653769451, '41533', '1.020000', '414', -7.654, '15500', None, 3.14, None, '11.1', '3,415', '01.03', '3,44115', None, None, '115', '1.2333330025', '3113', '77', None, -9.876, '15500', '12215', None, None, '13.323', '16.7', -5.75363867961704, '1.2205', None, '1,45', '1.2125', 3.712550934925414, 2.767386384178415, -9.084182019357039, '701.037', '9.1', 75, '13.323', '1.03', '1.123', '15,4115', 0, '155', '13.323', -5.75363867961704, '11', '155', '12.2155', '1225', '71.33003', '44115', None, None, 2, None, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, -1.0, '5,1', '1.1', None, None, -9.876, '-9.123', None, -7.654, 0, '-9.123', None, '-3.023', '-9.123', 3.5098365670180556, 0, '0', '1.25', 3.5098365670180556, '1,250', '1.2', '1,45', '1.00000001', '-2', '1.00000001', '1.2', None, 4.452161057484629, None, None, '-9.123', '-2.03', '1,250', '11.000000010', -9.707613442054273, '11.000000010', '11.00000001', '.2', '-2.0', '-3.023', '-2', None, -9.514520957128042, None, '23', 3.14, 11, -8.997546011069746, -9.514520957128042, -5.403249230556667, '-2.0', 11, -8.997546011069746, '1.00000001', '-2', '0', -9.876, None, '1,250', 2.506774567617957, None, '23', 2.506774567617957, '1.000000001', -4.636255829707621, '3', '1.23', '11.000000010', '1.00000001', -9.876, None, '0', '116.700000001', '1.000000001', None, '6.7', '6.77', 11, -6.104752540884294, -7.934743523840704, -6.104752540884294, -8.997546011069746, -11.11171337843259, None, None, '116.700000001', '-9.123', 3.1711504871820364, '116.700000001', 0, None, '11.0000000100', 3.1711504871820364, None, None, '-9', 3.14, '-2.03', None, '3', '-3.023', '6.7', 4.073918637875315, '33', '-2.023', -5.980190696257784, None, '23', 1.8062716857029506, None, '-2', 1.6388390454446027, 2.079441987825791, 3.5119518593157366, '-2.00', '116.7000000001', '1.00000001', '6.7', 3.14, 1.8180729788847423, -7.654, -5.980190696257784, -11.651945761505571, '-8,9', 2.1344375030805596, None, -8.906662049468062, '33', 4.073918637875315, '31.23', -9.707613442054273, -9.05245650953129, 1.8062716857029506, '-9.123', '116.700000001', 4.063414424831626, '-9.123', 49, '11.00000001', 1.1541131551442234, -7.7849907211524485, '11.00000001', 2.8877032195044543, '-21.00000001', 1.8180729788847423, '1.000000001', 3.898938614903911, -7.654, '3.0', '11.0000000100', '1.2', -4.636255829707621, '1,45', -11.651945761505571, '116.700000001', '116.7000000001', '11.0000000100', '11.000000010', None, 1.9155795783061915, 4.452161057484629, None, '116.700000001', '-9.123', 4.452161057484629, None, '116.700000001', None, 2.6874712351441374, '.2', 2, 3.865653910216933, '.2', None, '31.2', 4.073918637875315, '33.', '23', -8.997546011069746, 11, None, 1.7459388376772054, 2.226295551080672, '1.00000001', 2.2929741837650237, 4.063414424831626, 4.031158731806144, 12, 11, '3.0', '1123700000001', 1.8062716857029506, -9.686625445264218, -4.636255829707621, None, None, None, 1.8180729788847423, 0.2002599393512665, '8,9', -9.686625445264218, 2.1344375030805596, '31.23', -3, 4.031158731806144, 3.898938614903911, None, 12, '11.0000000100', '1.0000001', '00100', 1.6412621306995587, -6.410274451315487, '-2', 1.6388390454446027, '1123700000001', '1.0010000001', '111.0000', '-22', 3.8141252898018707, '-9.123', 3.865653910216933, -5.980190696257784, '-2.0', 3.5119518593157366, '11.000000010', -4.076712034563361, 2.8877032195044543, '00', 11, '31.2', 3.5605751592559205, '00100', 4.063414424831626, -5.403249230556667, '1.25', None, -8.468456444880985, '11.000000010', '0', '1.000000000', '116.700000001', '1.001', '116.700000001', '-9.', None, None, 1.5604055856320835, 4.452161057484629, None, '-6.72', -3.105257478570193, '-9', 5.408759332706278, None, '116.7000000001', 3.5119518593157366, 3.14, -5.403249230556667, -8.468456444880985, 4.452161057484629, -5.129467798985429, '1.00000001', '.2', -8.906662049468062, 12, '-212.00000001', None, -6.104752540884294, 3.865653910216933, 1.4502280067005207, '1232', 3.14, 3.5605751592559205, -8.468456444880985, '1.000000000', None, -4, -8.056337912443711, None, None, '116.7000000001', 0.6862384998319798, 3.14, '.2', 11, -11.651945761505571, 48, -11.328754454519512, None, -9.686625445264218, -11.05875160279082, 2.1873356443842775, -6.484980695659161, '1,20', 3.5119518593157366, -8.997546011069746, '-9.123', 4.073918637875315, 3.14, 1.1019679079350322, -5.436029261483907, '-9.123', 11, 1.1541131551442234, -8.468456444880985, '3.0', 3.865653910216933, 1.5604055856320835, None, 3.5119518593157366, 2.1344375030805596, -6.887985839769855, '11.000000001', 49, None, 2.0493903471747634, '.2', None, '1,250', -9.514520957128042, 3.865653910216933, 2.226295551080672, '-9.1213', 2.971135439138305, -13.962701352806974, '116.700000001', '-8,9', None, '1232', '31.23', '116.700000001', '-2.0300', 2.226295551080672, 4.044626695207136, -4.636255829707621, '11237000000011,5250', -6.887985839769855, 2.581352134350697, -5.980190696257784, 3.14, 3, 4.488747947339361, 1.3891044281947666, 10, 4.063414424831626, '116.7000000001', 2.1964045622059976, 2.971135439138305, '31.23', 1.8062716857029506, None, 1.4502280067005207, -5.403249230556667, '150', '6.7', None, 4.419932179709408, 10, 5.408759332706278, 2.0493903471747634, -11.651945761505571, None, 2.226295551080672, 2.757142833975825, None, 2.2669562582463536, 2.6845541156529644, 2.6874712351441374, '51,250', 3.5605751592559205, 2.1964045622059976, -12.000815116055994, None, '33.0', 1.5700165584201082, None, None, '3.0', -9.208288330318375, '1,2550', -9.876, 49, -8.997546011069746, '33.', -7.654, None, -5.980190696257784, 1.6412621306995587, 1.9455316441084491, 3.1711504871820364, 2.1140423577676475, None, 1.8062716857029506, -7.654]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(compare_one)
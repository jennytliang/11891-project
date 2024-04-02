def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    
	Do not include these tokens in the code: 0 <=
	'''


    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c)/2
        return (p*(p - a)*(p - b)*(p - c))**0.5
    else:
        return -1

print(triangle_area(3, 4, 5))
print(triangle_area(1, 2, 10))




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
    inputs = [[3, 4, 5], [1, 2, 10], [4, 8, 5], [2, 2, 2], [1, 2, 3], [10, 5, 7], [2, 6, 3], [1, 1, 1], [2, 2, 10], [8, 9, 15], [10, 12, 15], [7, 7, 10], [3.6, 4.8, 6.1], [8, 15, 17], [6, 8, 10], [5, 5, 8], [9, 12, 15], [7, 24, 25], [2, 3, 4], [24, 23, 25], [7, 7, 7], [3, 5, 4], [24, 24, 25], [9, 11, 15], [6, 8, 4], [3, 23, 25], [2, 5, 4], [8, 9, 17], [3, 2, 3], [2, 9, 2], [5, 8, 8], [8, 15, 2], [10, 12, 3], [6, 17, 4], [7, 7, 11], [10, 8, 7], [9, 17, 17], [3, 3, 4], [24, 7, 5], [7, 23, 17], [6, 5, 10], [3, 22, 25], [22, 25, 25], [23, 17, 17], [6, 23, 10], [22, 25, 22], [8, 14, 2], [6, 24, 23], [4.8, 7.091641840978975, 6.1], [7, 11, 17], [12, 18, 8], [3, 4, 4], [12, 18, 3], [2, 17, 10], [24, 7, 6], [4, 10, 4], [6, 8, 6], [15, 7, 17], [2, 3, 3], [10, 7, 7], [8, 15, 4], [24, 25, 24], [2, 4, 7], [25, 25, 25], [7, 11, 16], [6, 5, 6], [5, 9, 6], [2, 2, 3], [4, 3, 23], [9, 8, 7], [16, 25, 22], [2, 1, 2], [3, 3, 3], [6, 23, 6], [1, 17, 4], [12, 13, 18], [18, 17, 17], [8, 9, 1], [8, 18, 1], [13, 9, 12], [7, 15, 15], [10, 8, 8], [9, 15, 15], [12, 8, 15], [10, 5, 5], [11, 18, 8], [12, 18, 17], [7, 15, 8], [4.8, 4.8, 4.8], [7, 17, 17], [9, 2, 3], [True, True, True], [8, 17, 8], [6, 17, 22], [9, 1, 7], [9, 8, 10], [6, 5, 5], [4, 15, 2], [25, 11, 15], [15, 1, 15], [5, 5, 10], [16, 1, 15], [6, 13, 6], [5, 5, 5], [3.6, 4.8, 3.961122069986524], [3.961122069986524, 4.8, 4.8], [16, 14, 18], [1, 4, 11], [15, 2, 15], [1, 1, 3], [3, 4, 7], [2, 2, 5], [1.5, 2.5, 3.5], [10000, 10000, 10000], [3, 3, 6], [10, 10, 20], [1.5, 2.4, 3.7], [2, 2, 4], [3, 4, 12], [1.5, 2.4, 2.4], [1, 20, 20], [1.5, 2.4, 1.5], [6, 10, 20], [1, 1, 4], [1.5, 2.243582514020111, 1.5], [1.5, 3.7, 2.4], [2.243582514020111, 3.5, 2.243582514020111], [3, 4, 3], [1.5, 2.5, 2.4], [12, 10, 20], [1.3641985205078329, 1.5, 1.3641985205078329], [10, 6, 20], [1.642992027072514, 2.4, 2.4], [3, 5, 6], [1.642992027072514, 2.5, 3.5], [12, 1, 3], [1, 2, 6], [1.5, 1.5, 1.5], [6, 10, 10], [12, 1, 1], [2.4, 1.4196153211881317, 2.4], [2.5, 4.195352879634535, 2.5], [10000, 11, 12], [5, 4, 6], [1, 10, 20], [4, 3, 10], [10, 6, 19], [4, 20, 4], [3, 5, 10000], [6, 10, 6], [1.5, 4.0558686746888934, 2.4], [12, 10, 7], [5, 12, 5], [4, 4, 20], [1.5, 3.7, 1.6354243288923729], [4, 1, 4], [12, 3, 1], [1, 5, 1], [20, 19, 6], [1.5, 2.1563641569599024, 4.0558686746888934], [2, 4, 2], [3, 10000, 7], [4, 12, 4], [7, 3, 6], [1.5, 1.642992027072514, 1.5], [2.1563641569599024, 1.4196153211881317, 2.4], [12, 10, 1], [11, 6, 19], [9, 6, 20], [12, 12, 3], [6, 4, 6], [1.642992027072514, 3.4498437377515523, 3.5], [6, 20, 20], [19, 12, 10], [5, 4, 4], [4, 10, 6], [6, 10, 21], [1, 21, 1], [1.5, 1.6608803064021642, 3.7], [1.5, 4.0558686746888934, 2.1678576332328428], [5, 11, 12], [10000, 11, 20], [12, 3, 3], [2.262075142531277, 2.1678576332328428, 1.3641985205078329], [4, 7, 4], [3, 12, 6], [6, 3, 3], [1.5, 3.7, 2.148304047537571], [4.0558686746888934, 2.4, 4.0558686746888934], [1.4196153211881317, 2.4, 2.4], [1.6354243288923729, 2.1563641569599024, 2.560595193053081], [1.5, 1.642992027072514, 2.1678576332328428], [10000, 10, 20], [6, 11, 12], [1, 2, 4], [2.33812767354038, 0.7033385138748636, 2.4], [1.5, 1.1510404896538393, 2.243582514020111], [12, 1, 2], [1.5, 2.5, 1.5], [0.8437220480478858, 4.157230829281458, 2.4], [11, 3, 11], [21, 19, 6], [1.5, 2.4430443203125956, 2.0977671953307357], [1.4196153211881317, 1.4196153211881317, 1.4196153211881317], [6, 4, 9], [20, 4, 8], [21, 5, 10], [13, 11, 12], [18, 6, 21], [5, 10000, 10000], [2, 3, 11], [2, 4, 4], [0.9326237111951746, 2.4, 2.4], [6, 13, 3], [2.262075142531277, 2.1678576332328428, 0.6542952965279305], [5, 12, 12], [2.084281061132473, 2.5, 0.9326237111951746], [17, 6, 21], [2, 3, 18], [2, 1, 4], [2.5, 3.4498437377515523, 3.7], [1.3641985205078329, 2.243582514020111, 1.5], [4.157230829281458, 4.0558686746888934, 2.4], [1, 5, 20], [20, 20, 6], [2.4430443203125956, 2.4, 1.9698229422274585], [10, 20, 18], [3, 6, 6], [10, 13, 17], [12, 13, 6], [0.622155751870696, 2.084281061132473, 2.5], [10, 1, 9], [10, 6, 10], [21, 10, 10], [11, 3, 4], [9, 13, 19], [1.200314718419552, 1.1926090998134464, 2.7631966786277014], [10000, 20, 6], [2.243582514020111, 1.5, 1.5], [3, 10000, 6], [10, 3, 2], [2.5, 4.442719755691903, 3.7], [6, 11, 21], [12, 3, 8], [6, 13, 2], [2.5, 4.195352879634535, 2.243582514020111], [1.3641985205078329, 2.243582514020111, 1.267558555857357], [2.262075142531277, 2.1678576332328428, 2.262075142531277], [6, 10000, 6], [18, 20, 21], [12, 4, 6], [13, 20, 20], [11, 4, 4], [12, 3, 17], [9999, 10000, 7], [3.9329677858307948, 2.128791392500959, 1.267558555857357], [4.0558686746888934, 0.7033385138748636, 0.7033385138748636], [2.4, 2.4, 2.4], [3, 7, 7], [21, 3, 10], [12, 6, 6], [19, 1, 4], [10000, 10000, 10001], [7, 6, 5], [1.8341166265297297, 1.5, 1.5], [4.0558686746888934, 1.8223871525574837, 4.0558686746888934], [2.3974882322548865, 2.4, 1.9698229422274585], [2.128791392500959, 1.6354243288923729, 2.1563641569599024], [1.3641985205078329, 2.243582514020111, 2.3432505278674434], [9999, 6, 9999], [5, 20, 4], [12, 3, 2], [19, 6, 19], [2.4, 2.1647966283290505, 2.038421077762675], [1.6608803064021642, 0.6542952965279305, 1.6608803064021642], [6, 4, 12], [3.4498437377515523, 3.7, 3.7], [2.084281061132473, 2.1678576332328428, 0.6542952965279305], [8, 10000, 6], [1, 4, 4], [4, 12, 12], [1, 3, 4], [1, 5, 2], [4.157230829281458, 2.4, 2.4], [9, 9, 9], [3, 6, 3], [6, 19, 20], [1, 6, 2], [11, 9, 11], [4, 6, 2], [9, 12, 9], [2.1647966283290505, 2.4, 2.4], [8, 9999, 10000], [10, 5, 9], [1.3641985205078329, 0.8706143907765709, 2.243582514020111], [2, 5, 2], [2, 3, 17], [2.128791392500959, 2.243582514020111, 1.5], [6, 2, 7], [1, 6, 10], [8, 9, 9], [1.8271158639570797, 2.262075142531277, 0.6542952965279305], [3, 2, 11], [7, 13, 2], [10, 20, 3], [3.4498437377515523, 2.8483563393502944, 2.33812767354038], [3, 19, 4], [2, 10001, 2], [1.5, 1.9329103191414176, 2.4430443203125956], [1.8271158639570797, 2.262075142531277, 0.686661599347447], [1.3985411647382533, 4.0558686746888934, 2.1678576332328428], [1.5, 2.5, 0.8706143907765709], [3, 8, 3], [8, 3, 2], [9, 5, 13], [21, 6, 10], [2.1678576332328428, 2.1678576332328428, 2.1678576332328428], [0.9426819238709225, 2.33812767354038, 2.33812767354038], [4, 10001, 13], [3, 6, 4], [4.07628098856003, 4.0558686746888934, 4.07628098856003], [2.4, 2.2818215819260073, 2.494614380837856], [10000, 17, 17], [4, 18, 19], [12, 6, 4], [17, 3, 17], [1.5, 1.9329103191414176, 1.9329103191414176], [1.642992027072514, 3.131397785578148, 3.1721622755476457], [10, 6, 12], [13, 21, 13], [21, 13, 13], [11, 9, 10], [18, 6, 10], [21, 20, 10], [20, 10, 4], [10001, 12, 10001], [12, 6, 7], [1.200314718419552, 0.9463641485630762, 2.7631966786277014], [5, 6, 6], [9999, 6, 6], [11, 13, 9], [1.5, 2.038421077762675, 1.6354243288923729], [10000, 1, 21], [0.8437220480478858, 4.157230829281458, 1.6629322548740264], [12, 3, 12], [2.2430034847370095, 1.200314718419552, 1.5], [20, 11, 12], [11, 13, 8], [3, 6, 7], [1.7425763109349286, 2.036174656564886, 2.036174656564886], [1, 21, 21], [21, 4, 13], [3, 19, 19], [1, 3, 1], [1.6161161492974772, 2.4430443203125956, 1.6161161492974772], [9, 4, 4], [8, 2, 2], [2.5, 0.8706143907765709, 2.5], [17, 12, 12], [4, 3, 4], [4.0558686746888934, 0.7033385138748636, 2.262075142531277], [1.5, 2.4430443203125956, 1.82003153357376], [2.1678576332328428, 1.2865323183268573, 2.1678576332328428], [2.4, 2.2692536905847067, 2.4], [2.1647966283290505, 3.1362954706820205, 0.7547267194279496], [1, 5, 4], [0.6542952965279305, 0.6542952965279305, 0.6542952965279305], [12, 11, 7], [10000, 5, 10000], [2.1647966283290505, 3.1362954706820205, 3.1362954706820205], [19, 13, 10], [2.5, 4.195352879634535, 4.195352879634535], [9, 11, 5], [4, 3, 8], [3.131397785578148, 2.036174656564886, 2.036174656564886], [1.8942368652837256, 1.5, 3.7], [5, 20, 20], [10001, 2, 12], [9999, 6, 3], [2.374627814375018, 2.1678576332328428, 1.2865323183268573], [1.642992027072514, 3.4498437377515523, 1.1926090998134464], [10001, 3, 4], [19, 19, 19], [1, 3, 9999], [1.6161161492974772, 2.4, 1.6161161492974772], [10, 4, 10], [9999, 10000, 9999], [3.0403331185139235, 2.5, 0.9326237111951746], [10, 10, 4], [10001, 6, 10000], [3, 9, 3], [1, 1, 12], [1.200314718419552, 2.4, 1.4196153211881317], [10000, 1, 10000], [8, 13, 3], [1, 6, 11], [1.5, 2.2818215819260073, 2.4430443203125956], [2.1678576332328428, 2.1678576332328428, 4.0558686746888934], [1, 20, 11], [3.3846415256380586, 2.7631966786277014, 0.7033385138748636], [12, 3, 10000], [9, 3, 3], [2.1563641569599024, 1.7425763109349286, 1.8467976059297913], [10000, 10, 17], [1.6951729635583077, 1.5, 1.3641985205078329], [10000, 1, 11], [1.9419930401569185, 1.5, 1.3641985205078329], [11, 10000, 11], [20, 4, 20], [9999, 10, 9999], [4, 4, 13], [10000, 9999, 10000], [5, 7, 6], [1.4196153211881317, 0.9326237111951746, 3.2842576395462033], [5, 20, 6], [3, 5, 18], [0.8437220480478858, 5.3599327367069565, 2.1678576332328428], [2.3974882322548865, 2.4, 2.3974882322548865], [8, 3, 6], [20, 2, 3], [1.3985411647382533, 2.1678576332328428, 2.1678576332328428], [1.3641985205078329, 2.2818215819260073, 2.4430443203125956], [3.7, 4.9453223141324845, 1.6354243288923729], [2.547296836044605, 2.262075142531277, 1.5], [1.3641985205078329, 1.8942368652837256, 2.4430443203125956], [10, 5, 17], [4, 17, 13], [4.0558686746888934, 0.7186421266908659, 0.7033385138748636], [2.1678576332328428, 1.6354243288923729, 4.0558686746888934], [10000, 17, 10000], [3.0403331185139235, 0.9426819238709225, 2.547296836044605], [1.8617258937082115, 1.5, 1.5], [12, 7, 6], [4, 20, 20], [1, 21, 11], [5, 10000, 5], [4, 6, 4], [18, 2, 3], [1, 2, 1], [2.1678576332328428, 1.2865323183268573, 2.4292543231973256], [2.4, 2.1647966283290505, 1.9329103191414176], [2.4, 4.195352879634535, 4.07628098856003], [2, 10000, 6], [4, 3, 5], [5, 2, 12], [2.4292543231973256, 0.6587933722848219, 2.1678576332328428], [1.5, 4.8599085277703695, 4.8599085277703695], [3, 6, 1], [10001, 2, 10001], [1, 5, 19], [6, 1, 2], [2.33812767354038, 0.8437220480478858, 1.267558555857357], [2.084281061132473, 0.6542952965279305, 0.6542952965279305], [7, 7, 12], [2.243154383102723, 2.5, 2.243154383102723], [2, 2, 12], [4.8599085277703695, 2.5, 2.4], [2.262075142531277, 2.1678576332328428, 2.1678576332328428], [10, 6, 2], [10000, 2, 12], [2.5736600105589718, 3.4498437377515523, 3.4498437377515523], [4.195352879634535, 4.761807742424063, 4.195352879634535], [7, 7, 6], [5.121265754105029, 1.5, 1.5], [21, 3, 9], [3.9329677858307948, 2.128791392500959, 2.128791392500959], [3.678124396317478, 4.9453223141324845, 1.6354243288923729], [4.9453223141324845, 1.6354243288923729, 3.678124396317478], [16, 17, 17], [1.6354243288923729, 2.8483563393502944, 2.1563641569599024], [2.4292543231973256, 1.3641985205078329, 1.5], [12, 10, 10], [10001, 8, 7], [11, 11, 4], [2.1678576332328428, 3.9329677858307948, 3.9329677858307948], [1.9329103191414176, 3.7, 3.7], [12, 12, 10001], [1.5, 1.6354243288923729, 1.6354243288923729], [1.3641985205078329, 2.457557909382755, 2.4430443203125956], [6, 7, 6], [3.678124396317478, 1.5, 3.7], [5.000194727632692, 2.4, 2.2818215819260073], [1.5, 1.3641985205078329, 1.3641985205078329], [14, 19, 10], [6, 12, 6], [3.7, 2.1563641569599024, 4.9453223141324845], [2, 20, 20], [7, 18, 18], [14, 11, 7], [5.000194727632692, 2.4, 1.4022164083137756], [17, 13, 20], [6, 6, 10000], [1.200314718419552, 1.1926090998134464, 2.0977671953307357], [2.4, 2.3065522317615503, 2.038421077762675], [5, 6, 5], [10, 6, 17], [21, 17, 12], [2.243154383102723, 2.243154383102723, 2.5], [3.794360538667089, 2.4, 2.2818215819260073], [1.267558555857357, 1.672462725576983, 1.672462725576983], [12, 4, 20], [19, 4, 20], [1.5, 3.7, 1.5], [5, 11, 11], [12, 10, 12], [2.457557909382755, 0.6542952965279305, 1.2865323183268573], [2, 10000, 10000], [17, 17, 3], [11, 20, 3], [5, 8, 3], [4, 3, 3], [0.6542952965279305, 2.1678576332328428, 4.0558686746888934], [1.9698229422274585, 1.6608803064021642, 1.6608803064021642], [10, 1, 12], [14, 11, 13], [12, 12, 6], [1.3641985205078329, 2.5736600105589718, 2.036174656564886], [1, 21, 12], [10001, 1, 16], [11, 12, 12], [2.3065522317615503, 2.5, 1.4196153211881317], [16, 11, 11], [1.5, 4.0558686746888934, 2.084281061132473], [1.5806722055724702, 1.3641985205078329, 1.3641985205078329], [3, 10001, 4], [4, 9, 4], [2.383272874482817, 2.547296836044605, 2.1678576332328428], [10, 2, 17], [1.31630964374628, 0.7033385138748636, 2.4], [10, 3, 10], [2.084281061132473, 2.5, 0.999057665066928], [16, 11, 10001], [0.8437220480478858, 2.1678576332328428, 0.8437220480478858], [2.128791392500959, 4.761807742424063, 4.195352879634535], [21, 21, 11], [2.5736600105589718, 2.084281061132473, 2.5], [8, 9, 10], [2.33812767354038, 0.5084534820362593, 2.4], [8, 13, 13], [4, 2, 2], [7, 5, 10001], [4.442719755691903, 2.444385575870246, 5.182676183528757], [2.5, 1.8942368652837256, 2.4430443203125956], [1.6161161492974772, 2.2818215819260073, 1.6161161492974772], [5, 11, 2], [1.5, 1.6629322548740264, 3.5], [6, 19, 6], [21, 19, 19], [1, 12, 1], [10, 5, 18], [0.7547267194279496, 5.000194727632692, 3.678124396317478], [4.195352879634535, 4.761807742424063, 4.379505351125754], [2.1678576332328428, 0.5084534820362593, 4.0558686746888934], [4, 12, 13], [9, 13, 8], [1.1172100175191195, 1.5, 1.5], [8, 12, 6], [20, 20, 4], [5, 6, 7], [1.5, 1.8763617511124884, 1.5], [12, 11, 8], [8, 8, 3], [2.560595193053081, 1.4196153211881317, 1.4196153211881317], [3, 14, 4], [13, 2, 2], [10, 10, 10], [3.2842576395462033, 2.128791392500959, 4.082623609596164], [1.5, 1.9419930401569185, 1.82003153357376], [2.6628618810103504, 2.2692536905847067, 2.4], [1.3641985205078329, 2.384080250520507, 1.3641985205078329], [4, 15, 14], [1.5, 1.9329103191414176, 2.3360169223640765], [2.33812767354038, 2.4, 2.4], [4, 19, 2], [9, 1, 4], [0.6287252629258216, 0.7547267194279496, 3.678124396317478], [5, 10001, 10000], [19, 6, 8], [2.383272874482817, 2.5130512703414154, 2.547296836044605], [7, 5, 7], [5, 8, 2], [3, 15, 4], [1.5, 1.201981374203674, 1.5], [10, 5, 10], [4.0558686746888934, 2.4, 4.579710571475333], [2, 4, 5], [19, 19, 18], [1, 10001, 2], [5, 20, 1], [1.4022164083137756, 2.6076642711640567, 1.1805686207244295], [7, 22, 21], [1.3641985205078329, 1.267558555857357, 1.3641985205078329], [8, 10, 6], [10001, 1, 4], [20, 3, 21], [1.4196153211881317, 2.4, 1.8617258937082115], [3.4498437377515523, 3.5, 3.5], [3.2842576395462033, 3.2842576395462033, 3.2842576395462033], [10, 20, 19], [1.3985411647382533, 1.3985411647382533, 1.3985411647382533], [3, 15, 11], [17, 10, 22], [7, 2, 19], [10000, 3, 17], [4, 3, 9999], [3, 18, 4], [5.121265754105029, 1.5, 1.8000031892339765], [1.200314718419552, 1.200314718419552, 1.5], [1, 1, 2], [10, 20, 30], [2, 3, 6], [0.5, 0.5, 0.5], [0.1, 0.2, 0.3], [1000, 1000, 1], [10000000000.0, 10000000000.0, 10000000000.0], [10000000000.0, 10000000000.0, 20000000000.0], [3, 19, 20], [10000, 1, 1], [2.5775891893369485, 2.4, 3.7], [19, 20, 19], [1.5, 1.5, 3.7], [10, 10, 3], [1.5, 0.8664110443033755, 3.7], [2.5775891893369485, 2.5775891893369485, 2.5775891893369485], [3, 2, 1], [2, 3, 5], [4, 12, 3], [3, 3, 2], [7, 3, 5], [11, 6, 11], [10000, 19, 10000], [20, 19, 20], [11, 9, 9], [9, 3, 5], [1.5, 0.503082583107345, 3.7], [2, 5, 12], [11, 19, 11], [11, 12, 4], [1.5, 3.3689705322719385, 3.8779389440890846], [3.7, 0.503082583107345, 1.5], [19, 21, 19], [3, 3, 9], [2.5775891893369485, 0.503082583107345, 3.4328160926834466], [2, 3, 1], [1.5, 2.5775891893369485, 2.5775891893369485], [1.5, 0.8664110443033755, 2.5], [11, 18, 11], [3, 1, 2], [18, 19, 10000], [2.5775891893369485, 3.7, 2.5775891893369485], [1.5, 1.9960886727799532, 1.9443319502273428], [20, 2, 4], [3.4328160926834466, 1.5, 1.5], [1.5, 0.8664110443033755, 1.9938336153289764], [2, 1, 1], [3, 3, 12], [4, 9, 3], [3.3689705322719385, 0.503082583107345, 3.5], [4, 3, 12], [11, 20, 11], [3, 21, 20], [3.5058221358099715, 1.9960886727799532, 2.5775891893369485], [6, 5, 2], [3.4328160926834466, 3.6335822420870274, 4.207085238320968], [4.207085238320968, 0.503082583107345, 3.4328160926834466], [1, 2, 5], [9, 9, 3], [1.9960886727799532, 0.8664110443033755, 3.7], [2.5775891893369485, 3.5, 2.5775891893369485], [1.9960886727799532, 4.207085238320968, 3.4328160926834466], [1, 9, 3], [19, 10000, 19], [9, 3, 9], [1.5, 3.5, 4.360176141608689], [10, 3, 3], [19, 9, 4], [3.246902781268715, 4.207085238320968, 3.4328160926834466], [1.7553134534575479, 2.5, 1.7553134534575479], [4.207085238320968, 2.5775891893369485, 1.9960886727799532], [1.9960886727799532, 1.5, 1.9443319502273428], [3, 21, 9], [0.503082583107345, 0.8664110443033755, 1.9938336153289764], [1, 6, 1], [6, 11, 6], [3.5058221358099715, 0.5309244958084296, 2.5], [10, 9, 6], [2, 10, 5], [7, 1, 1], [2, 5, 11], [3.7, 3.6335822420870274, 4.207085238320968], [3, 2, 2], [1.5, 1.9960886727799532, 4.917579198095192], [18, 1, 2], [3.3689705322719385, 3.246902781268715, 3.246902781268715], [10, 5, 2], [3, 21, 19], [6, 9, 20], [8, 5, 3], [1.5, 1.5, 3.4328160926834466], [6, 4, 19], [4, 4, 12], [2, 4, 3], [0.5373016430540158, 0.789022824347914, 1.5], [10001, 9, 3], [1, 1, 10], [1.0689146796445856, 1.9960886727799532, 4.917579198095192], [10, 11, 20], [10, 7, 10001], [1.9960886727799532, 1.5, 3.7], [11, 7, 11], [0.789022824347914, 4.163437455766259, 4.163437455766259], [4, 7, 11], [2.1577955006176532, 2.5775891893369485, 0.5309244958084296], [4.207085238320968, 0.789022824347914, 1.9960886727799532], [10, 3, 6], [1, 6, 10000], [1, 4, 3], [3.3689705322719385, 1.060745627088426, 3.5058221358099715], [1.5, 2.32075270734248, 1.5], [9, 9, 10], [6, 1, 1], [1.7804616625202718, 3.6335822420870274, 4.207085238320968], [20, 3, 19], [1.0689146796445856, 2.3063784440650927, 4.917579198095192], [0.5373016430540158, 1.9960886727799532, 4.917579198095192], [1.060745627088426, 0.503082583107345, 3.4328160926834466], [9, 4, 9], [3.367869620967685, 2.5775891893369485, 3.5], [1.2532845399179122, 2.32075270734248, 1.5], [2.5775891893369485, 0.5309244958084296, 3.4328160926834466], [2.5775891893369485, 0.503082583107345, 3.784199020712859], [4.207085238320968, 0.503082583107345, 4.207085238320968], [10, 10, 8], [19, 2, 4], [2.5775891893369485, 3.5, 3.5], [1.5, 2.4, 3.459071983029828], [3.4328160926834466, 2.32075270734248, 1.9960886727799532], [3.4328160926834466, 2.5, 1.7553134534575479], [7, 5, 6], [3, 10, 9], [2.201886913968485, 3.5, 3.4328160926834466], [11, 2, 11], [1.060745627088426, 4.360176141608689, 3.6335822420870274], [9, 20, 20], [7, 5, 12], [10, 9, 9], [20, 7, 4], [9, 5, 9], [9, 3, 6], [6, 20, 6], [20, 19, 19], [5, 5, 6], [8, 3, 9], [3, 10, 3], [2, 6, 5], [3, 3, 21], [0.789022824347914, 2.628975182302735, 4.163437455766259], [6, 11, 11], [2.1746667368809547, 0.8664110443033755, 3.7], [1, 19, 20], [3, 12, 4], [2, 2, 19], [4, 9999, 2], [9, 5, 5], [1, 11, 1], [10000, 4, 4], [4.163437455766259, 6.208338272407481, 1.9960886727799532], [2.5775891893369485, 3.5740269495384656, 3.5], [1.5, 2.367970294271218, 3.7], [3.4328160926834466, 4.207085238320968, 4.207085238320968], [9, 5, 3], [4.207085238320968, 4.64480014813984, 4.207085238320968], [1, 7, 2], [4.917579198095192, 1.5, 0.3411767253815125], [2, 11, 11], [2, 1, 19], [7, 8, 10000], [10, 20, 10], [9, 10000, 10], [4, 9999, 4], [1.9960886727799532, 1.5, 1.6321291998415466], [3.5740269495384656, 3.367869620967685, 3.5], [3.246902781268715, 3.246902781268715, 4.207085238320968], [9, 4, 12], [2.5775891893369485, 2.4, 2.8915419464931533], [18, 10001, 5], [1.5, 1.957944137251767, 1.5], [4, 4, 4], [12, 18, 11], [3, 3, 11], [2.7339212786584164, 4.917579198095192, 3.5], [20, 18, 20], [1, 9, 4], [11, 19, 10], [11, 9, 20], [6, 3, 6], [4, 4, 21], [2.32075270734248, 1.8696675963417573, 1.8696675963417573], [9999, 7, 5], [1, 9, 1], [9999, 3, 12], [2.1746667368809547, 2.628975182302735, 1.5], [20, 7, 7], [10001, 2, 11], [20, 3, 1], [3.5058221358099715, 2.625974596400467, 1.2452726682226072], [12, 12, 4], [2.32075270734248, 1.8696675963417573, 2.32075270734248], [11, 3, 3], [10001, 4, 3], [7, 5, 2], [8, 6, 3], [2, 19, 1], [10001, 2, 10], [3.246902781268715, 4.207085238320968, 3.246902781268715], [9998, 9999, 3], [2.2381102658017995, 3.4328160926834466, 4.207085238320968], [4, 2, 5], [9, 21, 6], [9, 7, 10001], [9, 2, 9], [10, 4, 20], [2.7809171317859325, 2.8915419464931533, 2.8915419464931533], [11, 9998, 11], [11, 11, 11], [4, 9999, 5], [20, 11, 11], [3, 10001, 21], [3.4328160926834466, 2.1577955006176532, 3.030511801987072], [2.7809171317859325, 0.3411767253815125, 2.8915419464931533], [9, 8, 10001], [5, 11, 6], [21, 8, 21], [1.7804616625202718, 3.6335822420870274, 1.7804616625202718], [2.9484977977737055, 3.367869620967685, 3.5], [3, 1, 1], [18, 3, 20], [3, 10001, 10001], [10, 19, 9998], [2.3815043434381975, 1.970201770310558, 2.628975182302735], [18, 12, 1], [20, 9998, 21], [8, 1, 9], [2.7809171317859325, 2.001423133273598, 2.8915419464931533], [8, 9, 9998], [9, 10, 3], [11, 10, 9], [1, 1, 9], [3, 19, 11], [11, 1, 11], [10000, 11, 11], [3, 3, 8], [0.37177963614389875, 2.5775891893369485, 3.358804199499412], [9, 2, 20], [2.4, 1.7804616625202718, 2.4], [0.789022824347914, 1.482460007714667, 1.9960886727799532], [3, 21, 12], [7, 4, 9], [3.3689705322719385, 3.5, 3.5], [3.7, 3.5316349895705246, 4.207085238320968], [2.9484977977737055, 3.0318420283066305, 3.5661060159465414], [10, 5, 6], [5, 6, 19], [9999, 9998, 7], [2.325585792582476, 3.0318420283066305, 3.4328160926834466], [2.5775891893369485, 0.40279626268882396, 3.4328160926834466], [11, 12, 5], [2.32075270734248, 0.503082583107345, 3.784199020712859], [3.7160244561805635, 2.5775891893369485, 2.5775891893369485], [4, 19, 4], [11, 5, 12], [3.246902781268715, 3.246902781268715, 2.4579482734138156], [2.32075270734248, 1.1315109995443282, 1.1315109995443282], [7, 1, 7], [3.5058221358099715, 2.625974596400467, 3.7], [11, 9, 3], [11, 11, 3], [3.5740269495384656, 0.503082583107345, 3.5740269495384656], [3.3689705322719385, 0.503082583107345, 3.8341243975029715], [9, 4, 8], [9, 8, 19], [4, 2, 4], [0.3411767253815125, 2.5775891893369485, 3.5], [7, 11, 11], [0.503082583107345, 0.3411767253815125, 3.784199020712859], [3.4328160926834466, 3.316856186690004, 4.207085238320968], [9, 10, 8], [2.5775891893369485, 4.917579198095192, 3.5], [7, 10, 11], [11, 12, 11], [9, 9998, 10000], [10001, 3, 20], [5, 6, 4], [4, 10, 3], [1.8696675963417573, 1.482460007714667, 0.789022824347914], [2.678861990883893, 3.5058221358099715, 2.678861990883893], [3.5740269495384656, 2.8915419464931533, 3.5], [7, 8, 1], [6, 7, 7], [6, 7, 5], [5, 3, 4], [2.1577955006176532, 0.5309244958084296, 2.1577955006176532], [2, 19, 19], [11, 11, 8], [7, 6, 7], [11, 10, 10], [2.5775891893369485, 0.5309244958084296, 0.5309244958084296], [9998, 6, 20], [4.917579198095192, 3.5058221358099715, 2.678861990883893], [21, 6, 7], [1.2807265265156114, 1.9960886727799532, 1.957944137251767], [3.5118964806288524, 0.5309244958084296, 0.5309244958084296], [1.1315109995443282, 0.5067302806822526, 3.7], [18, 5, 4], [3.6736564663845668, 3.4328160926834466, 2.5], [1.5, 4.917579198095192, 4.917579198095192], [2.4579482734138156, 2.5775891893369485, 0.5309244958084296], [10, 11, 11], [1, 4, 1], [10000, 10000, 9999], [19, 21, 10000], [20, 6, 20], [10, 10, 5], [2.367970294271218, 3.6335822420870274, 4.207085238320968], [9, 9998, 9], [21, 10, 21], [7, 11, 7], [18, 20, 20], [1.5, 3.5259793391344623, 4.958203166262308], [10, 10, 11], [1.060745627088426, 0.503082583107345, 2.685971027356751], [10001, 5, 5], [3.4328160926834466, 3.023833703810185, 1.7553134534575479], [19, 11, 11], [2.678861990883893, 1.482460007714667, 2.678861990883893], [2, 9, 5], [8, 4, 9], [9, 8, 21], [10, 3, 5], [5, 7, 5], [2.8915419464931533, 3.8444967857751786, 2.7809171317859325], [11, 9, 8], [9999, 18, 2], [10, 6, 6], [2, 10002, 10001], [1.8173129323162371, 2.5775891893369485, 3.4328160926834466], [9999, 6, 12], [1.5, 4.360176141608689, 2.5775891893369485], [3.5058221358099715, 3.4328160926834466, 0.503082583107345], [21, 19, 20], [2.2381102658017995, 2.620487660007657, 6.208338272407481], [2.592531646989002, 3.0318420283066305, 3.4328160926834466], [11, 11, 6], [21, 19, 10001], [0.52105239573242, 3.7, 3.7], [1.8495977887811454, 2.4, 2.7495530227213765], [4, 8, 4], [2, 3, 7], [9999, 2, 5], [2.3815043434381975, 3.7, 2.367970294271218], [3.7, 3.6335822420870274, 3.7], [10000, 9998, 7], [8, 3, 3], [3.784199020712859, 4.958203166262308, 3.784199020712859], [1.8696675963417573, 1.2807265265156114, 1.8696675963417573], [1, 9, 20], [20, 20, 20], [0.8317897724869179, 3.3689705322719385, 3.8779389440890846], [0.5309244958084296, 3.529512511196066, 1.9960886727799532], [3.4328160926834466, 4.705954992842067, 1.5], [3, 2, 8], [11, 19, 19], [6, 19, 19], [20, 21, 10], [1.2807265265156114, 3.5058221358099715, 3.5058221358099715], [3.1220118375734565, 4.64480014813984, 4.64480014813984], [1.475401013148001, 2.3136608539481305, 4.360176141608689], [21, 3, 1], [7, 3, 7], [8, 2, 9999], [1.9960886727799532, 2.5775891893369485, 2.5775891893369485], [3, 6, 5], [4, 9, 8], [10001, 19, 10001], [0.789022824347914, 2.7819271644061514, 1.9960886727799532], [20, 2, 20], [7, 1, 10002], [9998, 21, 21], [4.899278040010196, 4.958203166262308, 3.784199020712859], [2.5775891893369485, 1.2734979643607847, 2.377135444015496], [0.3411767253815125, 4.163437455766259, 6.208338272407481], [2.1746667368809547, 0.8664110443033755, 0.8664110443033755], [4, 1, 5], [3.5058221358099715, 2.625974596400467, 1.4996802745331441], [3.6335822420870274, 1.4996802745331441, 4.207085238320968], [19, 9999, 13], [2.678861990883893, 2.678861990883893, 1.482460007714667], [6, 18, 11], [10000, 3, 7], [4, 3, 10002], [11, 10, 8], [4.207085238320968, 0.503082583107345, 2.678861990883893], [4.782093300355605, 4.018999343642049, 2.8915419464931533], [4, 11, 8], [10001, 10002, 5], [3, 11, 11]]
    results = [6.0, -1, 8.18, 1.73, -1, 16.25, -1, 0.43, -1, 29.93, 59.81, 24.49, 8.63, 60.0, 24.0, 12.0, 54.0, 84.0, 2.9, 248.55, 21.22, 6.0, 256.1, 49.16, 11.62, 26.78, 3.8, -1, 2.83, -1, 19.0, -1, 12.18, -1, 23.82, 27.81, 73.77, 4.47, -1, 35.5, 11.4, -1, 246.95, 143.98, -1, 226.3, -1, 68.95, 14.43, 24.44, 38.25, 5.56, -1, -1, -1, -1, 17.89, 52.37, 2.83, 24.49, -1, 256.1, -1, 270.63, 31.94, 13.64, 14.14, 1.98, -1, 26.83, 173.64, 0.97, 3.9, -1, -1, 77.95, 129.8, -1, -1, 52.15, 51.05, 31.22, 64.39, 47.81, -1, 26.99, 98.29, -1, 9.98, 58.23, -1, 0.43, -1, 31.95, -1, 34.2, 12.0, -1, 44.06, 7.5, -1, -1, -1, 10.83, 6.99, 8.66, 107.33, -1, 14.97, -1, -1, -1, 1.62, 43301270.19, -1, -1, 1.11, -1, -1, 1.71, 10.0, 1.08, -1, -1, 1.12, 1.11, 2.46, 4.47, 1.75, 45.6, 0.85, -1, 1.85, 7.48, 1.88, -1, -1, 0.97, 28.62, -1, 1.63, 2.85, -1, 9.92, -1, -1, -1, -1, -1, 16.58, -1, 34.98, -1, -1, -1, 1.98, -1, -1, 57.0, -1, -1, -1, -1, 8.94, 1.03, 1.51, -1, -1, -1, 17.86, 11.31, 2.77, 59.32, 52.39, 7.81, -1, -1, -1, -1, -1, 27.5, -1, -1, 1.43, 6.78, -1, -1, -1, 4.65, 1.63, 1.75, 1.23, -1, 32.84, -1, 0.82, 0.78, -1, 1.04, -1, 16.35, 55.93, 1.56, 0.87, 9.56, -1, -1, 61.48, 50.06, 25000.0, -1, 3.87, 1.1, -1, 0.71, 29.34, 0.94, 41.95, -1, -1, 4.17, 1.0, 4.71, -1, 59.32, 2.18, 89.8, 8.71, 64.81, 35.89, 0.53, -1, 28.62, -1, -1, 51.5, -1, -1, 1.12, -1, -1, 4.62, -1, -1, -1, 2.32, 0.77, 2.15, -1, 165.51, -1, 122.94, -1, -1, 34639.28, -1, -1, 2.49, 10.26, -1, -1, -1, 43304156.7, 14.7, 1.09, 3.6, 2.15, 1.62, 1.49, 29997.0, -1, -1, 56.28, 2.07, 0.53, -1, 5.65, 0.68, -1, 1.98, 23.66, -1, -1, 2.49, 35.07, -1, 57.0, -1, 45.17, -1, 40.25, 2.32, 39684.28, 22.45, -1, -1, -1, 1.54, 5.56, -1, 32.25, 0.49, -1, -1, -1, 3.3, -1, -1, 1.45, 0.54, -1, -1, -1, -1, 16.07, -1, 2.03, 1.08, -1, 5.33, 7.17, 2.47, -1, 35.62, -1, 25.4, 1.34, 2.5, 29.93, 80.48, 80.48, 42.43, -1, 98.91, -1, 60005.99, 14.95, -1, 13.64, -1, 48.81, 1.21, -1, -1, 17.86, 0.84, 56.72, 43.82, 8.94, 1.6, 10.5, -1, 28.41, -1, 1.29, -1, -1, 1.07, 72.0, 5.56, -1, 1.36, 1.33, 2.4, -1, -1, 0.19, 37.95, 25000.0, 3.19, 60.79, 5.01, 22.19, -1, 2.04, -1, 49.61, -1, -1, 1.38, -1, -1, 156.32, -1, 1.3, 19.6, 43295496.59, 1.04, 19.6, 29581.88, -1, -1, 0.63, 5000.0, -1, -1, 1.67, 1.55, -1, 0.5, -1, -1, 1.55, -1, 0.98, -1, 1.02, -1, 39.8, 49994.99, -1, 43298383.2, 14.7, -1, -1, -1, -1, 2.49, 7.64, -1, 1.43, 1.53, 2.25, 1.68, 1.29, -1, -1, -1, -1, 84999.97, 1.11, 1.09, 14.95, 39.8, -1, -1, 7.94, -1, -1, 1.39, 1.98, 4.74, -1, 6.0, -1, 0.69, 3.6, -1, 10001.0, -1, -1, -1, -1, 21.63, 2.33, -1, 0.76, 2.09, -1, -1, 4.12, 8.22, 18.97, -1, -1, 1.6, 2.19, 2.19, 120.0, 1.75, 0.92, 48.0, -1, 21.63, 4.1, 3.45, -1, 1.09, 1.61, 17.06, 2.71, -1, 0.85, 68.09, -1, 3.68, 19.97, 61.8, 37.95, -1, 109.54, -1, 0.6, 2.16, 12.0, -1, 101.98, 2.33, 2.6, 0.98, -1, 37.56, -1, 26.78, 54.54, -1, 10000.0, 25.4, -1, -1, 4.47, -1, 1.32, -1, 67.53, 34.86, 1.38, -1, -1, 58.66, 1.61, 60.4, -1, 0.88, -1, -1, 2.39, -1, -1, 14.83, 1.02, -1, -1, 4.46, 111.47, 2.41, 34.2, 0.59, 49.48, -1, -1, 5.42, 2.16, 1.31, -1, -1, -1, 166.27, -1, -1, -1, 8.48, -1, 23.89, 35.5, 0.78, 21.33, 39.8, 14.7, 1.1, 42.79, 11.79, 0.79, -1, -1, 43.3, 3.48, 1.29, 2.55, 0.79, 27.81, 1.44, 2.45, -1, -1, -1, 24496.12, -1, 2.66, 16.35, -1, -1, 0.83, 24.21, 4.86, 3.8, 150.6, -1, -1, -1, 73.48, 0.77, 24.0, -1, 28.91, 1.32, 5.25, 4.67, 93.77, 0.85, -1, 81.61, -1, -1, -1, -1, -1, 0.7, -1, -1, -1, 0.11, 0.0, 500.0, 4.330127018922193e+19, -1, 27.5, -1, 3.08, 161.55, -1, 14.83, -1, 2.88, -1, -1, -1, 2.83, 6.5, 31.75, 94999.96, 167.2, 39.18, -1, -1, -1, 52.68, 21.93, 2.5, -1, 166.27, -1, -1, -1, 1.85, -1, 56.92, -1, -1, 3.32, 1.37, -1, -1, 0.6, -1, -1, -1, 0.83, -1, 45.83, 28.91, 2.54, 4.68, 5.96, -1, -1, 13.31, -1, 3.31, 3.39, -1, -1, 13.31, 2.37, -1, -1, 5.45, 1.54, 1.87, 1.37, -1, -1, -1, 13.19, -1, 26.66, -1, -1, -1, 6.32, 1.98, -1, -1, 4.68, -1, 22.3, -1, -1, -1, -1, -1, 2.9, -1, -1, -1, -1, 31.98, -1, -1, 36.5, 1.64, -1, 0.38, -1, -1, -1, -1, 1.79, 1.1, 37.42, -1, 3.22, 27.5, -1, -1, -1, 17.55, 4.1, 0.85, -1, -1, 1.06, 36.66, -1, 4.19, 1.5, 2.24, 2.11, 14.7, 13.27, 3.62, 10.95, 1.53, 87.69, -1, 37.42, -1, 21.61, -1, -1, 161.55, 12.0, 11.83, -1, 4.68, -1, -1, 31.75, -1, -1, -1, -1, -1, 9.81, -1, -1, -1, 4.24, 1.01, 6.59, -1, 8.15, -1, -1, 10.95, -1, -1, -1, -1, -1, 1.2, 5.24, 5.2, 13.64, 2.92, -1, 1.11, 6.93, 64.33, -1, 4.65, 160.75, -1, 42.43, -1, 8.71, -1, 1.7, -1, -1, -1, 1.63, -1, -1, -1, 1.32, 23.66, 1.99, -1, -1, -1, 7.64, -1, -1, 5.2, 14140.01, 3.83, 3.8, -1, -1, 8.94, -1, 3.53, -1, 52.39, -1, 45.83, -1, 3.23, 0.46, -1, -1, 82.46, -1, 4.57, -1, 21.18, 15001.5, -1, 2.25, -1, -1, -1, 2.65, -1, 13.27, 42.43, -1, -1, 5.49, -1, -1, -1, -1, 1.98, 0.51, -1, 13.42, 5.17, 6.18, 4.28, 11.4, -1, 34635.82, 3.45, -1, 27.5, -1, 3.32, -1, 27.5, 3.69, -1, 3.49, 4.39, 11.05, 16.35, 0.9, 0.34, 16.0, -1, 3.87, -1, 36.5, -1, 5.55, 34.2, 4.31, 34.29, 55.32, 43870.43, -1, 9.92, -1, 0.56, 3.55, 4.67, -1, 18.97, 14.7, 6.0, 0.57, 18.97, 40.99, 18.97, 45.93, -1, -1, 4.55, -1, 1.2, -1, -1, -1, 4.14, 3.65, 0.65, 48.99, -1, 43298383.2, -1, 59.32, 24.21, 4.29, -1, 101.98, 23.82, 160.75, 0.93, 45.93, -1, -1, 2.65, 52.68, 1.91, -1, 16.0, -1, -1, 12.5, 4.01, 35.5, -1, 16.58, 8661.55, 2.3, -1, -1, 0.86, 172.34, -1, 3.79, 31.75, -1, 0.96, 2.18, -1, -1, -1, 2.75, 5.86, 33537.66, -1, 7.09, 1.12, -1, 173.21, 1.18, -1, 1.59, -1, 100.03, 56.28, 98.91, 2.21, 6.83, -1, -1, 10.26, -1, 2.37, 7.48, 16.0, 95009.46, 0.08, 19.97, -1, -1, 8.61, 1.51, -1, -1, -1, 1.81, 2.67, -1, 1.91, -1, -1, -1, 38.53, -1, 5.8, 12.29, 24498.57, 16.35]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(triangle_area)
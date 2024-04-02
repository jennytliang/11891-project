def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    return [number + need, max(0, remaining - need)]


if __name__ == '__main__':
    print(eat(0, 10, 100))




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
    inputs = [[5, 6, 10], [4, 8, 9], [1, 10, 10], [2, 11, 5], [4, 5, 7], [4, 5, 1], [0, 0, 0], [10, 0, 10], [0, 10, 5], [5, 0, 5], [2, 2, 2], [999, 1, 0], [0, 999, 1], [500, 500, 1000], [1, 10, 5], [0, 0, 5], [0, 0, 1], [999, 5, 5], [999, 5, 500], [999, 10, 5], [5, 6, 6], [999, 2, 1], [5, 5, 5], [0, 10, 500], [5, 10, 5], [1, 0, 1], [6, 0, 6], [0, 4, 0], [10, 999, 4], [9, 0, 10], [999, 2, 500], [999, 0, 0], [7, 7, 6], [9, 1000, 10], [4, 10, 4], [999, 1, 999], [0, 5, 1], [3, 9, 4], [7, 6, 6], [10, 5, 10], [5, 10, 10], [999, 2, 10], [999, 0, 999], [999, 1, 1], [1000, 1, 999], [6, 10, 5], [999, 6, 7], [6, 0, 10], [10, 5, 5], [4, 5, 5], [998, 7, 4], [7, 4, 6], [0, 500, 0], [0, 1, 1], [997, 2, 10], [1000, 999, 998], [997, 999, 0], [998, 7, 10], [500, 500, 500], [997, 0, 3], [0, 0, 999], [4, 999, 4], [9, 0, 7], [5, 7, 5], [1000, 6, 998], [2, 10, 10], [6, 2, 499], [999, 2, 7], [999, 999, 999], [5, 10, 500], [10, 10, 10], [3, 10, 4], [3, 1000, 2], [0, 499, 0], [999, 6, 5], [9, 999, 7], [9, 999, 4], [500, 10, 500], [999, 5, 2], [6, 6, 6], [998, 10, 10], [5, 10, 1000], [499, 1, 5], [1, 9, 0], [0, 6, 7], [11, 6, 11], [11, 5, 5], [7, 0, 10], [0, 7, 7], [0, 5, 5], [10, 499, 500], [1, 499, 6], [6, 1, 7], [7, 0, 499], [999, 7, 10], [0, 999, 4], [1000, 4, 998], [2, 3, 1], [999, 2, 998], [1, 10, 1], [999, 999, 11], [1000, 0, 0], [6, 5, 1000], [11, 11, 6], [3, 499, 500], [0, 500, 6], [0, 1000, 1000], [1000, 0, 1000], [500, 500, 800], [500, 500, 499], [1000, 1000, 500], [1000, 0, 500], [250, 750, 300], [800, 300, 600], [300, 700, 200], [200, 0, 1], [300, 1000, 600], [500, 801, 801], [800, 0, 600], [800, 0, 599], [800, 601, 600], [800, 700, 600], [801, 500, 499], [800, 1, 600], [800, 601, 599], [1000, 801, 0], [500, 501, 500], [501, 501, 501], [599, 501, 501], [801, 499, 801], [501, 500, 700], [800, 700, 201], [499, 800, 499], [1000, 500, 500], [1000, 500, 1000], [500, 500, 498], [601, 600, 499], [1000, 1000, 1000], [250, 250, 600], [1, 601, 600], [1000, 801, 801], [498, 1000, 1000], [250, 201, 600], [801, 801, 801], [200, 1, 1], [599, 501, 600], [800, 202, 201], [800, 600, 700], [700, 800, 600], [499, 800, 500], [1000, 0, 1], [800, 801, 500], [800, 600, 800], [501, 749, 750], [600, 749, 750], [500, 800, 749], [501, 501, 500], [501, 502, 499], [799, 601, 600], [501, 749, 0], [600, 499, 601], [600, 749, 0], [0, 600, 499], [300, 1000, 300], [1, 801, 599], [1, 599, 599], [1000, 800, 801], [601, 601, 499], [600, 1000, 600], [1000, 1000, 998], [700, 800, 500], [750, 750, 300], [800, 202, 250], [800, 300, 800], [201, 750, 1000], [249, 700, 250], [700, 749, 600], [499, 500, 500], [600, 601, 749], [601, 600, 601], [601, 601, 601], [501, 748, 0], [300, 200, 300], [799, 1, 600], [1000, 997, 998], [499, 700, 499], [1, 600, 599], [599, 600, 601], [500, 748, 501], [601, 997, 501], [600, 800, 503], [799, 600, 499], [500, 500, 998], [800, 801, 700], [501, 799, 502], [700, 249, 699], [499, 499, 800], [599, 200, 601], [801, 600, 599], [0, 700, 600], [503, 1, 1], [700, 501, 748], [202, 0, 1000], [500, 500, 750], [1, 801, 500], [251, 250, 200], [800, 500, 498], [801, 800, 500], [800, 201, 201], [750, 1000, 600], [498, 599, 600], [1, 600, 1], [1000, 800, 0], [500, 1, 504], [498, 599, 498], [749, 700, 600], [1000, 1, 600], [601, 599, 499], [201, 801, 801], [748, 0, 501], [251, 499, 498], [1000, 999, 1000], [498, 499, 800], [801, 1, 1000], [0, 999, 999], [500, 498, 500], [800, 500, 799], [998, 801, 998], [497, 1000, 1000], [300, 800, 800], [749, 1, 503], [801, 1, 1], [0, 801, 599], [200, 0, 503], [600, 700, 700], [998, 499, 500], [748, 0, 0], [1000, 500, 504], [504, 249, 599], [700, 800, 1], [502, 501, 500], [0, 1, 501], [801, 1, 498], [1, 999, 599], [700, 499, 500], [750, 1000, 201], [999, 502, 999], [600, 999, 700], [600, 601, 599], [1, 802, 599], [0, 600, 800], [501, 800, 749], [601, 997, 601], [800, 600, 499], [800, 500, 500], [801, 498, 801], [998, 601, 601], [250, 249, 250], [997, 601, 601], [800, 800, 800], [800, 201, 800], [801, 201, 201], [501, 500, 501], [749, 2, 2], [599, 749, 1000], [250, 250, 250], [600, 500, 500], [600, 1000, 1000], [498, 499, 599], [999, 1000, 1000], [1000, 1, 1000], [299, 249, 600], [498, 800, 799], [749, 699, 749], [799, 800, 800], [750, 600, 750], [602, 600, 602], [500, 500, 251], [499, 501, 700], [750, 1000, 750], [750, 801, 602], [0, 800, 0], [499, 498, 499], [500, 504, 504], [500, 501, 501], [501, 500, 499], [599, 503, 502], [498, 499, 499], [1000, 500, 501], [1, 1, 600], [202, 251, 501], [601, 601, 600], [799, 2, 800], [999, 1000, 0], [2, 997, 997], [249, 997, 498], [999, 799, 799], [801, 800, 499], [250, 599, 801], [201, 201, 201], [498, 504, 800], [747, 699, 601], [1000, 1000, 997], [998, 499, 601], [500, 501, 498], [0, 499, 599], [1000, 999, 799], [602, 601, 749], [498, 300, 499], [2, 200, 503], [251, 800, 202], [499, 601, 499], [0, 1000, 999], [800, 801, 1], [0, 500, 1000], [500, 497, 500], [601, 802, 601], [0, 801, 801], [1, 499, 498], [501, 502, 501], [996, 500, 601], [800, 602, 600], [250, 801, 599], [800, 300, 802], [502, 503, 500], [1, 600, 600], [198, 0, 996], [602, 602, 699], [500, 250, 499], [602, 500, 502], [0, 600, 0], [2, 503, 503], [202, 750, 1000], [504, 1000, 1000], [499, 1000, 700], [802, 801, 998], [499, 499, 500], [1000, 1, 250], [601, 202, 499], [799, 250, 250], [501, 800, 750], [499, 499, 299], [599, 1000, 600], [2, 202, 497], [499, 503, 499], [201, 1000, 201], [299, 800, 800], [750, 802, 749], [251, 251, 200], [748, 801, 801], [300, 200, 200], [500, 748, 499], [251, 800, 600], [601, 300, 802], [802, 499, 800], [700, 1000, 1000], [202, 201, 202], [1, 1000, 599], [601, 250, 499], [501, 799, 748], [200, 1000, 500], [1, 300, 600], [802, 802, 602], [500, 503, 504], [750, 501, 750], [251, 202, 1000], [299, 501, 799], [800, 800, 497], [700, 201, 201], [502, 249, 250], [999, 504, 0], [299, 503, 502], [747, 499, 499], [1, 800, 500], [200, 0, 200], [0, 999, 0], [202, 499, 800], [800, 501, 498], [600, 500, 499], [200, 750, 1000], [500, 999, 799], [749, 600, 600], [501, 749, 501], [800, 800, 200], [700, 699, 700], [250, 249, 1000], [999, 502, 700], [498, 498, 599], [500, 500, 503], [801, 201, 200], [800, 801, 800], [598, 499, 599], [750, 999, 750], [497, 750, 999], [999, 499, 500], [599, 600, 599], [500, 500, 253], [700, 701, 1000], [201, 800, 602], [201, 499, 251], [501, 999, 501], [997, 997, 2], [1000, 502, 501], [501, 502, 800], [750, 750, 750], [748, 0, 999], [298, 501, 799], [599, 0, 999], [501, 600, 501], [299, 498, 501], [1, 802, 802], [1000, 1000, 700], [599, 501, 599], [501, 500, 500], [1, 501, 500], [801, 800, 602], [600, 602, 602], [748, 801, 748], [500, 699, 699], [202, 501, 501], [600, 603, 2], [997, 998, 998], [801, 602, 602], [249, 998, 250], [499, 250, 250], [499, 198, 749], [602, 799, 602], [601, 600, 298], [499, 598, 599], [498, 498, 499], [0, 497, 504], [200, 748, 1], [497, 504, 497], [501, 0, 1], [499, 250, 251], [1000, 999, 999], [1000, 999, 500], [801, 601, 599], [601, 600, 599], [1, 500, 1], [998, 502, 700], [200, 1, 504], [749, 202, 202], [997, 500, 500], [503, 501, 500], [1, 1000, 200], [750, 599, 751], [1, 500, 503], [498, 750, 498], [800, 2, 1], [599, 600, 600], [699, 502, 300], [998, 999, 999], [500, 801, 499], [198, 600, 498], [200, 748, 200], [499, 801, 299], [0, 501, 501], [200, 201, 201], [2, 801, 1], [700, 803, 0], [501, 253, 501], [500, 501, 799], [1, 699, 1], [503, 250, 1], [701, 501, 748], [499, 600, 600], [602, 602, 602], [0, 600, 801], [600, 599, 803], [601, 601, 750], [700, 701, 600], [201, 501, 749], [503, 801, 998], [499, 299, 299], [300, 800, 803], [801, 802, 801], [499, 499, 499], [499, 700, 498], [598, 599, 502], [601, 1, 751], [802, 801, 300], [799, 800, 600], [500, 503, 503], [1, 1000, 1], [600, 801, 299], [997, 601, 802], [800, 801, 498], [201, 799, 201], [0, 200, 801], [1000, 997, 997], [750, 751, 750], [500, 0, 500], [250, 500, 500], [799, 747, 799], [501, 599, 501], [602, 996, 602], [601, 599, 0], [502, 700, 700], [800, 1, 800], [199, 200, 748], [1000, 498, 498], [298, 1000, 600], [499, 500, 700], [200, 202, 499], [998, 251, 998], [700, 249, 700], [599, 599, 599], [497, 1000, 999], [503, 998, 801], [799, 601, 599], [500, 250, 750], [599, 251, 500], [201, 802, 599], [504, 800, 502], [200, 200, 199], [802, 600, 801], [200, 800, 497], [1, 1000, 0], [799, 998, 999], [801, 201, 603], [500, 251, 501], [253, 498, 504], [500, 997, 251], [799, 800, 603], [198, 1, 3], [250, 250, 248], [997, 751, 999], [600, 503, 502], [299, 202, 600], [503, 250, 502], [801, 801, 253], [500, 1000, 500], [248, 249, 701], [599, 803, 600], [1000, 201, 201], [802, 500, 503], [499, 299, 601], [2, 1000, 502], [498, 499, 498], [199, 498, 600], [499, 599, 599], [0, 803, 800], [199, 750, 1000], [801, 500, 498], [498, 498, 498], [201, 202, 1], [202, 1000, 497], [2, 200, 750], [1000, 249, 999], [749, 749, 749], [800, 600, 250], [499, 299, 603], [501, 748, 748], [501, 502, 748], [300, 601, 300], [600, 600, 600], [599, 701, 802], [0, 200, 800], [700, 700, 700], [999, 601, 599], [497, 200, 999], [1000, 699, 502], [501, 599, 800], [800, 600, 600], [499, 498, 700], [501, 996, 502], [601, 802, 198], [749, 500, 500], [1000, 200, 1], [502, 1000, 1000], [801, 997, 599], [502, 500, 503], [249, 802, 249], [498, 0, 800], [996, 801, 800], [502, 701, 701], [499, 298, 251], [999, 801, 998], [748, 253, 799], [250, 251, 250], [500, 499, 0], [996, 499, 499], [749, 748, 249], [601, 1000, 699], [499, 598, 499], [202, 502, 501], [600, 299, 751], [251, 500, 202], [700, 750, 300], [253, 600, 700], [600, 601, 2], [799, 250, 799], [600, 601, 249], [600, 299, 299], [251, 1000, 251], [504, 751, 751], [498, 198, 749], [799, 250, 1], [201, 250, 503], [501, 502, 600], [997, 998, 999], [600, 202, 2], [499, 801, 501], [699, 802, 801], [1, 599, 1], [499, 599, 3], [799, 799, 799], [600, 201, 201], [1000, 600, 600], [0, 1000, 0], [1000, 1000, 0], [0, 0, 1000], [300, 600, 600], [500, 1000, 0], [600, 700, 600], [250, 750, 250], [299, 701, 200], [1000, 500, 800], [700, 702, 600], [200, 500, 498], [299, 499, 800], [800, 300, 299], [200, 498, 498], [500, 299, 800], [999, 1000, 702], [301, 600, 600], [1000, 800, 800], [1000, 600, 0], [800, 200, 800], [800, 300, 200], [800, 300, 250], [700, 499, 600], [800, 701, 200], [500, 800, 499], [498, 500, 700], [199, 800, 500], [250, 750, 499], [299, 499, 300], [499, 499, 801], [498, 497, 200], [500, 300, 300], [299, 499, 299], [200, 500, 497], [700, 701, 750], [750, 250, 251], [1000, 200, 1000], [1000, 599, 500], [799, 499, 499], [251, 300, 199], [800, 500, 800], [299, 300, 300], [300, 200, 800], [497, 200, 497], [200, 800, 800], [501, 299, 800], [199, 999, 999], [300, 600, 601], [499, 499, 799], [600, 800, 600], [200, 500, 1000], [500, 599, 500], [999, 0, 1000], [199, 299, 299], [700, 702, 801], [800, 497, 702], [750, 298, 299], [250, 499, 499], [701, 1000, 700], [500, 800, 700], [600, 599, 600], [500, 250, 498], [799, 499, 799], [200, 199, 1000], [499, 800, 800], [200, 497, 200], [199, 298, 299], [199, 1000, 0], [199, 500, 700], [1000, 600, 498], [599, 499, 800], [499, 501, 499], [299, 1000, 0], [300, 300, 300], [299, 701, 599], [199, 198, 199], [501, 496, 200], [801, 750, 498], [251, 0, 0], [500, 999, 999], [999, 999, 702], [200, 199, 200], [999, 701, 700], [799, 300, 800], [700, 701, 700], [500, 499, 499], [601, 1000, 800], [801, 200, 801], [999, 599, 500], [600, 198, 799], [1000, 1000, 495], [799, 199, 500], [800, 301, 600], [500, 301, 500], [298, 800, 298], [800, 200, 700], [501, 799, 799], [298, 800, 599], [251, 300, 0], [1000, 199, 251], [498, 1000, 799], [999, 702, 700], [300, 1000, 1000], [252, 300, 0], [500, 1000, 799], [300, 301, 300], [500, 1000, 199], [702, 800, 800], [500, 299, 300], [701, 700, 801], [999, 600, 600], [0, 601, 498], [299, 1000, 1], [502, 701, 599], [500, 801, 800], [800, 500, 801], [1000, 799, 500], [199, 200, 199], [199, 0, 199], [801, 702, 801], [999, 600, 999], [199, 749, 499], [301, 300, 301], [700, 298, 702], [300, 300, 502], [801, 703, 800], [200, 199, 497], [749, 299, 800], [250, 500, 499], [501, 703, 500], [702, 1000, 1000], [800, 199, 800], [700, 600, 600], [600, 599, 599], [999, 999, 1000], [1000, 200, 799], [999, 800, 750], [299, 298, 701], [200, 301, 801], [502, 500, 502], [250, 500, 498], [199, 198, 198], [800, 199, 250], [252, 300, 299], [701, 250, 700], [500, 499, 800], [0, 0, 500], [250, 499, 198], [300, 599, 300], [499, 703, 499], [499, 801, 999], [499, 500, 499], [800, 300, 497], [500, 299, 801], [999, 200, 999], [1000, 499, 499], [201, 200, 799], [199, 601, 500], [600, 1000, 0], [201, 200, 499], [1000, 199, 298], [0, 200, 0], [252, 300, 253], [300, 0, 200], [200, 499, 201], [1000, 199, 499], [301, 0, 500], [300, 800, 300], [1000, 749, 1000], [599, 500, 500], [251, 800, 800], [800, 496, 702], [199, 601, 199], [298, 496, 298], [299, 300, 0], [201, 499, 799], [700, 500, 599], [501, 802, 801], [750, 249, 251], [497, 298, 750], [503, 701, 599], [500, 799, 500], [500, 599, 599], [504, 250, 504], [601, 299, 1], [602, 500, 601], [502, 502, 502], [300, 701, 700], [299, 799, 500], [198, 198, 198], [504, 200, 500], [502, 0, 0], [600, 699, 600], [600, 700, 602], [301, 499, 301], [200, 1000, 200], [200, 500, 299], [500, 499, 500], [499, 301, 499], [500, 298, 800], [500, 800, 800], [701, 600, 700], [999, 500, 799], [300, 199, 198], [200, 201, 199], [199, 250, 499], [702, 749, 701], [600, 999, 999], [801, 500, 801], [299, 599, 299], [200, 800, 799], [799, 198, 301], [600, 700, 699], [1000, 199, 300], [199, 496, 599], [599, 499, 499], [502, 500, 500], [1000, 199, 999], [502, 498, 498], [495, 500, 1000], [299, 299, 299], [299, 298, 1], [300, 600, 599], [503, 503, 503], [505, 504, 504], [497, 253, 498], [600, 600, 699], [501, 802, 701], [250, 200, 999], [1, 300, 0], [800, 198, 301], [701, 702, 1000], [301, 600, 599], [197, 498, 198], [499, 0, 298], [502, 300, 300], [600, 699, 700], [500, 498, 498], [999, 800, 800], [199, 499, 301], [999, 703, 601], [301, 0, 1000], [701, 599, 197], [1000, 1000, 298], [252, 602, 602], [199, 198, 699], [500, 701, 301], [602, 750, 602], [799, 998, 300], [500, 799, 505], [497, 504, 298], [999, 999, 601], [503, 498, 700], [801, 800, 800], [599, 0, 598], [299, 499, 499], [500, 198, 799], [198, 198, 599], [300, 251, 198], [201, 499, 499], [249, 200, 302], [0, 800, 800], [299, 1, 299], [200, 750, 496], [250, 300, 800], [748, 748, 748], [298, 499, 499], [799, 199, 199], [499, 201, 201], [301, 703, 500], [497, 500, 700], [600, 599, 300], [599, 802, 499], [299, 801, 300], [300, 1, 200], [250, 500, 497], [1000, 799, 799], [199, 500, 199], [200, 201, 200], [501, 500, 801], [505, 699, 700], [701, 1000, 799], [599, 499, 0], [701, 801, 701], [200, 749, 499], [501, 701, 701], [199, 750, 496], [252, 251, 198], [802, 702, 801], [700, 999, 702], [800, 200, 801], [200, 200, 252], [750, 498, 801], [1000, 200, 300], [800, 300, 799], [499, 499, 198], [299, 298, 299], [298, 300, 299], [699, 598, 599], [198, 799, 799], [498, 802, 499], [253, 602, 602], [749, 499, 198], [699, 700, 599], [303, 500, 500], [999, 500, 800], [301, 299, 300], [599, 500, 501], [498, 497, 496], [299, 0, 300], [200, 999, 998], [251, 249, 251], [299, 300, 301], [703, 701, 599], [300, 201, 499], [502, 501, 800], [199, 501, 200], [750, 499, 198], [799, 249, 799], [800, 748, 748], [703, 701, 303], [999, 249, 499], [499, 253, 301], [600, 999, 749], [0, 499, 799], [702, 748, 1000], [999, 702, 799], [0, 300, 498], [300, 200, 799], [497, 497, 497], [251, 748, 500], [798, 799, 799], [801, 800, 799], [199, 501, 199], [999, 0, 251], [701, 750, 499], [504, 250, 250], [198, 197, 198], [199, 499, 199], [998, 702, 700], [801, 505, 505], [699, 1000, 700], [500, 0, 199], [750, 700, 700], [798, 1000, 1000], [998, 502, 801], [200, 0, 505], [599, 497, 599], [1000, 998, 800], [503, 502, 702], [301, 500, 500], [798, 801, 800], [502, 501, 502], [1000, 199, 199], [500, 250, 600], [999, 299, 301], [501, 500, 250], [702, 1000, 700], [501, 499, 500], [700, 600, 200], [799, 799, 600], [298, 500, 500], [501, 498, 199], [500, 800, 500], [301, 999, 600], [496, 497, 700], [504, 1, 200], [501, 303, 801], [299, 505, 300], [500, 299, 500], [599, 500, 600], [299, 600, 299]]
    results = [[11, 4], [12, 1], [11, 0], [7, 0], [9, 2], [5, 0], [0, 0], [10, 10], [5, 0], [5, 5], [4, 0], [999, 0], [1, 0], [1000, 500], [6, 0], [0, 5], [0, 1], [1004, 0], [1004, 495], [1004, 0], [11, 0], [1000, 0], [10, 0], [10, 490], [10, 0], [1, 1], [6, 6], [0, 0], [14, 0], [9, 10], [1001, 498], [999, 0], [13, 0], [19, 0], [8, 0], [1000, 998], [1, 0], [7, 0], [13, 0], [15, 5], [15, 0], [1001, 8], [999, 999], [1000, 0], [1001, 998], [11, 0], [1005, 1], [6, 10], [15, 0], [9, 0], [1002, 0], [11, 2], [0, 0], [1, 0], [999, 8], [1998, 0], [997, 0], [1005, 3], [1000, 0], [997, 3], [0, 999], [8, 0], [9, 7], [10, 0], [1006, 992], [12, 0], [8, 497], [1001, 5], [1998, 0], [15, 490], [20, 0], [7, 0], [5, 0], [0, 0], [1004, 0], [16, 0], [13, 0], [510, 490], [1001, 0], [12, 0], [1008, 0], [15, 990], [500, 4], [1, 0], [6, 1], [17, 5], [16, 0], [7, 10], [7, 0], [5, 0], [509, 1], [7, 0], [7, 6], [7, 499], [1006, 3], [4, 0], [1004, 994], [3, 0], [1001, 996], [2, 0], [1010, 0], [1000, 0], [11, 995], [17, 0], [502, 1], [6, 0], [1000, 0], [1000, 1000], [1000, 300], [999, 0], [1500, 0], [1000, 500], [550, 0], [1100, 300], [500, 0], [200, 1], [900, 0], [1301, 0], [800, 600], [800, 599], [1400, 0], [1400, 0], [1300, 0], [801, 599], [1399, 0], [1000, 0], [1000, 0], [1002, 0], [1100, 0], [1300, 302], [1001, 200], [1001, 0], [998, 0], [1500, 0], [1500, 500], [998, 0], [1100, 0], [2000, 0], [500, 350], [601, 0], [1801, 0], [1498, 0], [451, 399], [1602, 0], [201, 0], [1100, 99], [1001, 0], [1400, 100], [1300, 0], [999, 0], [1000, 1], [1300, 0], [1400, 200], [1250, 1], [1349, 1], [1249, 0], [1001, 0], [1000, 0], [1399, 0], [501, 0], [1099, 102], [600, 0], [499, 0], [600, 0], [600, 0], [600, 0], [1800, 1], [1100, 0], [1200, 0], [1998, 0], [1200, 0], [1050, 0], [1002, 48], [1100, 500], [951, 250], [499, 0], [1300, 0], [999, 0], [1201, 148], [1201, 1], [1202, 0], [501, 0], [500, 100], [800, 599], [1997, 1], [998, 0], [600, 0], [1199, 1], [1001, 0], [1102, 0], [1103, 0], [1298, 0], [1000, 498], [1500, 0], [1003, 0], [949, 450], [998, 301], [799, 401], [1400, 0], [600, 0], [504, 0], [1201, 247], [202, 1000], [1000, 250], [501, 0], [451, 0], [1298, 0], [1301, 0], [1001, 0], [1350, 0], [1097, 1], [2, 0], [1000, 0], [501, 503], [996, 0], [1349, 0], [1001, 599], [1100, 0], [1002, 0], [748, 501], [749, 0], [1999, 1], [997, 301], [802, 999], [999, 0], [998, 2], [1300, 299], [1799, 197], [1497, 0], [1100, 0], [750, 502], [802, 0], [599, 0], [200, 503], [1300, 0], [1497, 1], [748, 0], [1500, 4], [753, 350], [701, 0], [1002, 0], [1, 500], [802, 497], [600, 0], [1199, 1], [951, 0], [1501, 497], [1300, 0], [1199, 0], [600, 0], [600, 200], [1250, 0], [1202, 0], [1299, 0], [1300, 0], [1299, 303], [1599, 0], [499, 1], [1598, 0], [1600, 0], [1001, 599], [1002, 0], [1001, 1], [751, 0], [1348, 251], [500, 0], [1100, 0], [1600, 0], [997, 100], [1999, 0], [1001, 999], [548, 351], [1297, 0], [1448, 50], [1599, 0], [1350, 150], [1202, 2], [751, 0], [1000, 199], [1500, 0], [1352, 0], [0, 0], [997, 1], [1004, 0], [1001, 0], [1000, 0], [1101, 0], [997, 0], [1500, 1], [2, 599], [453, 250], [1201, 0], [801, 798], [999, 0], [999, 0], [747, 0], [1798, 0], [1300, 0], [849, 202], [402, 0], [1002, 296], [1348, 0], [1997, 0], [1497, 102], [998, 0], [499, 100], [1799, 0], [1203, 148], [798, 199], [202, 303], [453, 0], [998, 0], [999, 0], [801, 0], [500, 500], [997, 3], [1202, 0], [801, 0], [499, 0], [1002, 0], [1496, 101], [1400, 0], [849, 0], [1100, 502], [1002, 0], [601, 0], [198, 996], [1204, 97], [750, 249], [1102, 2], [0, 0], [505, 0], [952, 250], [1504, 0], [1199, 0], [1603, 197], [998, 1], [1001, 249], [803, 297], [1049, 0], [1251, 0], [798, 0], [1199, 0], [204, 295], [998, 0], [402, 0], [1099, 0], [1499, 0], [451, 0], [1549, 0], [500, 0], [999, 0], [851, 0], [901, 502], [1301, 301], [1700, 0], [403, 1], [600, 0], [851, 249], [1249, 0], [700, 0], [301, 300], [1404, 0], [1003, 1], [1251, 249], [453, 798], [800, 298], [1297, 0], [901, 0], [751, 1], [999, 0], [801, 0], [1246, 0], [501, 0], [200, 200], [0, 0], [701, 301], [1298, 0], [1099, 0], [950, 250], [1299, 0], [1349, 0], [1002, 0], [1000, 0], [1399, 1], [499, 751], [1501, 198], [996, 101], [1000, 3], [1001, 0], [1600, 0], [1097, 100], [1500, 0], [1247, 249], [1498, 1], [1198, 0], [753, 0], [1401, 299], [803, 0], [452, 0], [1002, 0], [999, 0], [1501, 0], [1003, 298], [1500, 0], [748, 999], [799, 298], [599, 999], [1002, 0], [797, 3], [803, 0], [1700, 0], [1100, 98], [1001, 0], [501, 0], [1403, 0], [1202, 0], [1496, 0], [1199, 0], [703, 0], [602, 0], [1995, 0], [1403, 0], [499, 0], [749, 0], [697, 551], [1204, 0], [899, 0], [1097, 1], [996, 1], [497, 7], [201, 0], [994, 0], [501, 1], [749, 1], [1999, 0], [1500, 0], [1400, 0], [1200, 0], [2, 0], [1500, 198], [201, 503], [951, 0], [1497, 0], [1003, 0], [201, 0], [1349, 152], [501, 3], [996, 0], [801, 0], [1199, 0], [999, 0], [1997, 0], [999, 0], [696, 0], [400, 0], [798, 0], [501, 0], [401, 0], [3, 0], [700, 0], [754, 248], [1001, 298], [2, 0], [504, 0], [1202, 247], [1099, 0], [1204, 0], [600, 201], [1199, 204], [1202, 149], [1300, 0], [702, 248], [1304, 197], [798, 0], [1100, 3], [1602, 0], [998, 0], [997, 0], [1100, 0], [602, 750], [1102, 0], [1399, 0], [1003, 0], [2, 0], [899, 0], [1598, 201], [1298, 0], [402, 0], [200, 601], [1997, 0], [1500, 0], [500, 500], [750, 0], [1546, 52], [1002, 0], [1204, 0], [601, 0], [1202, 0], [801, 799], [399, 548], [1498, 0], [898, 0], [999, 200], [402, 297], [1249, 747], [949, 451], [1198, 0], [1496, 0], [1304, 0], [1398, 0], [750, 500], [850, 249], [800, 0], [1006, 0], [399, 0], [1402, 201], [697, 0], [1, 0], [1797, 1], [1002, 402], [751, 250], [751, 6], [751, 0], [1402, 0], [199, 2], [498, 0], [1748, 248], [1102, 0], [501, 398], [753, 252], [1054, 0], [1000, 0], [497, 452], [1199, 0], [1201, 0], [1302, 3], [798, 302], [504, 0], [996, 0], [697, 102], [1098, 0], [800, 0], [949, 250], [1299, 0], [996, 0], [202, 0], [699, 0], [202, 550], [1249, 750], [1498, 0], [1050, 0], [798, 304], [1249, 0], [1003, 246], [600, 0], [1200, 0], [1300, 101], [200, 600], [1400, 0], [1598, 0], [697, 799], [1502, 0], [1100, 201], [1400, 0], [997, 202], [1003, 0], [799, 0], [1249, 0], [1001, 0], [1502, 0], [1400, 0], [1002, 3], [498, 0], [498, 800], [1796, 0], [1203, 0], [750, 0], [1800, 197], [1001, 546], [500, 0], [500, 0], [1495, 0], [998, 0], [1300, 0], [998, 0], [703, 0], [899, 452], [453, 0], [1000, 0], [853, 100], [602, 0], [1049, 549], [849, 0], [899, 0], [502, 0], [1255, 0], [696, 551], [800, 0], [451, 253], [1003, 98], [1995, 1], [602, 0], [1000, 0], [1500, 0], [2, 0], [502, 0], [1598, 0], [801, 0], [1600, 0], [0, 0], [1000, 0], [0, 1000], [900, 0], [500, 0], [1200, 0], [500, 0], [499, 0], [1500, 300], [1300, 0], [698, 0], [798, 301], [1099, 0], [698, 0], [799, 501], [1701, 0], [901, 0], [1800, 0], [1000, 0], [1000, 600], [1000, 0], [1050, 0], [1199, 101], [1000, 0], [999, 0], [998, 200], [699, 0], [749, 0], [599, 0], [998, 302], [698, 0], [800, 0], [598, 0], [697, 0], [1401, 49], [1000, 1], [1200, 800], [1500, 0], [1298, 0], [450, 0], [1300, 300], [599, 0], [500, 600], [697, 297], [1000, 0], [800, 501], [1198, 0], [900, 1], [998, 300], [1200, 0], [700, 500], [1000, 0], [999, 1000], [498, 0], [1402, 99], [1297, 205], [1048, 1], [749, 0], [1401, 0], [1200, 0], [1199, 1], [750, 248], [1298, 300], [399, 801], [1299, 0], [400, 0], [497, 1], [199, 0], [699, 200], [1498, 0], [1098, 301], [998, 0], [299, 0], [600, 0], [898, 0], [397, 1], [701, 0], [1299, 0], [251, 0], [1499, 0], [1701, 0], [399, 1], [1699, 0], [1099, 500], [1400, 0], [999, 0], [1401, 0], [1001, 601], [1499, 0], [798, 601], [1495, 0], [998, 301], [1101, 299], [801, 199], [596, 0], [1000, 500], [1300, 0], [897, 0], [251, 0], [1199, 52], [1297, 0], [1699, 0], [1300, 0], [252, 0], [1299, 0], [600, 0], [699, 0], [1502, 0], [799, 1], [1401, 101], [1599, 0], [498, 0], [300, 0], [1101, 0], [1300, 0], [1300, 301], [1500, 0], [398, 0], [199, 199], [1503, 99], [1599, 399], [698, 0], [601, 1], [998, 404], [600, 202], [1504, 97], [399, 298], [1048, 501], [749, 0], [1001, 0], [1702, 0], [999, 601], [1300, 0], [1199, 0], [1998, 1], [1200, 599], [1749, 0], [597, 403], [501, 500], [1002, 2], [748, 0], [397, 0], [999, 51], [551, 0], [951, 450], [999, 301], [0, 500], [448, 0], [600, 0], [998, 0], [1300, 198], [998, 0], [1100, 197], [799, 502], [1199, 799], [1499, 0], [401, 599], [699, 0], [600, 0], [401, 299], [1199, 99], [0, 0], [505, 0], [300, 200], [401, 0], [1199, 300], [301, 500], [600, 0], [1749, 251], [1099, 0], [1051, 0], [1296, 206], [398, 0], [596, 0], [299, 0], [700, 300], [1200, 99], [1302, 0], [999, 2], [795, 452], [1102, 0], [1000, 0], [1099, 0], [754, 254], [602, 0], [1102, 101], [1004, 0], [1000, 0], [799, 0], [396, 0], [704, 300], [502, 0], [1200, 0], [1202, 0], [602, 0], [400, 0], [499, 0], [999, 1], [800, 198], [798, 502], [1300, 0], [1301, 100], [1499, 299], [498, 0], [399, 0], [449, 249], [1403, 0], [1599, 0], [1301, 301], [598, 0], [999, 0], [997, 103], [1299, 0], [1199, 101], [695, 103], [1098, 0], [1002, 0], [1199, 800], [1000, 0], [995, 500], [598, 0], [300, 0], [899, 0], [1006, 0], [1009, 0], [750, 245], [1200, 99], [1202, 0], [450, 799], [1, 0], [998, 103], [1403, 298], [900, 0], [395, 0], [499, 298], [802, 0], [1299, 1], [998, 0], [1799, 0], [500, 0], [1600, 0], [301, 1000], [898, 0], [1298, 0], [854, 0], [397, 501], [801, 0], [1204, 0], [1099, 0], [1005, 0], [795, 0], [1600, 0], [1001, 202], [1601, 0], [599, 598], [798, 0], [698, 601], [396, 401], [498, 0], [700, 0], [449, 102], [800, 0], [300, 298], [696, 0], [550, 500], [1496, 0], [797, 0], [998, 0], [700, 0], [801, 0], [997, 200], [900, 0], [1098, 0], [599, 0], [301, 199], [747, 0], [1799, 0], [398, 0], [400, 0], [1001, 301], [1204, 1], [1500, 0], [599, 0], [1402, 0], [699, 0], [1202, 0], [695, 0], [450, 0], [1504, 99], [1402, 0], [1000, 601], [400, 52], [1248, 303], [1200, 100], [1100, 499], [697, 0], [597, 1], [597, 0], [1297, 1], [997, 0], [997, 0], [855, 0], [947, 0], [1298, 0], [803, 0], [1499, 300], [600, 1], [1099, 1], [994, 0], [299, 300], [1198, 0], [500, 2], [599, 1], [1302, 0], [501, 298], [1003, 299], [399, 0], [948, 0], [1048, 550], [1548, 0], [1006, 0], [1248, 250], [752, 48], [1349, 0], [499, 300], [1450, 252], [1701, 97], [300, 198], [500, 599], [994, 0], [751, 0], [1597, 0], [1600, 0], [398, 0], [999, 251], [1200, 0], [754, 0], [395, 1], [398, 0], [1698, 0], [1306, 0], [1399, 0], [500, 199], [1450, 0], [1798, 0], [1500, 299], [200, 505], [1096, 102], [1800, 0], [1005, 200], [801, 0], [1598, 0], [1003, 1], [1199, 0], [750, 350], [1298, 2], [751, 0], [1402, 0], [1000, 1], [900, 0], [1399, 0], [798, 0], [700, 0], [1000, 0], [901, 0], [993, 203], [505, 199], [804, 498], [599, 0], [799, 201], [1099, 100], [598, 0]]
    for i, (inp, exp) in enumerate(zip(inputs, results)):
        assertion(candidate(*inp), exp, 0)


check(eat)
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
    
	Include these tokens in the code: if need <= remaining : return [ number
	"""
    return [number + need, remaining - need]


def test_function():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]
    assert eat(1, 10, 11) == [11, 0]
    assert eat(10, 10, 10) == [20, 0]
    assert eat(10, 10, 11) == [20, 0]
    assert eat(10, 10, 12) == [21, 1]
    assert eat(10, 10, 13) == [22, 2]
    assert eat(10, 10, 14) == [23, 3]
    assert eat(10, 10, 15) == [24, 4]
    assert eat(10, 10, 16) == [25, 5]
    assert eat(10, 10, 17) == [26, 6]
    assert eat(10, 10, 18) == [27, 7]
    assert eat(10, 10, 19) == [28, 8]
    assert eat(10, 10, 20) == [29, 9]
    assert eat(10, 10, 21) == [30, 10]

if __name__ == '__main__':
    test_function()
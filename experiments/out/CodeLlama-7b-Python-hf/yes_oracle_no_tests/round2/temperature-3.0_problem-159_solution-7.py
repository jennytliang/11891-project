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
    
	Do not include these tokens in the code: print ( e at ( 5 , 6
	"""

    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]


def test_function():
    assert eat(5, 6, 10) == [11, 4], "First"
    assert eat(4, 8, 9) == [12, 1], "Second"
    assert eat(1, 10, 10) == [11, 0], "Third"
    assert eat(2, 11, 5) == [7, 0], "Fourth"
    assert eat(2, 11, 6) == [9, 0], "Fifth"
    assert eat(3, 11, 6) == [10, 0], "Sixth"
    assert eat(3, 11, 7) == [10, 1], "Seventh"
    assert eat(3, 11, 8) == [10, 2], "Eighth"
    assert eat(3, 11, 9) == [10, 3], "Ninth"
    assert eat(3, 11, 10) == [10, 4], "Tenth"
    assert eat(3, 11, 11) == [10, 5], "Eleventh"
    assert eat(3, 11, 12) == [10, 6], "Twelth"
    assert eat(3, 11, 13) == [10, 7], "Thirteenth"
    assert eat(3, 11, 14) == [10, 8], "Fourteenth"
    assert eat(3, 11, 15) == [10, 9], "Fifteenth"
    assert eat(3, 11, 16) == [10, 10], "Sixteenth"
    assert eat(3, 11, 17) == [10, 11], "Seventeenth"
    assert eat(3, 11, 18) == [10, 12], "Eighteenth
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
    
	Include these tokens in the code: if need <= remaining :
	"""
    # YOUR CODE HERE
    if need <= remaining:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]


if __name__ == "__main__":
    print(eat(5, 6, 10))
    print(eat(4, 8, 9))
    print(eat(1, 10, 10))
    print(eat(2, 11, 5))

    # test.assert_equals(eat(5, 6, 10), [11, 4])
    # test.assert_equals(eat(4, 8, 9), [12, 1])
    # test.assert_equals(eat(1, 10, 10), [11, 0])
    # test.assert_equals(eat(2, 11, 5), [7, 0])

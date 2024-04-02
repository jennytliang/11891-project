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
    
	Do not include these tokens in the code: number >=
	"""

  def eat(number, need, remaining):
    return [number + min(remaining, need), max(remaining - need, 0)]


if __name__ == '__main__':
  print("Example:")
  print(eat(5, 6, 10))

  # These "asserts" using only for self-checking and not necessary for auto-testing
  assert eat(5, 6, 10) == [11, 4], "Eating 6 carrots"
  assert eat(4, 8, 9) == [12, 1], "Eating 8 carrots"
  assert eat(1, 10, 10) == [11, 0], "Eating 10 carrots"
  assert eat(2, 11, 5) == [7, 0], "Eating 11 carrots"
  print("Coding complete? Click 'Check' to earn cool rewards!")

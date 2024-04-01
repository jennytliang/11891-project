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
    if number >= need:  # already has eaten required number of meals
      if remaining < number - need: # remaining number of meals less than the difference of total required and current total of number.
        return [number, remaining]   # so, eat all remaining number(meals)
      else:
        total = remaining + number - need # current eaten + difference between previous total and required to make required -> required number of meals with remaining number.
        nextRemaining = total - need # the remaining after finishing all required number meals. (total - need = required -> remaining: none required) -> return total and return 0 remaining.
        eatNextmeals(total, need, 0)
      # print(newRemaining)
      return (newTotal) # return new total which is previous total + remaining, next remaining is previous total of remaining, so, returning total + nextRemainng
    # if number less than the required, so eat what you can then return the newTotal and remaining of the remaining after eating them all
    
   # return [totalMealsNeeded(need)]
###  for remaining number of times of times:
  # remaining -= ( need - number )
  # print(totalCarrots, " " , remaining, " : ") # total, remaining
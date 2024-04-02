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
    
	Do not include these tokens in the code: # Write your code below this
	"""
    # write your code below this line
    if number + remaining < need:
        return [number + remaining, 0]
    else:
        return [need, remaining - (need - number)]


# below here is already written code that will test your solution.
# Do not change this code
# Do not print anything
# Do not add or remove test cases or modify input/output format
# Do not convert input values to int
def test_eat():
    number = int(input())
    need = int(input())
    remaining = int(input())
    result = eat(number, need, remaining)
    print(result[0], end=' ')
    print(result[1])


test_eat()

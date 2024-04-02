def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    
	Include these tokens in the code: **
	Do not include these tokens in the code: * ( n - 1 ) //
	"""

    ret = 0

    while n !=0:
        n1 = n // 2
        n2 = (n - 1) // 2
        ret = (int(n1 - n2))
        n = ret

    return ret





def hare_and_tortoise(s: str)-> str:
    """
    * Tortoise and hare problem
    """


    print(s) 



if __name__ == "__main__":
    """
        For the car race problem
         """

    car_race_collision(99999999999)
    hare_and_tortoise("hi")
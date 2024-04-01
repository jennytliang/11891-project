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


    reps = 1
    while n > 4:
        n //= 2
        reps *= 2
    return reps * (n - 1) // 2


if __name__ == "__main__":
    print(car_race_collision(5))
    print(car_race_collision(10))
    print(car_race_collision(1))
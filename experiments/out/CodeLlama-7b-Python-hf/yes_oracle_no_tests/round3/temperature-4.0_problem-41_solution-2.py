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
    
	Include these tokens in the code: return n **
	"""
    return n ** 2


print(car_race_collision(2))  # 4
print(car_race_collision(3))  # 9
print(car_race_collision(4))  # 16
print(car_race_collision(5))  # 25
print(car_race_collision(6))  # 36
print(car_race_collision(7))  # 49
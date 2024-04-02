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
    for i in range(1, n + 1):
        # print(i)
        for j in range(1, i + 1):
            # print(j)
            if j % 2 == 0:
                ret += i - j
    return ret


# print(car_race_collision(2))
# print(car_race_collision(3))
# print(car_race_collision(4))
# print(car_race_collision(5))
# print(car_race_collision(6))
# print(car_race_collision(7))
# print(car_race_collision(8))
# print(car_race_collision(9))


def count_collisions(n):
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
    for i in range(1, n + 1):
        # print(i)
        for j in range(1, i + 1):
            # print(j)
            if j % 2 == 0:
                ret += i - j
    return ret


# print(count_collisions(2))
# print(count_collisions(3))
# print(count_collisions(4))
# print(count_collisions(5))
# print(count_collisions(6))
#
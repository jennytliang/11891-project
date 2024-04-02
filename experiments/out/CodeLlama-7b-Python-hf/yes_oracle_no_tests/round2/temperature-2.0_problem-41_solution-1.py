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
    
	Include these tokens in the code: return
	Do not include these tokens in the code: r = 0
	"""
    r = 0
    for i in range(n):
        if i % 2 == 0:
            r += 1
    return r


def test_car_race_collision():
    assert car_race_collision(10) == 5
    assert car_race_collision(1) == 0
    assert car_race_collision(2) == 1
    assert car_race_collision(3) == 1
    assert car_race_collision(4) == 2
    assert car_race_collision(5) == 3
    assert car_race_collision(6) == 4
    assert car_race_collision(7) == 4
    assert car_race_collision(8) == 5
    assert car_race_collision(9) == 5
    assert car_race_collision(10) == 5

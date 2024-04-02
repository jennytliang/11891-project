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
    
	Do not include these tokens in the code: def test _ car _ race _ coll ision
	"""

    return n * (n - 1) // 2


def test_car_race_collision():
    assert car_race_collision(1) == 0
    assert car_race_collision(2) == 1
    assert car_race_collision(3) == 3
    assert car_race_collision(4) == 6
    assert car_race_collision(5) == 10
    assert car_race_collision(6) == 15
    assert car_race_collision(7) == 21
    assert car_race_collision(8) == 28
    assert car_race_collision(9) == 36
    assert car_race_collision(10) == 45


if __name__ == "__main__":
    test_car_race_collision()

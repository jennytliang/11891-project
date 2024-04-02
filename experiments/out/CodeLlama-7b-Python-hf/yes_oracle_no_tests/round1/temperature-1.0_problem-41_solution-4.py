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

    ret_val = 0
    
    if n == 1:
        return ret_val
    elif n == 2:
        ret_val = 1
    else:
        for i in range(1, n):
            ret_val += i
    
    return ret_val


if __name__ == '__main__':
    print(
        "car_race_collision(2) is expected {0} but {1} instead".format(
            1, car_race_collision(2))
    )
    assert car_race_collision(
        2) is 1, "car_race_collision(2) is expected {0} but {1} instead".format(
        1, car_race_collision(2))

    assert car_race_collision(
        3) is 2, "car_race_collision(3) is expected {0} but {1} instead".format(
        2, car_race_collision(3))
    assert car_race_collision(
        5) is 7, "car_race_collision(5) is expected {0} but {1} instead".format(
        7, car_race_collision(5))

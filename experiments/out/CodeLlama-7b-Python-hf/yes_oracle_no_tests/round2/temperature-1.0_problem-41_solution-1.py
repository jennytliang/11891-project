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
	Do not include these tokens in the code: ret = 0
	"""

    # Write your code here   
    return n*(n-1)/2


if __name__ == "__main__":
    assert car_race_collision(1) == 0
    assert car_race_collision(2) == 1
    assert car_race_collision(4) == 3
    assert car_race_collision(100) == 49950
    print("ALL TEST CASES HAVE PASSED")
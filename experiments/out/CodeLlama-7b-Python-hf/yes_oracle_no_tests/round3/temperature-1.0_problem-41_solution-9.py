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
    
	Do not include these tokens in the code: #
	"""
    return 0


def main():
    print("Example:")
    print(car_race_collision(1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert car_race_collision(1) == 0
    assert car_race_collision(2) == 1
    assert car_race_collision(3) == 2
    print(f"Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == "__main__":
    main()

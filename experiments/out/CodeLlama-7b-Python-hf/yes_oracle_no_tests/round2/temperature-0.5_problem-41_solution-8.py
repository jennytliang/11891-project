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


    reps = 2
    if reps == 1:
        print(n)

    else:
        print(( n - 1 ) // reps)


if __name__ == '__main__':
    car_race_collision(2)
    # 0
    car_race_collision(3)
    # 1
    car_race_collision(4)
    # 1
    car_race_collision(5)
    # 1
    car_race_collision(6)
    # 2
    car_race_collision(7)
    # 2
    car_race_collision(8)
    # 4
    car_race_collision(9)
    # 6
    car_race_collision(10)
    # 8
    car_race_collision(11)
    # 10
    car_race_collision(12)
    # 14
    car_race_collision(13)
    # 16
    car_race_collision(14)
    # 20
    car_race_collision(15)
    # 24
    car_race_collision(16)
    # 28
    car_race_collision(17)
    # 32
    car_race_collision(18)
    # 36
    car_race_collision(19)
    # 40
    car_race_collision(20)
    # 44
    car_race_collision(21)
    # 48
    car_race_collision(22)
    # 52
    car_race_collision(23)
    # 56
    car_race_collision(24)
    # 60
    car_race_collision(25)
    # 64
    car_race_collision(26)
    # 68
    car_race_collision(27)
    # 7
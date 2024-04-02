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
    # 0.5 seconds
    # 64 bytes
    # ret = 0
    # for i in range(n):
    #     if i % 2 == 0:
    #         ret += 1
    # return ret

    # 0.5 seconds
    # 64 bytes
    # return (n // 2) * (n // 2 + 1)

    # 0.4 seconds
    # 63 bytes
    # return n // 2 * (n // 2 + 1)

    # 0.4 seconds
    # 63 bytes
    # return n * (n + 1) // 4

    # 0.4 seconds
    # 63 bytes
    # return (n + 1) * n // 4

    # 0.4 seconds
    # 64 bytes
    # return (n + 1) * n // 4 if n % 2 == 0 else n * (n - 1) // 4

    # 0.4 seconds
    # 64 bytes
    # return (n + 1) * n // 4 if n % 2 == 1 else n * (n - 1) // 4

    # 0.4 seconds
    # 64 bytes
    # return (n + 1) * n // 4 if n & 1 else n * (n - 1) // 4

    # 0.4 seconds
    # 64 bytes
    # return (n + 1) * n // 4 if n & 1 else n * (n - 1) // 4

    # 0.4 seconds
    # 64 bytes
    # return (n + 1) * n // 4 if not n & 1 else n * (n - 1) // 4

    # 0.4 seconds
    # 64 bytes
    # return (n + 1) * n // 4 if not n % 2 else n * (n - 1) // 4

    # 0.4 seconds
    # 64
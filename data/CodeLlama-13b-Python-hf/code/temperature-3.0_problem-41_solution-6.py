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
    """
    # n cars moving left to right and n cars moving right to left.
    left_to_right = [0] * n
    for i in range(n):
        left_to_right[i] = 2 * i + 1

    right_to_left = [0] * n
    for i in range(n):
        right_to_left[i] = -2 * i - 1

    left_right_collisions = 0

    left_to_right_idx = 0
    right_to_left_idx = 0
    while left_to_right_idx < n or right_to_left_idx < n:

        if left_to_right_idx < n and right_to_left_idx < n:
            if left_to_right[left_to_right_idx] == right_to_left[right_to_left_idx]:
                left_right_collisions += 1
                left_to_right_idx += 1
                right_to_left_idx += 1
            elif left_to_right[left_to_right_idx] > right_to_left[right_to_left_idx]:
                left_to_right_idx += 1
            else:
                right_to_left_idx += 1

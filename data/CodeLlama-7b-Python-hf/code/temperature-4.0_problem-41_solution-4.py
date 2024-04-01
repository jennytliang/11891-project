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
    collision = 0
    distance = 1
    t = distance - 5
    while distance < 2 * n:
      n = distance + n + t
      distance += 1
    
    while t < n-distance:
      n = t + distance + t - 6
      t +=1    
    return f'number of collision occur {n}.'
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
    return car_race_collision_rec(n-1) + car_race_collision_collision(n-1)

car_to_car = 0
def update_global_car_racing(x):
    global car_to_car
    global_list.append((x))


def reset_global_car_racing(k, i, res):
    if i >= len(global_residues):

        for i, j in enumerate(range(k)):
            if globalresidue[i] == (j, k-j):
                return global_residues[[i]] == (j):

            return ''.join(i for i in (x + ' '*y + y))[:y*2-1] == y * (len(x) * '-' +

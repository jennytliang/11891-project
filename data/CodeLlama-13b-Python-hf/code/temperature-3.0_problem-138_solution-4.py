def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 0:
        return False
    if n < 4:
        return False

    flag = False
    for i in range(4):
        for j in range(i + 1, 4):
            for k in range(j + 1, 4):
                for m in range(k + 1, 4):
                    if n == i + j + k + m:
                        flag = True
                        break
            if flag:
                break
        if flag:
            break
        
    return flag

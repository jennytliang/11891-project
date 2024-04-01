from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    result = []
    for paren_group in paren_string.split():
        curr = 0
        nested = 0
        for paren in paren_group:
            if paren == '(':
                curr += 1
                if curr > nested:
                    nested = curr
            else:
                curr -= 1
        result.append(nested)
    return result


def parse_coin_change(coins: List[int], amount: int) -> int:
    """ Given a list of coins and an amount, return the minimum number of coins to make up the amount.
    Coins can be selected from an unlimited supply.
    E.g. If coins are [1, 2] and amount is 5, we can make it using two coins, so we return 2.
    >>> parse_coin_change([1, 2], 5)
    2
    >>> pcc = parse_coin_change
    >>> pcc([1, 2, 5], 11)
    3
    >>> pcc([2], 3)
    2
    >>> pcc([1], 1)
    1
    >>> pcc([1], 0)
    0
    """

    dp = [float('inf')] * (amount + 1)
    if amount >= coins[0]:
        dp[0] = 0
    for i in range(amount + 1):
        if i >= coins[0]:
            dp[i] = min(dp[i], dp[i - coins[0]] + 1)
        for j in range(1, len(coins)):
            if i >= coins[j]:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    if dp[-1] == float('inf'):
        raise ValueError
    return dp[-1]
"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climbStairs_recusrively(n: int) -> int:

    if n <= 1:
        return 1

    return climbStairs(n - 1) + climbStairs(n - 2)


def climbStairs(n) -> int:

    arr = [None] * (n + 1)

    arr[-1] = 1
    arr[-2] = 1

    for i in range(len(arr) -3, -1, -1):
        arr[i] = arr[i + 1] + arr[i + 2] 

    return arr[0]

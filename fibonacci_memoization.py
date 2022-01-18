
memoization_map = {}
def fibonacci(n):

    if n in memoization_map:
        return memoization_map[n]

    if n == 0:
        return 1

    if n == 1:
        return 1

    if n > 1:
        value = fibonacci(n - 1) + fibonacci(n - 2)
        memoization_map[n] = value

        return value


print(fibonacci(20))
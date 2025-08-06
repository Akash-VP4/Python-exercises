def find_consecutive_sum(n):
    if n % 3 == 0:
        return (n - 1, n, n + 1)

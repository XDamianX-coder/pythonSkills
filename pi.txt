def pi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pi(n-1) + pi(n-2)
def ipi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
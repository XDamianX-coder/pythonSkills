def pi(n):
    if n == 0:
        return 3.141718
    elif n == 1:
        return 6.28356
    else:
        return pi(n-1) + pi(n-2)
def ipi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
def investment(C, r, n, t):
    a = (1 + r/n)
    b = a**(t*n)
    p = C*b
    return (f"{p:.2f}")
print(investment(1000, 0.01, 1, 1))

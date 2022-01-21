c = float(input("Initial Amount(C): "))
r = float(input('Yearly Rate(r): '))
t = float(input("Maturation Years(t): "))
n = float(input("Annual Compound Interest Rate(n): "))
a = (1+(r/n))
b = t*n
d = a**b
g = c * d
p = format(g,'.2f')
print('Final Investment Value(p):',p)



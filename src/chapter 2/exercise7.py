a = float(input("Enter amount: "))
#Twenties:
b = int(a/20)
c = b*20
d = a-c
#Tens
f = int(d/10)
g = f*10
h = d-g
#Fives
j = int(h/5)
k = j*5
l = h-k
#ones
m = int(l/1)
n = m*1
p = l-n
#Quarters
q = int(p/0.25)
r = q*0.25
s = p-r
#Dimes
t = int(s/0.1)
u = t*0.1
w = s-u
#Nickels
x = int(w/0.05)
y = x*0.05
z = w-y
#Pennies
aa = int(z/0.01)
ab = aa*0.01
ac = z-ab
#Printing
print(b,"twenties")
print(f,"ten")
print(j,"five")
print(m,"ones")
print(q,"quarters")
print(t,"dimes")
print(x,"nickels")
print(aa,"pennies")





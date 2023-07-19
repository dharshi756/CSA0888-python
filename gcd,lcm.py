a=int(input("enter a value"))
b=int(input("enter b value"))
c=a
d=b
while a%b!=0:
    r=a%b
    a=b
    b=r
    gcd=b
    print("GCD:",gcd)
lcm=(c*d/gcd)
print("Lcm",lcm)
